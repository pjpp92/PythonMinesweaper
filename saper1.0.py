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
            bomb = randint(0, (self.height)-1)
            bomb1 = randint(0, (self.width)-1)
            if [bomb, bomb1] not in bomb_tab:
                bomb_tab.append([bomb, bomb1])
                help += 1
        return bomb_tab

    def full_board(self, bombs):
        full =[]
        for i in range(self.height):
            full.append([])
            for j in range(self.width):
                full[i].append(Point(i, j, [i, j] in bombs, False))
        return full

class Point(Board):
    def __init__(self, x, y, point_status, point_view):
        self.x = x
        self.y = y
        self.point_status = point_status
        self.point_view = point_view
        self.number = self.calc_number(bombs)


    def calc_number(self, bombs):
        number = 0
        for item in range(3):
            for item1 in range(3):
                if [self.x + item -1, self.y + item1 -1] in bombs:
                    number += 1
        return number
board = Board(7,10,10)
bombs = board.bomb_place()
full_board = board.full_board(bombs)
for item in range(len(full_board)):
    for item1 in range(len(full_board[item])):
        print full_board[item][item1].x, full_board[item][item1].y,\
            full_board[item][item1].point_status, full_board[item][item1].point_view,\
            full_board[item][item1].number


print ("bombs", bombs)
new_point = Point(0,0,True,True)

class Gui:
    point_tab = []
    def __init__(self, mGui):
        mGui.title("Minesweaper")
        mGui.geometry("2000x2000")
        self.button = Tkinter.Button(mGui, text="destroy", command=self.y)
        self.button.pack()

    def x(self):
        self.button.destroy()

    def y(self):
        for item in range(len(full_board)):
            for item1 in range(len(full_board[item])):
                if full_board[item][item1].point_status:
                    help = Tkinter.Label(mGui, text="X")
                    help.pack()
                    help.place(x=15*item, y=15*item1)
                else:
                    txt = str(full_board[item][item1].number)
                    help = Tkinter.Label(mGui, text= txt)
                    help.pack()
                    help.place(x=15*item, y=15*item1)

mGui = Tkinter.Tk()

Gui(mGui)
mGui.mainloop()
