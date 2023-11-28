#!/usr/bin/env python3
"""connect_four.py"""

# code is modified form that given by Dr. David Biersach

# I used the hardcoding the solutions method that I used once for Tic-Tac-Toe
# chatgpt was used to adapt this to fit the 7x6 board 
    # (I asked it to show me a way look at each set of 4 in the board using for loops)
    # result is a list of hard coded winning patterns without having to write them all


def check_winner(board: list[list[int]]) -> int:
    """
    Checks the board and looks for a winner. Returns 0, 1, or 2.
    0 -> no winner, 1 -> player 1 won, 2 -> player 2 won.
    """
    # r = rows  c = column
    winning_patterns = [
        # Horizontal - for every row it checks each set of 4
        [(r, c), (r, c + 1), (r, c + 2), (r, c + 3)]
        for r in range(6)
        for c in range(4)
    ] + [
        # Vertical - for every column it checks each set of 4
        [(r, c), (r + 1, c), (r + 2, c), (r + 3, c)]
        for r in range(3)
        for c in range(7)
    ] + [
        # Diagonal (top-left to bottom-right)
        [(r, c), (r + 1, c + 1), (r + 2, c + 2), (r + 3, c + 3)]
        for r in range(3)
        for c in range(4)
    ] + [
        # Diagonal (top-right to bottom-left)
        [(r, c), (r + 1, c - 1), (r + 2, c - 2), (r + 3, c - 3)]
        for r in range(3)
        for c in range(6, 2, -1)
    ]

    # for each set (pattern) in the list if
    for pattern in winning_patterns:
        values = [board[row][col] for row, col in pattern]
        if len(set(values)) == 1 and values[0] != 0: 
            return values[0]
        
    return 0






def print_winner(board: list[list[int]]) -> None:
    """
    Prints the result of the check_winner function. Shows whether a player won or if
    if there is no winner yet with the current board.
    """
    print(*board, sep="\n")
    print()
    # we create a variable that stores the result of the check_winner returns (0, 1, 2)
    winner: int = check_winner(board)

    # print results based on the value of winner
    if winner != 0:
        print(f"Winner is Player {winner}\n")
    else:
        print("No winner\n")
      


def main() -> None:
    board1: list[list[int]] = [
        [0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 1, 0, 0],
        [0, 2, 2, 1, 1, 0, 0],
        [0, 2, 1, 2, 2, 0, 1],
        [2, 1, 1, 1, 2, 0, 2],
    ]
    print_winner(board1)

    board2: list[list[int]] = [
        [0, 0, 2, 0, 0, 0, 0],
        [0, 0, 1, 0, 0, 0, 0],
        [0, 0, 1, 0, 0, 0, 0],
        [0, 2, 2, 2, 2, 1, 0],
        [0, 1, 1, 2, 2, 2, 0],
        [2, 2, 1, 1, 1, 2, 0],
    ]
    print_winner(board2)

    board3: list[list[int]] = [
        [0, 0, 0, 2, 0, 0, 0],
        [0, 0, 0, 1, 0, 0, 0],
        [0, 0, 1, 1, 2, 2, 0],
        [0, 1, 2, 1, 2, 2, 0],
        [0, 2, 2, 2, 1, 1, 0],
        [0, 1, 1, 2, 1, 2, 0],
    ]
    print_winner(board3)


if __name__ == "__main__":
    main()
