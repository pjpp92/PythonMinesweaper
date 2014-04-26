from random import randint

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

board = Board(10,10,10)
bombs = board.bomb_place()


class Point(Board):
    def __init__(self, x, y, point_status, point_view):
        self.x = x
        self.y = y
        self.point_status = point_status
        self.point_view = point_view

    def full_board(self, Board, bombs):
        board_tab = []
        for item in range(Board.height):
            for item1 in range(Board.width):
                new_point = Point(item, item1, [item, item1] in bombs , False)
                board_tab.append(new_point)
        return board_tab

    def number(self, bombs):
        number = 0
        for item in range(-1,1):
            for item1 in range(-1,1):
                if [self.x + item, self.y + item1] in bombs:
                    number += 1
        return number

print ("bombs", bombs)
new_point = Point(0,0,True,True)
for item in new_point.full_board(board, bombs):
    print (item.x, item.y, item.point_status, item.point_view, item.number(bombs))
