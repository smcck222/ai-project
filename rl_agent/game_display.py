import time
from tkinter import Frame, Label, CENTER
import game_functions
import game_constants
import game_util_new


EDGE_LENGTH = 400
CELL_COUNT = 4
CELL_PAD = 10

UP_KEY = "'w'"
DOWN_KEY = "'s'"
LEFT_KEY = "'a'"
RIGHT_KEY = "'d'"
AI_KEY = "'q'"
AI_PLAY_KEY = "'p'"
GREEDY_KEY = "'g'"

LABEL_FONT = ("Verdana", 40, "bold")

GAME_COLOR = "#a6bdbb"

EMPTY_COLOR = "#8eaba8"

TILE_COLORS = {2: "#daeddf", 4: "#9ae3ae", 8: "#6ce68d", 16: "#42ed71",
               32: "#17e650", 64: "#17c246", 128: "#149938",
               256: "#107d2e", 512: "#0e6325", 1024: "#0b4a1c",
               2048: "#031f0a", 4096: "#000000", 8192: "#000000", }

LABEL_COLORS = {2: "#011c08", 4: "#011c08", 8: "#011c08", 16: "#011c08",
                32: "#011c08", 64: "#f2f2f0", 128: "#f2f2f0",
                256: "#f2f2f0", 512: "#f2f2f0", 1024: "#f2f2f0",
                2048: "#f2f2f0", 4096: "#f2f2f0", 8192: "#f2f2f0", }


class Display(Frame):
    def __init__(self, solver = None, matrix = None):
        Frame.__init__(self)

        self.grid()
        self.master.title('2048')
        #self.master.bind("<Key>", self.key_press)

        self.commands = {
                         UP_KEY: game_functions.move_up,
                         DOWN_KEY: game_functions.move_down,
                         LEFT_KEY: game_functions.move_left,
                         RIGHT_KEY: game_functions.move_right
                         # GREEDY_KEY = GreedySearch()
                         }

        self.grid_cells = []
        self.build_grid()
        self.init_matrix()
        self.draw_grid_cells(matrix)
        #self.update(solver)
        self.mainloop()


    def update(self, solver):
        move_made = None
        """"
        while not game_util_new.is_game_over(self.matrix) and solver != game_constants.MANUAL:
            if solver == game_constants.MDQN:
                move_made = GreedySearch(self.matrix).get_move()

            if move_made:
                self.matrix, _, _ = game_util_new.action_functions[move_made](self.matrix)
                self.matrix = game_functions.add_new_tile(self.matrix)
                self.draw_grid_cells()
                move_made = False
        
        """

        # time.sleep(1)
        # self.mainloop()

    def build_grid(self):
        background = Frame(self, bg=GAME_COLOR,
                           width=EDGE_LENGTH, height=EDGE_LENGTH)
        background.grid()
        
        for row in range(CELL_COUNT):
            grid_row = []
            for col in range(CELL_COUNT):
                cell = Frame(background, bg=EMPTY_COLOR,
                             width=EDGE_LENGTH / CELL_COUNT,
                             height=EDGE_LENGTH / CELL_COUNT)
                cell.grid(row=row, column=col, padx=CELL_PAD,
                          pady=CELL_PAD)
                t = Label(master=cell, text="",
                          bg=EMPTY_COLOR,
                          justify=CENTER, font=LABEL_FONT, width=5, height=2)
                t.grid()
                grid_row.append(t)

            self.grid_cells.append(grid_row)


    def init_matrix(self):
        self.matrix = game_functions.initialize_game()

    def draw_grid_cells(self,matrix):
        for row in range(CELL_COUNT):
            for col in range(CELL_COUNT):
                tile_value = matrix[row][col]
                if not tile_value:
                    self.grid_cells[row][col].configure(text="", bg=EMPTY_COLOR)
                else:
                    self.grid_cells[row][col].configure(text=str(2**tile_value), bg=TILE_COLORS[2**tile_value],fg=LABEL_COLORS[2**tile_value])

        self.update_idletasks()

    def key_press(self, event):
        print(self.matrix)
        valid_game = True
        key = repr(event.char)
        if key == GREEDY_KEY:
            move_made = GreedySearch(self.matrix).get_move()
            self.matrix, _, _ = game_util_new.action_functions[move_made](self.matrix)
            if move_made:
                self.matrix = game_functions.add_new_tile(self.matrix)
                self.draw_grid_cells()
                move_made = False

        elif key in self.commands:
            self.matrix, move_made, _ = self.commands[repr(event.char)](self.matrix)
            if move_made:
                self.matrix = game_functions.add_new_tile(self.matrix)
                self.draw_grid_cells()
                move_made = False




