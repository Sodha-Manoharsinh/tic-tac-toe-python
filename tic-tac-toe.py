import random

data = [1,2,3,4,5,6,7,8,9]
spaceLeft = 9

def board():
    print(" ",data[0]," | ",data[1]," | ",data[2])
    print(" ",data[3]," | ",data[4]," | ",data[5])
    print(" ",data[6]," | ",data[7]," | ",data[8])

def gameOver():
    # to check rows
    if data[0]==data[1]==data[2] or data[3]==data[4]==data[5] or data[6]==data[7]==data[8]:
        return True

    # to check columns
    if data[0]==data[3]==data[6] or data[1]==data[4]==data[7] or data[2]==data[5]==data[8]:
        return True

    # to check diagonals
    if data[0]==data[4]==data[8] or data[2]==data[4]==data[6]:
        return True
    
    return False

def updateBoard(place,turn):
    data[place] = turn
    board()

def getValidNumber(turn):
    try:
        inputText = "Enter the place to put "+turn+" :- "
        number=int(input(inputText))
        if 0<number<=9:
            return number
        else:
            print("Value is out of range. It should be between 1 and 9")
    except ValueError:
        print("Invalid value add value between 1 to 9 :- ")


def startGame():
    turn = "X"
    global spaceLeft

    # to give randomness to turns

    if random.randint(0,1):
        turn = "O"
    else:
        turn = "X"

    board()

    while not gameOver() and spaceLeft > 0:
        place= getValidNumber(turn)

        if not place:
            continue

        if data[place-1] not in ["X","O"]:
            updateBoard(place-1,turn)
            if turn == "X":
                turn = "O"
            else:
                turn = "X"

            spaceLeft -= 1
        else:
            print("Error:- Position is already occupied by ",data[place-1])

        print(spaceLeft,turn)

    if turn == "X":
        turn = "O"
    else:
        turn = "X"

    if gameOver():
        print ("WINNER IS ",turn,"!!")
    else:
        print ("DRAW!!")
        

startGame()
