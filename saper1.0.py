from random import randint
import Tkinter

class Board(object):
    def __init__(self, height, width, bomb_count):
        self.height = height
        self.width = width
        self.bomb_count = bomb_count

    def bomb_place(self):
        help = 0
        bomb_tab = []
        while help < self.bomb_count:
            bomb = randint(0, (self.height))
            bomb1 = randint(0, (self.width))
            if [bomb, bomb1] not in bomb_tab:
                bomb_tab.append([bomb, bomb1])
                help += 1
        return bomb_tab

    def full_board(self, bombs):
        full = [[Point(col, row, [col, row] in bombs, False) for col in range(self.height)] for row in range(self.width)]
        return full


class Point(Board):
    def __init__(self, x, y, point_status, point_view):
        self.x = x
        self.y = y
        self.point_status = point_status
        self.point_view = point_view
        self.number = self.calc_number(bombs)

    def full_board(self, Board, bombs):
        board_tab = []
        for item in range(Board.height):
            for item1 in range(Board.width):
                new_point = Point(item, item1, [item, item1] in bombs , False)
                board_tab.append(new_point)
        return board_tab

    def calc_number(self, bombs):
        number = 0
        for item in range(-1,1):
            for item1 in range(-1,1):
                if [self.x + item, self.y + item1] in bombs:
                    number += 1
        return number

board = Board(10,10,10)
bombs = board.bomb_place()
full_board = board.full_board(bombs)
for item in range(board.height):
    for item1 in range(board.width):
        print full_board[item][item1].x, full_board[item][item1].y,\
            full_board[item][item1].point_status, full_board[item][item1].point_view,\
            full_board[item][item1].number


print ("bombs", bombs)
new_point = Point(0,0,True,True)

class Gui:
    def __init__(self, mGui):
        mGui.title("Minesweaper")
        mGui.geometry("500x500")
        self.label = Tkinter.Label(mGui, text="abc").pack()
        self.button = Tkinter.Button(mGui, text="destroy", command=self.x)
        self.button.pack()
    def x(self):
        self.button.destroy()

mGui = Tkinter.Tk()
Gui(mGui)

mGui.mainloop()