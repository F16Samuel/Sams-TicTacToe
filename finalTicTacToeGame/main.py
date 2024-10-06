import time
import player
import comp
import util

while True:
    #Chose To Play Against Player or Computer
    pvpKey=0
    while True:
        pvp=input("Enter PvP if you want to Play against another Player\nEnter PvE if you want to Play against the Computer\n\nEnter Your Choice: ")
        if pvp=='PvP':
            pvpKey=1
            break
        elif pvp=='PvC':
            pvpKey=2
            break
        else:
            print("Invalid Input Try Again...")
    if pvpKey==1:
        player.play()
    elif pvpKey==2:
        comp.play()

    #Replayability of the game
    replay=input("Do You Wish to Play Again?? (Y/N): ")
    if replay=='N' or replay=='n':
        util.clear_console()
        print("Exiting the Game")
        time.sleep(2)
        break
    else:
        util.clear_console()
        print("Resetting the Board")
        time.sleep(2)
        util.clear_console()