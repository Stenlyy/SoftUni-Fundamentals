def check_winner(board, player):
    for colum in board:
        if colum.count(player) == 3:
            return True

    for index in range(3):
        row = [row[index] for row in board]
        if row.count(player) == 3:
            return True

    diagonal = [board[index][index] for index in range(len(board))]

    if diagonal.count(player) == 3:
        return True

    second_diagonal = [board[index][2 - index] for index in range(len(board))]

    if second_diagonal.count(player) == 3:
        return True


board = [list(map(int, input().split())) for _ in range(3)]

if check_winner(board, 1):
    print("First player won")

elif check_winner(board, 2):
    print("Second player won")

else:
    print("Draw!")
