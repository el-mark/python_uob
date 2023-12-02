import random

def generate_square_board():
    square_board = [[0,0],[0,0]]
    """
    change square_board above to reflect the 2 X 2 board
    insert code here to generate a square board of 2 X 2 with zeros
    """
    return square_board

def print_board(square_board):
    """
    :param square_board:
    print the board as instructed
    """
    board = ''
    for line in square_board:
        board += '|'
        for element in line:
            board += f' {str(element):<2}|'
        board += '\n'
           
    print(board)

def generate_numbers(square_board):
    """
    :param square_board:
    generate the random numbers to replace all zeros on the board
    """
    new_square_board = []
    for line in square_board:
        new_line = []
        for element in line:
            new_line.append(random.randint(1, 20))
        new_square_board.append(new_line)

    return new_square_board

def calculate_win(square_board):
    message = " "
    """
    :param square_board: 
    determine a win
    message = "There is a win"
    message = "No win"
   """
    total_sum = 0
    for line in square_board:
        total_sum += sum(line)
    # print(total_sum)
    
    if total_sum % 10 > 0:
        message = "No win"
    else:
        message = "There is a win"

    return (message)

"""
this part of the coding is for testing purposes only
"""
square_board = generate_square_board()
square_board = generate_numbers(square_board)
print_board(square_board)
message = calculate_win(square_board)
print(message)