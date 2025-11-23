#!/usr/bin/python3
def print_board(board):
    for row in board:
        print(" | ".join(row))
        print("-" * (len(row) * 4 - 1))  # طول السطر متناسب مع حجم الصف

def check_winner(board):
    # تحقق من الصفوف
    for row in board:
        if row.count(row[0]) == len(row) and row[0] != " ":
            return True, row[0]

    # تحقق من الأعمدة
    for col in range(len(board[0])):
        if board[0][col] == board[1][col] == board[2][col] and board[0][col] != " ":
            return True, board[0][col]

    # تحقق من الأقطار
    if board[0][0] == board[1][1] == board[2][2] and board[0][0] != " ":
        return True, board[0][0]

    if board[0][2] == board[1][1] == board[2][0] and board[0][2] != " ":
        return True, board[0][2]

    return False, None

def tic_tac_toe():
    board = [[" "]*3 for _ in range(3)]
    player = "X"
    while True:
        print_board(board)
        try:
            row = int(input(f"Enter row (0, 1, or 2) for player {player}: "))
            col = int(input(f"Enter column (0, 1, or 2) for player {player}: "))
            if row not in [0,1,2] or col not in [0,1,2]:
                print("Row and column must be 0, 1, or 2. Try again.")
                continue
        except ValueError:
            print("Invalid input. Please enter numbers only.")
            continue

        if board[row][col] != " ":
            print("That spot is already taken! Try again.")
            continue

        board[row][col] = player

        # تحقق من الفائز
        winner, win_player = check_winner(board)
        if winner:
            print_board(board)
            print(f"Player {win_player} wins!")
            break

        # تحقق من التعادل
        if all(cell != " " for row in board for cell in row):
            print_board(board)
            print("It's a tie!")
            break

        # تبديل اللاعب
        player = "O" if player == "X" else "X"

tic_tac_toe()
