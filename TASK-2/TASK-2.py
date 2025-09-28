# Initialize empty board
board = [" " for _ in range(9)]  # 0-8 positions

# Function to display the board
def print_board(board):
    for i in range(3):
        print(board[i*3] + " | " + board[i*3+1] + " | " + board[i*3+2])
        if i < 2:
            print("--+---+--")
    print()

# Function to check for a winner
def check_winner(board, player):
    win_positions = [
        [0,1,2], [3,4,5], [6,7,8],  # Rows
        [0,3,6], [1,4,7], [2,5,8],  # Columns
        [0,4,8], [2,4,6]            # Diagonals
    ]
    for pos in win_positions:
        if board[pos[0]] == board[pos[1]] == board[pos[2]] == player:
            return True
    return False

# Function to check for a tie
def is_tie(board):
    return " " not in board

# Minimax algorithm
def minimax(board, depth, is_maximizing):
    if check_winner(board, "O"):  # AI wins
        return 1
    elif check_winner(board, "X"):  # Human wins
        return -1
    elif is_tie(board):
        return 0

    if is_maximizing:
        best_score = -float('inf')
        for i in range(9):
            if board[i] == " ":
                board[i] = "O"
                score = minimax(board, depth+1, False)
                board[i] = " "
                best_score = max(score, best_score)
        return best_score
    else:
        best_score = float('inf')
        for i in range(9):
            if board[i] == " ":
                board[i] = "X"
                score = minimax(board, depth+1, True)
                board[i] = " "
                best_score = min(score, best_score)
        return best_score

# Function to find the best move for AI
def best_move(board):
    best_score = -float('inf')
    move = 0
    for i in range(9):
        if board[i] == " ":
            board[i] = "O"
            score = minimax(board, 0, False)
            board[i] = " "
            if score > best_score:
                best_score = score
                move = i
    return move

# Main game loop
def play_game():
    board = [" " for _ in range(9)]
    print("Positions are numbered 0-8 as below:")
    print_board([str(i) for i in range(9)])

    while True:
        # Human move
        move = input("Enter your move (0-8): ")
        if not move.isdigit() or int(move) < 0 or int(move) > 8:
            print("Invalid input. Enter a number between 0 and 8.")
            continue
        move = int(move)

        if board[move] == " ":
            board[move] = "X"
        else:
            print("Position already taken. Try again.")
            continue

        print_board(board)

        if check_winner(board, "X"):
            print("You win!")
            break
        elif is_tie(board):
            print("It's a tie!")
            break

        # AI move
        ai_move = best_move(board)
        board[ai_move] = "O"
        print("AI plays at position", ai_move)
        print_board(board)

        if check_winner(board, "O"):
            print("AI wins!")
            break
        elif is_tie(board):
            print("It's a tie!")
            break

# Start the game
if __name__ == "__main__":
    play_game()
