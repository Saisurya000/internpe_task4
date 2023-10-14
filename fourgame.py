def print_board(board):
    for row in board:
        print(" | ".join(row))
        print("-" * (7 * len(row) - 1))

def check_winner(board, player):
    # Check horizontal
    for row in board:
        for i in range(len(row) - 3):
            if all(cell == player for cell in row[i:i+4]):
                return True

    # Check vertical
    for col in range(len(board[0])):
        for row in range(len(board) - 3):
            if all(board[row+i][col] == player for i in range(4)):
                return True

    # Check diagonal (top-left to bottom-right)
    for row in range(len(board) - 3):
        for col in range(len(board[0]) - 3):
            if all(board[row+i][col+i] == player for i in range(4)):
                return True

    # Check diagonal (top-right to bottom-left)
    for row in range(len(board) - 3):
        for col in range(3, len(board[0])):
            if all(board[row+i][col-i] == player for i in range(4)):
                return True

    return False

def is_board_full(board):
    return all(cell != " " for row in board for cell in row)

def main():
    rows = 6
    cols = 7
    board = [[" " for _ in range(cols)] for _ in range(rows)]
    player = "X"

    while True:
        print_board(board)
        col = int(input(f"Player {player}, choose a column (0-{cols-1}): "))
        
        if 0 <= col < cols and board[0][col] == " ":
            for row in range(rows - 1, -1, -1):
                if board[row][col] == " ":
                    board[row][col] = player
                    break
            if check_winner(board, player):
                print_board(board)
                print(f"Player {player} wins!")
                break
            elif is_board_full(board):
                print_board(board)
                print("It's a tie!")
                break
            player = "O" if player == "X" else "X"
        else:
            print("Invalid move. Try again.")

if __name__ == "__main__":
    main()
