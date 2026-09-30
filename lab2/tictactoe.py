board=list("123456789")
player="X"
wins=[(0,1,2),(3,4,5),(6,7,8),(0,3,6),(1,4,7),(2,5,8),(0,4,8),(2,4,6)]
while True:
    print(f"{board[0]}|{board[1]}|{board[2]}\n-+-+-\n{board[3]}|{board[4]}|{board[5]}\n-+-+-\n{board[6]}|{board[7]}|{board[8]}")
    try:
        move = int(input(f"Player {player}, enter your move (1-9): ")) - 1
    except ValueError:
        print("Invalid move, enter a number from 1 to 9.")
        continue
    if not 0 <= move < 9 or board[move] in "XO":
        print("Invalid move, try again.")
        continue

    board[move] = player
    if any(board[a]==board[b]==board[c]==player for a,b,c in wins):
        print(f"Player {player} wins!")
        break
    if all(cell in "XO" for cell in board):
        print("It's a draw!")
        break
    player="O" if player=="X" else "X"
        