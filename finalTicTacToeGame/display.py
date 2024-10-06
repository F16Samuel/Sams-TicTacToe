def printBoxSep():
    print("+-----+-----+-----+")
def printBoxMid():
    print("|     |     |     |")
def printBoxVal(a,b,c):
    print("| ",a," |","",b," |","",c," |")

def disp(boardVals):
    printBoxSep()
    printBoxMid()
    printBoxVal(boardVals[0],boardVals[1],boardVals[2])
    printBoxMid()
    printBoxSep()
    printBoxMid()
    printBoxVal(boardVals[3],boardVals[4],boardVals[5])
    printBoxMid()
    printBoxSep()
    printBoxMid()
    printBoxVal(boardVals[6],boardVals[7],boardVals[8])
    printBoxMid()
    printBoxSep()
