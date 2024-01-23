import random


def print_board(board):
    for i in range(0, 9, 3):
        print(f" {board[i]} | {board[i+1]} | {board[i+2]} ")
        if i < 6:
            print("-----------")


def check_winner(board, player):
    winning_combinations = [
        [0, 1, 2],
        [3, 4, 5],
        [6, 7, 8],  # Rows
        [0, 3, 6],
        [1, 4, 7],
        [2, 5, 8],  # Columns
        [0, 4, 8],
        [2, 4, 6],  # Diagonals
    ]

    for combo in winning_combinations:
        if all(board[i] == player for i in combo):
            return True
    return False


def is_board_full(board):
    return all(cell != " " for cell in board)


def computer_move(board, player, computer):
    # Check for a winning move
    for i in range(9):
        if board[i] == " ":
            board[i] = computer
            if check_winner(board, computer):
                return i
            board[i] = " "  # Reset the move

    # Check for a blocking move
    for i in range(9):
        if board[i] == " ":
            board[i] = player
            if check_winner(board, player):
                return i
            board[i] = " "  # Reset the move

    # If no winning or blocking move, choose a random move
    empty_cells = [i for i in range(9) if board[i] == " "]
    if empty_cells:
        return random.choice(empty_cells)
    else:
        return None


board = [" " for _ in range(9)]
player = "X"
computer = "O"

while True:
    print_board(board)
    print(f"Player {player}'s turn")

    if player == "X":
        move = input("Enter a number (1-9) to make your move: ")

        if not move.isdigit() or not (1 <= int(move) <= 9):
            print("Invalid input. Please enter a number between 1 and 9.")
            continue

        index = int(move) - 1

        if board[index] == " ":
            board[index] = player
        else:
            print("That space is already taken. Try again.")
            continue
    else:
        # Computer's turn
        index = computer_move(board, player, computer)
        if index is not None:
            board[index] = computer
        else:
            print_board(board)
            print("It's a tie!")
            break

    if check_winner(board, player):
        print_board(board)
        print(f"Player {player} wins!")
        break
    elif is_board_full(board):
        print_board(board)
        print("It's a tie!")
        break

    player = "X" if player == "O" else "O"
