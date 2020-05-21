#!/usr/bin/python

import sys
import random
from beautifultable import BeautifulTable

print('Number of arguments:', len(sys.argv), 'arguments')
print('Argument List:', str(sys.argv))

#Change Game
class MineGame():
    #Game will be 2D, 9 x 9 by default
    def __init__(self, rows=9, columns=9, difficulty='easy'):
        self.array2D = dict(((x, y), random.choice([-1, 0, 0]))
                            if difficulty == 'easy'
                            else ((x, y), random.choice([-1, -1, 0, 0, 0]))
                            if difficulty == 'medium'
                            else ((x, y), random.choice([-1, 0]))
                            for x in range(rows) for y in range(columns))
        self.rows = rows
        self.columns = columns

    def showState(self):
        table = BeautifulTable()
        table.column_headers = [""] + [str(i+1) for i in range(self.columns)]
        [table.append_row([str(j + 1)] + [str(self.array2D[i, j]) for i in range(self.columns)]) for j in range(self.rows)]
        print(table)

mines = MineGame()
mines.showState()
