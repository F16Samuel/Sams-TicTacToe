def checkwin(flag,board):
    if board[0]==flag and board[1]==flag and board[2]==flag:
        return 1
    elif board[3]==flag and board[4]==flag and board[5]==flag:
        return 1
    elif board[6]==flag and board[7]==flag and board[8]==flag:
        return 1
    elif board[0]==flag and board[3]==flag and board[6]==flag:
        return 1
    elif board[1]==flag and board[4]==flag and board[7]==flag:
        return 1
    elif board[2]==flag and board[5]==flag and board[8]==flag:
        return 1
    elif board[0]==flag and board[4]==flag and board[8]==flag:
        return 1
    elif board[2]==flag and board[4]==flag and board[6]==flag:
        return 1
    else:
        return 0

def update(flag):
    return flag+1