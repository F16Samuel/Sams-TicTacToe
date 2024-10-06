import util
import display
import gamelogic

def play():
    currentBoard=[1,2,3,4,5,6,7,8,9]
    moveCount=0
    XwinCheck=0
    OwinCheck=0
    while True:
        #Player X Moves

        util.clear_console()
        display.disp(currentBoard)
        bUpdate=int(input("Enter Box Num You Want to Place X in (1-9)"))
        currentBoard[bUpdate-1]='X'
        util.clear_console()
        display.disp(currentBoard)
        XwinCheck=gamelogic.checkwin('X',currentBoard)
        if XwinCheck==1:
            print("X Wins!!")
            break
        moveCount=gamelogic.update(moveCount)
        if moveCount==9:
            print("Game is Draw!!")
            break

        #Player Y Moves

        util.clear_console()
        display.disp(currentBoard)
        bUpdate=int(input("Enter Box Num You Want to Place O in (1-9)"))
        currentBoard[bUpdate-1]='O'
        util.clear_console()
        display.disp(currentBoard)
        OwinCheck=gamelogic.checkwin('O',currentBoard)
        if OwinCheck==1:
            print("O Wins!!")
            break
        moveCount=gamelogic.update(moveCount)
        if moveCount==9:
            print("Game is Draw!!")
            break