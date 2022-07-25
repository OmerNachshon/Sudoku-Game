import random

#more boards can be added!
boards = [[[3, 0, 6, 5, 0, 8, 4, 0, 0],
           [5, 2, 0, 0, 0, 0, 0, 0, 0],
           [0, 8, 7, 0, 0, 0, 0, 3, 1],
           [0, 0, 3, 0, 1, 0, 0, 8, 0],
           [9, 0, 0, 8, 6, 3, 0, 0, 5],
           [0, 5, 0, 0, 9, 0, 6, 0, 0],
           [1, 3, 0, 0, 0, 0, 2, 5, 0],
           [0, 0, 0, 0, 0, 0, 0, 7, 4],
           [0, 0, 5, 2, 0, 6, 3, 0, 0]]]

def get_random_board(): #get random board from board list
    i = random.randint(0, len(boards) - 1)
    return boards[i]
