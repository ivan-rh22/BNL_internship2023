#!/usr/bin/env python3
"""board_encoding.py"""

# some of the code was provided by Dr. Biersach and chatGPT
from typing import List

def decode_board(board_number: int) -> List[List[str]]:
    """Decodes the board by using the base 3 representation of the board number"""
    boardNumBase3 = base_10_to_base_3(board_number).zfill(9)
    board: List[List[str]] = [[] for _ in range(3)]
    # we are going to use this to traverse through the base 3 string
    index: int = 0
    # loop through the board list
    for i in range(3):
        for j in range(3):
            square_value: int = int(boardNumBase3[index])
            if square_value == 0:
                square = ' '
            elif square_value == 1:
                square = 'X'
            elif square_value == 2:
                square = 'O'
            else:
                print("ERROR: value out of range. check conversion")
            board[i].append(square)
            index += 1
    
    return board
    

def base_10_to_base_3(number: int) -> str:
    """
    Function returns a string that is the result of the conversion of the number in 
    base 10 to base 3
    """
    if number == 0:
        return '0'
    
    result: str = ''
    while number > 0:
        number, remainder = divmod(number, 3)
        result = str(remainder) + result
    return result

def printBoard(board: List[List[str]]) -> None:
    """Custom function to easily print a list[list[]] by row"""
    for row in board: 
        print(row)
    print()

def main() -> None:
    board1: List[List[str]] = decode_board(2271)
    board2: List[List[str]] = decode_board(1638)
    board3: List[List[str]] = decode_board(12065)

    print("Board Number: 2271")
    printBoard(board1)
    print("Board Number: 1638")
    printBoard(board2)
    print("Board Number: 12065")
    printBoard(board3)

    

if __name__ == "__main__":
    main()