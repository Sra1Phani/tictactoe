theBoard = {'topL':' ','topM':' ','topR':' ',
            'midL':' ','midM':' ','midR':' ',
            'lowL':' ','lowM':' ','lowR':' '}

def printBoard(board):
    print(board['topL']+'|'+board['topM']+'|'+board['topR'])
    print('-'*5)
    print(board['midL']+'|'+board['midM']+'|'+board['midR'])
    print('-'*5)
    print(board['lowL']+'|'+board['lowM']+'|'+board['lowR'])

def winCond(board):
    if board['topL']+board['topM']+board['topR']=='XXX' or board['topL']+board['topM']+board['topR']=='OOO':
        return True
    elif board['midL']+board['midM']+board['midR']=='XXX' or board['midL']+board['midM']+board['midR']=='OOO':
        return True
    elif board['lowL']+board['lowM']+board['lowR']=='XXX' or board['lowL']+board['lowM']+board['lowR']=='OOO':
        return True
    elif board['topL']+board['midL']+board['lowL']=='XXX' or board['topL']+board['midL']+board['lowL']=='OOO':
        return True
    elif board['topM']+board['midM']+board['lowM']=='XXX' or board['topM']+board['midM']+board['lowM']=='OOO':
        return True
    elif board['topR']+board['midR']+board['lowR']=='XXX' or board['topR']+board['midR']+board['lowR']=='OOO':
        return True
    elif board['topL']+board['midM']+board['lowR']=='XXX' or board['topL']+board['midM']+board['lowR']=='OOO':
        return True
    
turn = 'X'
win = False

for i in range(9):
    printBoard(theBoard)
    print('Turn for '+turn+'. Move on which space ?')
    move = input()
    theBoard[move] = turn
    
    win = winCond(theBoard)
    
    if win:
        print('Player with turn '+turn+' wins')
        break
    
    if turn == 'X':
        turn = 'O'
    else:
        turn = 'X'
if not win:
    print("It's a draw, neither player wins")
printBoard(theBoard)
