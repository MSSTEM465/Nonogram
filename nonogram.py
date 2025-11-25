from cmu_graphics import *
import numpy as np
import time
import json
import promptlib

prompter = promptlib.Files()

# Header
whiteHider = Rect(0,0,1920,115,fill="white")
buttonPlay = Rect(20,20,200,75,border="black",fill=None)
buttonCreate = Rect(240,20,200,75,border="black",fill=None)
buttonSolver = Rect(460,20,200,75,border="black",fill=None)
buttonInfo = Rect(1700,20,200,75,border="black",fill=None)
Label("Create",buttonCreate.centerX,buttonCreate.centerY,size=45,align="center",font="Archivo")
Label("Solver",buttonSolver.centerX,buttonSolver.centerY,size=45,align="center",font="Archivo")
Label("Play",buttonPlay.centerX,buttonPlay.centerY,size=45,align="center",font="Archivo")
Label("Info",buttonInfo.centerX,buttonInfo.centerY,size=45,align="center",font="Archivo")
app.width = 1920
app.height = 1080

playSizeX = 0
playSizeY = 0
createSizeX = 0
createSizeY = 0

fieldWidth = Rect(740,980,200,75,border="black",fill=None)
fieldXText = Label("Field X",fieldWidth.centerX,fieldWidth.centerY-60,size=30,font="Archivo")
fieldWidthText = Label("",fieldWidth.centerX,fieldWidth.centerY,size=45,font="Archivo")
fieldWidth.selected = False
fieldHeight = Rect(960,980,200,75,border="black",fill=None)
fieldYText = Label("Field Y",fieldHeight.centerX,fieldHeight.centerY-60,size=30,font="Archivo")
fieldHeightText = Label("",fieldHeight.centerX,fieldHeight.centerY,size=45,font="Archivo")
fieldHeight.selected = False

createBoardSelected = np.array(([],[]),ndmin=2)
playBoardArray = np.array(([],[]),ndmin=2)
playBoardSelected = np.array(([],[]),ndmin=2)

createBoard = Group()
createBoardNumbersX = Group()
createBoardNumbersY = Group()

playBoard = Group()
playBoardNumbersX = Group()
playBoardNumbersY = Group()
winCelebration = Label("Nonogram Solved!",300,540,size=50,font="Archivo",fill="green",visible = False)

def createCreateBoard():
    global createBoardSelected
    createBoard.clear()
    createBoardNumbersY.clear()
    createBoardNumbersX.clear()
    for i in range(createSizeY):
        tempGroup = Group()
        tempArray = np.array([],ndmin=1)
        for o in range(createSizeX):
            tempArray = np.append(tempArray,[0])
            tempGroup.add(Rect(100+(o*50),100+(i*50),50,50,fill=None,border="black"))
            if i == 0:
                createBoardNumbersX.add(Label("0",50+(o*50),100,align="bottom",font="Archivo",size=25,rotateAngle=90)) # God forbid supporting \n! Guess I must force users to tilt their heads
        try:
            createBoardSelected = np.vstack((createBoardSelected, tempArray))
        except:
            createBoardSelected = tempArray
        createBoard.add(tempGroup)
        createBoardNumbersY.add(Label("0",95,150+(i*50),align="right",font="Archivo",size=25))
    createBoard.toBack()
    createBoardNumbersX.toBack()
    createBoardNumbersY.toBack()
    createBoard.centerX = 960
    createBoard.centerY = 450
    createBoardNumbersX.bottom = createBoard.top - 5
    createBoardNumbersX.centerX = createBoard.centerX
    createBoardNumbersY.right = createBoard.left - 1
    createBoardNumbersY.centerY = createBoard.centerY
    #createBoardNumbers.bottomY = createBoard.topY
    print(createBoardSelected)

def playCreateBoard():
    global playBoardArray
    global playBoardSelected
    fileBoard = prompter.file()
    fileBoard = open(fileBoard)
    jsonBoard = json.load(fileBoard)
    playBoardW = jsonBoard["boardData"][0]["boardW"]
    playBoardH = jsonBoard["boardData"][0]["boardW"]
    playBoardArray = np.array(jsonBoard["boardArray"])
    for i in range(playBoardH):
        tempGroup = Group()
        tempArray = np.array([],ndmin=1)
        for o in range(playBoardW):
            if playBoardArray[i,o] == 2:
                tempArray = np.append(tempArray,[2])
            else:
                tempArray = np.append(tempArray,[0])
            if playBoardArray[i,o] == 2:
                tempGroup.add(Rect(100+(o*50),100+(i*50),50,50,fill="red",border="black"))
            else:
                print(playBoardArray[i,o])
                tempGroup.add(Rect(100+(o*50),100+(i*50),50,50,fill=None,border="black"))
            if i == 0:
                playBoardNumbersX.add(Label("0",50+(o*50),100,align="bottom",font="Archivo",size=25,rotateAngle=90)) # God forbid supporting \n! Guess I must force users to tilt their heads
        try:
            playBoardSelected = np.vstack((playBoardSelected, tempArray))
        except:
            playBoardSelected = tempArray
        playBoard.add(tempGroup)
        playBoardNumbersY.add(Label("0",95,150+(i*50),align="right",font="Archivo",size=25))
    playBoard.toBack()
    playBoardNumbersX.toBack()
    playBoardNumbersY.toBack()
    playBoard.centerX = 960
    playBoard.centerY = 450
    playBoardNumbersX.bottom = playBoard.top - 5
    playBoardNumbersX.centerX = playBoard.centerX
    playBoardNumbersY.right = playBoard.left - 1
    playBoardNumbersY.centerY = playBoard.centerY
    playUpdateText()

def playUpdateText():
    iN = -1
    for i in playBoardNumbersY:
        fN = -1
        iN +=1
        counter = 0
        finalStr = ""
        #print(playBoardArray)
        for f in playBoardArray[iN]:
            #print(f)
            fN += 1
            if f == 1:
                counter += 1
                #print(f,counter,"1L")
                if fN == len(playBoardArray[iN])-1:
                    if counter >= 1:
                        if finalStr == "":
                            finalStr = str(counter)
                        else:
                            finalStr = finalStr + ", " + str(counter)
                        counter = 0
            else:
                if counter >= 1:
                    #print(counter,"3K")
                    if finalStr == "":
                        finalStr = str(counter)
                    else:
                        finalStr = finalStr + ", " + str(counter)
                    counter = 0
        if finalStr == "":
            i.value = "0"
        else:
            i.value = finalStr
        i.right = playBoard.left - 5
    iN = -1
    for i in playBoardNumbersX:
        fN = -1
        iN += 1
        counter = 0
        finalStr = ""
        for f in playBoardArray[:, iN]:
            #print(f)
            fN += 1
            if f == 1:
                counter += 1
                #print(f,counter,"1L")
                if fN == len(playBoardArray)-1:
                    if counter >= 1:
                        if finalStr == "":
                            finalStr = str(counter)
                        else:
                            finalStr = finalStr + ", " + str(counter)
                        counter = 0
            else:
                if counter >= 1:
                    #print(counter,"3K")
                    if finalStr == "":
                        finalStr = str(counter)
                    else:
                        finalStr = finalStr + ", " + str(counter)
                    counter = 0
        if finalStr == "":
            i.value = "0"
        else:
            i.value = finalStr
        i.bottom = playBoard.top - 5


def updateText():
    iN = -1
    for i in createBoardNumbersY:
        fN = -1
        iN +=1
        counter = 0
        finalStr = ""
        for f in createBoardSelected[iN]:
            #print(f)
            fN += 1
            if f == 1:
                counter += 1
                #print(f,counter,"1L")
                if fN == len(createBoardSelected[iN])-1:
                    if counter >= 1:
                        if finalStr == "":
                            finalStr = str(counter)
                        else:
                            finalStr = finalStr + ", " + str(counter)
                        counter = 0
            else:
                if counter >= 1:
                    #print(counter,"3K")
                    if finalStr == "":
                        finalStr = str(counter)
                    else:
                        finalStr = finalStr + ", " + str(counter)
                    counter = 0
        if finalStr == "":
            i.value = "0"
        else:
            i.value = finalStr
        i.right = createBoard.left - 5
    iN = -1
    for i in createBoardNumbersX:
        fN = -1
        iN += 1
        counter = 0
        finalStr = ""
        for f in createBoardSelected[:, iN]:
            #print(f)
            fN += 1
            if f == 1:
                counter += 1
                #print(f,counter,"1L")
                if fN == len(createBoardSelected)-1:
                    if counter >= 1:
                        if finalStr == "":
                            finalStr = str(counter)
                        else:
                            finalStr = finalStr + ", " + str(counter)
                        counter = 0
            else:
                if counter >= 1:
                    #print(counter,"3K")
                    if finalStr == "":
                        finalStr = str(counter)
                    else:
                        finalStr = finalStr + ", " + str(counter)
                    counter = 0
        if finalStr == "":
            i.value = "0"
        else:
            i.value = finalStr
        i.bottom = createBoard.top - 5
def hideCreate():
    createBoard.visible = False
    fieldHeight.visible = False
    fieldWidth.visible = False
    fieldXText.visible = False
    fieldYText.visible = False
    fieldHeightText.visible = False
    fieldWidthText.visible = False
    createBoardNumbersX.visible = False
    createBoardNumbersY.visible = False

def showCreate():
    createBoard.visible = True
    fieldHeight.visible = True
    fieldWidth.visible = True
    fieldXText.visible = True
    fieldYText.visible = True
    fieldHeightText.visible = True
    fieldWidthText.visible = True
    createBoardNumbersX.visible = True
    createBoardNumbersY.visible = True

def showPlay():
    playBoard.visible = True
    playBoardNumbersX.visible = True
    playBoardNumbersY.visible = True

def hidePlay():
    playBoard.visible = False
    playBoardNumbersX.visible = False
    playBoardNumbersY.visible = False

def onMousePress(mX,mY):
    if buttonCreate.contains(mX,mY):
        showCreate()
    elif buttonInfo.contains(mX,mY):
        hideCreate()
    if createBoard.visible:
        if fieldWidth.contains(mX,mY) and not fieldWidth.selected and not fieldHeight.selected:
            fieldWidth.selected = True
            fieldWidth.fill = rgb(255,200,255)
        elif fieldHeight.contains(mX,mY) and not fieldWidth.selected and not fieldHeight.selected:
            fieldHeight.selected = True
            fieldHeight.fill = rgb(255,200,255)
        elif createBoard.contains(mX,mY):
            rN = -1
            tN = -1
            for r in createBoard:
                rN +=1
                tN = -1
                for t in r:
                    tN += 1
                    if t.contains(mX,mY):
                        if createBoardSelected[rN,tN] == 0:
                            t.fill="black"
                            createBoardSelected[rN,tN] = 1
                            print(createBoardSelected)
                        elif createBoardSelected[rN,tN] == 1:
                            t.fill="red"
                            createBoardSelected[rN,tN] = 2
                            print(createBoardSelected)
                        elif createBoardSelected[rN,tN] == 2:
                            t.fill = None
                            createBoardSelected[rN,tN] = 0

            updateText()
    if playBoard.visible:
        if playBoard.contains(mX,mY):
            rN = -1
            tN = -1
            for r in playBoard:
                rN +=1
                tN = -1
                for t in r:
                    tN += 1
                    if t.contains(mX,mY):
                        if playBoardSelected[rN,tN] == 0:
                            t.fill="black"
                            playBoardSelected[rN,tN] = 1
                            #print(createBoardSelected)
                        elif playBoardSelected[rN,tN] == 1:
                            t.fill = None
                            playBoardSelected[rN,tN] = 0
            if np.array_equal(playBoardArray,playBoardSelected):
                print("ya win buster!")
                winCelebration.visible = True


def createExportBoard():
    createBoardJson = {
        "boardData": [
            {"boardW": createSizeX},
            {"boardH": createSizeY}
        ],
        "boardArray": createBoardSelected.tolist()
    }
    print(json.dumps(createBoardJson))
    directory = prompter.dir()
    with open(directory + "\\nonogramJson.json","w") as f:
        print(directory)
        json.dump(createBoardJson,f,indent=4)

def onKeyPress(key):
    global createSizeX
    global createSizeY
    if createBoard.visible:
        if key == "g":
            createCreateBoard()
        if key == "j":
            playCreateBoard()
        if key == "e":
            createExportBoard()
        if key == "up":
            createBoard.centerY -= 10
            createBoardNumbersX.centerY -= 10
            createBoardNumbersY.centerY -= 10
        if key == "down":
            createBoard.centerY += 10
            createBoardNumbersX.centerY += 10
            createBoardNumbersY.centerY += 10
        if key == "left":
            createBoard.centerX -= 10
            createBoardNumbersX.centerX -= 10
            createBoardNumbersY.centerX -= 10
        if key == "right":
            createBoard.centerX += 10
            createBoardNumbersX.centerX += 10
            createBoardNumbersY.centerX += 10
        if fieldWidth.selected:
            if key.isnumeric():
                if int(fieldWidthText.value + key) <= 20:
                    fieldWidthText.value = fieldWidthText.value + key
            if key == "backspace":
                try:
                    fieldWidthText.value = fieldWidthText.value[:-1]
                except:
                    print("Failure to shorten text")
                    return
            if key == "enter":
                try:
                    createSizeX = int(fieldWidthText.value)
                    fieldWidth.selected = False
                    fieldWidth.fill = "white"
                except:
                    return
        if fieldHeight.selected:
            if key.isnumeric():
                if int(fieldHeightText.value + key) <= 20:
                    fieldHeightText.value = fieldHeightText.value + key
            if key == "backspace":
                try:
                    fieldHeightText.value = fieldHeightText.value[:-1]
                except:
                    print("Failure to shorten text")
                    return
            if key == "enter":
                try:
                    createSizeY = int(fieldHeightText.value)
                    fieldHeight.selected = False
                    fieldHeight.fill = "white"
                except:
                    return



cmu_graphics.run()