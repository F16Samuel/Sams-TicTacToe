import util
import display
import gamelogic
import random
import time

def play():
    currentBoard=[1,2,3,4,5,6,7,8,9]
    moveCount=0
    XwinCheck=0
    OwinCheck=0
    print("Computer Moves First!!")
    while True:
        #Computer Moves

        util.clear_console()
        display.disp(currentBoard)
        print("Computer is Thinking")
        time.sleep(1)
        remInt=[item for item in currentBoard if isinstance(item,int)]
        bUpdate=random.choice(remInt)
        currentBoard[bUpdate-1]='X'
        util.clear_console()
        display.disp(currentBoard)
        time.sleep(2)
        XwinCheck=gamelogic.checkwin('X',currentBoard)
        if XwinCheck==1:
            print("Computer Wins!!")
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
            print("Player Wins!!")
            break
        moveCount=gamelogic.update(moveCount)
        if moveCount==9:
            print("Game is Draw!!")
            break