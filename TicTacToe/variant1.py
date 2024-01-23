def print_board(board):
    for row in board:
        print(" | ".join(row))
        print("-" * 9)


def check_winner(board, player):
    for i in range(3):
        if all(board[i][j] == player for j in range(3)) or all(
            board[j][i] == player for j in range(3)
        ):
            return True
    if all(board[i][i] == player for i in range(3)) or all(
        board[i][2 - i] == player for i in range(3)
    ):
        return True
    return False


def is_board_full(board):
    return all(cell != " " for row in board for cell in row)


board = [[" " for _ in range(3)] for _ in range(3)]
player = "X"

while True:
    print_board(board)
    print(f"Player {player}'s turn")
    row, col = map(int, input("Enter row and column (e.g., 1 2): ").split())

    if row < 1 or row > 3 or col < 1 or col > 3 or board[row - 1][col - 1] != " ":
        print("Invalid move. Try again.")
        continue

    board[row - 1][col - 1] = player

    if check_winner(board, player):
        print_board(board)
        print(f"Player {player} wins!")
        break
    elif is_board_full(board):
        print_board(board)
        print("It's a tie!")
        break

    player = "X" if player == "O" else "O"
