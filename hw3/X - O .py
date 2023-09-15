
board = list(range(1, 10))

def draw_b(board):
    print('-------------')
    for i in range(3):
        print('|', board[0+i*3],'|', board[1+i*3],'|', board[2+i*3], '|')
    print('-------------')
draw_b(board)

def check_winer():
    win = ''
    result = [[0, 1, 2],[3, 4, 5],[6, 7, 8],[0, 3, 6],[1, 4, 7],
    [2, 5, 8],[0, 4, 8],[2, 4, 6]]
    for i in result:
        if board[i[0]] == 'X' and board[i[1]] == 'X' and board[i[2]] == 'X':
            win = 'X'
        if board[i[0]] == 'O' and board[i[1]] == 'O' and board[i[2]] == 'O':
            win = 'O'   
    return win

def step_maps(step,simvol):
    ind = board.index(step)
    board[ind] = simvol

def game():
    game_over = False
    player1 = True
    while game_over == False:
        if player1 == True:
            simvol = 'X'
            step = int(input("Первый игрок, ваш ход: "))
            step_maps(step,simvol)
            draw_b(board)
        else:
            simvol = 'O'
            step = int(input("Второй игрок, ваш ход: "))
            step_maps(step,simvol)
            draw_b(board)
        win = check_winer()
        if win != '':
            game_over = True
        else:
            game_over = False
        player1 = not(player1)  
    if win == 'X':
        print('Победил первый игрок')
    else:
        print('Победил второй игрок') 
game()