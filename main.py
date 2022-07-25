import boards
board=boards.get_random_board()
SIZE=len(board)

def print_board(board_input=None):
    if not board_input:
        print('input is invalid!')
    for i in range(len(board_input)):
        for j in range(len(board_input)):
            print(str(board_input[i][j])+' ',end='')
            if (j+1)%3==0 and j!=len(board_input)-1:
                print('| ',end='')
        if (i+1)%3==0 and i!=len(board_input)-1:
            print('\n'+'-'*21)
        else:
            print()

def check_row_num(board_input,r,c,num):
    for index in range(len(board_input)):
        if c!=index and board_input[r][index]==num:     # num already exists in row
            return False
    return True     # num is good for the given row

def check_col_num(board_input,r,c,num):
    for index in range (len(board_input)):
        if r!=index and board_input[index][c]==num:     # num already exists in col
            return False
    return True     # num is good for the given col

def check_box_num(board_input,r,c,num):
    row_check=(r//3)*3
    col_check=(c//3)*3
    for row in range(row_check,row_check+3):
        for col in range(col_check,col_check+3):
            if board_input[row][col]==num:
                if not (r==row and c==col):
                    return False    # num exists in box
    return True

def is_square_safe(board_input,r,c,num):   #checks row,col,box
    return check_col_num(board_input, r, c, num) and check_row_num(board_input, r, c, num) and check_box_num(board_input, r,c, num)

def check_board(board_input):   #checks if game is over!
    for r in range(len(board_input)):
        for c in range(len(board_input)):
            if board_input[r][c]==0:
                return False #board not complete
    return True     #board is complete!


def solve(board_input,r,c):
    if r==SIZE-1 and c==SIZE:     #if condition is matched , it means we covered the whole board
        return True
    if c==SIZE:
        c=0
        r+=1

    if board_input[r][c]!=0:
        return solve(board_input,r,c+1)
    for i in range(1,SIZE+1):
        board_input[r][c]=i
        if is_square_safe(board_input,r,c,i):
            if solve(board_input,r,c+1):
                return True
        board_input[r][c] = 0
    return False


print_board(board_input=board)










