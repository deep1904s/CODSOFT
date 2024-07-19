import math

AI_AGENT = 'X'
HUMAN_PLAYER = 'O'
EMPTY = ' '

def print_board(board):
    for row in board:
        print("|".join(row))
        print("-----")
    print()

def is_winner(board, player):
    lines = [  
        [(0, 0), (0, 1), (0, 2)],  
        [(1, 0), (1, 1), (1, 2)],
        [(2, 0), (2, 1), (2, 2)],
        [(0, 0), (1, 0), (2, 0)],  
        [(0, 1), (1, 1), (2, 1)],
        [(0, 2), (1, 2), (2, 2)],
        [(0, 0), (1, 1), (2, 2)],  
        [(0, 2), (1, 1), (2, 0)]
    ]
    return any(all(board[r][c] == player for r, c in line) for line in lines)

def game_over(board):
    return any(is_winner(board, player) for player in [AI_AGENT, HUMAN_PLAYER]) or all(board[r][c] != EMPTY for r in range(3) for c in range(3))

def available_moves(board):
    return [(r, c) for r in range(3) for c in range(3) if board[r][c] == EMPTY]

def minimax(board, depth, maximizing_player):
    if game_over(board):
        return 1 if is_winner(board, AI_AGENT) else (-1 if is_winner(board, HUMAN_PLAYER) else 0)

    best_eval = -math.inf if maximizing_player else math.inf
    player = AI_AGENT if maximizing_player else HUMAN_PLAYER

    for r, c in available_moves(board):
        board[r][c] = player
        eval = minimax(board, depth + 1, not maximizing_player)
        board[r][c] = EMPTY

        if maximizing_player:
            best_eval = max(best_eval, eval)
        else:
            best_eval = min(best_eval, eval)

    return best_eval

def get_best_move(board):
    best_move = None
    best_eval = -math.inf

    for r, c in available_moves(board):
        board[r][c] = AI_AGENT
        eval = minimax(board, 0, False)
        board[r][c] = EMPTY

        if eval > best_eval:
            best_eval = eval
            best_move = (r, c)

    return best_move

def main():
    board = [[EMPTY] * 3 for _ in range(3)]
    current_player = HUMAN_PLAYER

    while not game_over(board):
        print_board(board)

        if current_player == HUMAN_PLAYER:
            while True:
                try:
                    r, c = map(int, input("Enter row and column (0-2) for O: ").split(','))
                    if board[r][c] == EMPTY:
                        board[r][c] = HUMAN_PLAYER
                        current_player = AI_AGENT
                        break
                    else:
                        print("Invalid move. Try again.")
                except ValueError:
                    print("Invalid input. Please enter two integers separated by comma.")

        else:  
            r, c = get_best_move(board)
            board[r][c] = AI_AGENT
            current_player = HUMAN_PLAYER

    print_board(board)

    if is_winner(board, AI_AGENT):
        print("AI wins!")
    elif is_winner(board, HUMAN_PLAYER):
        print("Congratulations! You win!")
    else:
        print("It's a draw!")

if _name_ == "_main_":
    main()