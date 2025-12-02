from cmu_graphics import *
import numpy as np
import time
import math
import json
import promptlib
import tkinter as tk
from tkinter import filedialog

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

fieldWidth = Rect(740,980,200,75,border="black",fill=None,visible = False)
fieldXText = Label("Field X",fieldWidth.centerX,fieldWidth.centerY-60,size=30,font="Archivo",visible = False)
fieldWidthText = Label("",fieldWidth.centerX,fieldWidth.centerY,size=45,font="Archivo",visible = False)
fieldWidth.selected = False
fieldHeight = Rect(960,980,200,75,border="black",fill=None,visible = False)
fieldYText = Label("Field Y",fieldHeight.centerX,fieldHeight.centerY-60,size=30,font="Archivo",visible = False)
fieldHeightText = Label("",fieldHeight.centerX,fieldHeight.centerY,size=45,font="Archivo",visible = False)
fieldHeight.selected = False

createBoardSelected = np.array(([],[]),ndmin=2)
playBoardArray = np.array(([],[]),ndmin=2)
playBoardSelected = np.array(([],[]),ndmin=2)


createBoard = Group()
createBoard.visible = False
createBoardNumbersX = Group()
createBoardNumbersX.visible = False
createBoardNumbersY = Group()
createBoardNumbersY.visible = False

playBoard = Group()
playBoard.visible = False
playBoardNumbersX = Group()
playBoardNumbersX.visible = False
playBoardNumbersY = Group()
playBoardNumbersY.visible = False
winCelebration = Label("Nonogram Solved!",300,540,size=50,font="Archivo",fill="green",visible = False)
wrongThing = Label("Thats wrong!",300,300,size=50,font="Archivo",fill="Red",visible=False)
playTutorial1 = Label("Press J to select a JSON file",1720,500,visible=False,size=40)
playTutorial2 = Label("Press the squares to fill in",1680,540,visible=False,size=40)

info = Group(
    Label("Nonogram is a puzzle that uses a grid and numbers on the edges to reveals a hidden image,",940,200,size=30),
    Label("created by Non Ishida and James Dalgety.",940,250,size=30),
    Label("HOW TO PLAY",940,300,size=40),
    Label("To start a game, press the letter J on the play screen. This will allow you to open up",940,350,size=30),
    Label("a Nonogram JSON. When opened, you will see a grid with numbers along the left and top edge.",940,400,size=30),
    Label("Those numbers explains the length of a unbroken cell, with atleast one spacing between cells.",940,450,size=30),
    Label("For example, if you have a row with numbers 2, 3, 8, you can expect there to be a sequence", 940,500,size=30),
    Label("in that row that looks like 2 unbroken cells on the left, 3 unbroken cells after the 2,",940,550,size=30),
    Label("and a long 8 cells around the right.",940,600,size=30),
    Label("HOW TO CREATE",940,650,size=40),
    Label("To create, open up the create tab. On the bottom allows you to determine the size of the",940,700,size=30),
    Label("grid. Press on it, type a number from 1-20 for either, and press G to generate the nonogram.",940,750,size=30),
    Label("Press the grid to draw your image. It will create a black cell. Press on it again to make",940,800,size=30),
    Label("it red. A red cell is a empty cell, however persists into gameplay, telling the player that",940,850,size=30),
    Label("it's an empty cell. This can prevent the player from solving the nonogram incorrectly.",940,900,size=30)
)

greyOut = Rect(0,0,1920,1080,fill="white",opacity=80,visible = False)
backgroundGUI = Rect(360,180,1200,720,fill="white",border="black",borderWidth=7,visible = False)
xMark = Label("X",1510,230,size=50,visible = False)
titlePlayGUI = Label("Play Mode Settings",1920/2,230,size=40,visible = False)
checkmarkAutofill = Rect(400,320,100,100,fill="white",border="black",borderWidth=3,visible = False)
settingAutofill = Label("Autofill Lane",600,370,size=30,visible = False)
checkmarkCorrection = Rect(400,440,100,100,fill="white",border="black",borderWidth=3,visible = False)
settingCorrection = Label("Correction",600,490,size=30,visible = False)
autofill = False
correction = False

titleCreateGUI = Label("Create Mode Settings",1920/2,230,size=40,visible = False)
#checkmarkAutofill = Rect(400,320,100,100,fill="white",border="black",borderWidth=3)
#settingAutofill = Label("Autofill Lane",600,370,size=30)
#checkmarkCorrection = Rect(400,440,100,100,fill="white",border="black",borderWidth=3)
#settingCorrection = Label("Correction",600,490,size=30)

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
            tempGroup.add(Rect(100+(o*50),100+(i*50),50,50,fill=None,border="grey"))
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
    #print(createBoardSelected)

def playCreateBoard():
    global playBoardArray
    global playBoardSelected
    playBoard.clear()
    playBoardNumbersY.clear()
    playBoardNumbersX.clear()
    winCelebration.visible = False
    try:
        fileBoard = prompter.file()
        fileBoard = open(fileBoard)
        jsonBoard = json.load(fileBoard)
    except:
        print("Failure to open file")
        return
    playBoardW = jsonBoard["boardData"][0]["boardW"]
    playBoardH = jsonBoard["boardData"][1]["boardH"]
    playBoardArray = np.array(jsonBoard["boardArray"])
    for i in range(playBoardH):
        tempGroup = Group()
        tempArray = np.array([],ndmin=1)
        for o in range(playBoardW):
            #print(i,o,playBoardW,playBoardH)
            if playBoardArray[i,o] == 2:
                tempArray = np.append(tempArray,[2])
            else:
                tempArray = np.append(tempArray,[0])
            if playBoardArray[i,o] == 2:
                tempGroup.add(Rect(100+(o*50),100+(i*50),50,50,fill="red",border="grey"))
            else:
                #print(playBoardArray[i,o])
                tempGroup.add(Rect(100+(o*50),100+(i*50),50,50,fill=None,border="grey"))
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

def showPlayConfig():
    greyOut.visible = True
    backgroundGUI.visible = True
    titlePlayGUI.visible = True
    checkmarkAutofill.visible = True
    checkmarkCorrection.visible = True
    settingAutofill.visible = True
    settingCorrection.visible = True
    xMark.visible = True

def showCreateConfig():
    greyOut.visible = True
    backgroundGUI.visible = True
    titleCreateGUI.visible = True
    xMark.visible = True

def hideConfigs():
    greyOut.visible = False
    backgroundGUI.visible = False
    titlePlayGUI.visible = False
    titleCreateGUI.visible = False
    checkmarkAutofill.visible = False
    checkmarkCorrection.visible = False
    settingAutofill.visible = False
    settingCorrection.visible = False
    xMark.visible = False

def showInfo():
    info.visible = True

def hideInfo():
    info.visible = False

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
    playTutorial1.visible = True
    playTutorial2.visible = True

def hidePlay():
    playTutorial1.visible = False
    playTutorial2.visible = False
    playBoard.visible = False
    winCelebration.visible = False
    playBoardNumbersX.visible = False
    playBoardNumbersY.visible = False

def onMouseDrag(mX,mY,button):
    if createBoard.visible:
        print(1)
        if createBoard.contains(mX,mY):
            print(2)
            rN = -1
            tN = -1
            for r in createBoard:
                rN +=1
                tN = -1
                for t in r:
                    tN += 1
                    if t.contains(mX,mY):
                        print(3)
                        if button == [0]:
                            t.fill="black"
                            createBoardSelected[rN,tN] = 1
                            #print(createBoardSelected)
                        elif button == [2]:
                            t.fill="red"
                            createBoardSelected[rN,tN] = 2
                            #print(createBoardSelected)
                        elif button == [1]:
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
                        if correction:
                                if playBoardArray[rN,tN] == 2: # Won't reprimand player by pressing red cells this way
                                    return
                                elif button == 0 and not playBoardArray[rN,tN] == 1:
                                    print("Wrong")
                                    wrongThing.visible = True
                                    return
                                elif button == 2 and not playBoardArray[rN,tN] == 0:
                                    print("Wrong")
                                    wrongThing.visible = True
                                    return
                        if button == [0]:
                            if t.fill == None or t.fill == "blue":
                                t.fill = "black"
                                playBoardSelected[rN,tN] = 1
                            #elif t.fill == "blue":
                            #    t.fill = None
                            #    playBoardSelected[rN,tN] = 0
                        if button == [1]:
                            if t.fill == "black" or t.fill == "blue":
                                t.fill = None
                                playBoardSelected[rN,tN] = 0
                        if button == [2]:
                            if t.fill == "black" or t.fill == None:
                                t.fill = "blue"
                        if autofill:
                            if np.array_equal(playBoardSelected[:, tN],playBoardArray[:, tN]): # This is ugly code. Sorry
                                #print(len(playBoardArray[:,0]))
                                countauto = -1
                                countvert = -1
                                preventions = 0
                                for k in playBoard:
                                    countvert += 1
                                    for l in k:
                                        if preventions == countvert:
                                            countauto += 1
                                        #print(tN,countauto,preventions,countvert)
                                        if tN == countauto and preventions == countvert:
                                            preventions += 1
                                            countauto = -1
                                            if l.fill == None:
                                                l.fill = "blue"
                            if np.array_equal(playBoardSelected[rN],playBoardArray[rN]):
                                countvert2 = -1
                                for c in playBoard:
                                    countvert2 += 1
                                    if countvert2 == rN:
                                        for v in c:
                                            if v.fill == None:
                                                v.fill = "blue"

            if np.array_equal(playBoardArray,playBoardSelected):
                #print("ya win buster!")
                winCelebration.visible = True
    


def onMousePress(mX,mY,button):
    global autofill
    global correction
    if xMark.contains(mX,mY):
        hideConfigs()
    elif titleCreateGUI.visible:
        print()
    elif titlePlayGUI.visible:
        if checkmarkAutofill.contains(mX,mY):
            autofill = not autofill
            if autofill:
                checkmarkAutofill.fill = "red"
            else:
                checkmarkAutofill.fill = "white"
        if checkmarkCorrection.contains(mX,mY):
            correction = not correction
            if correction:
                checkmarkCorrection.fill = "red"
            else:
                checkmarkCorrection.fill = "white"
    elif buttonCreate.contains(mX,mY):
        showCreate()
        hidePlay()
        hideInfo()
    elif buttonInfo.contains(mX,mY):
        hideCreate()
        hidePlay()
        showInfo()
    elif buttonPlay.contains(mX,mY):
        hideCreate()
        showPlay()
        hideInfo()
    if createBoard.visible:
        if not greyOut.visible:
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
                                #print(createBoardSelected)
                            elif createBoardSelected[rN,tN] == 1:
                                t.fill="red"
                                createBoardSelected[rN,tN] = 2
                                #print(createBoardSelected)
                            elif createBoardSelected[rN,tN] == 2:
                                t.fill = None
                                createBoardSelected[rN,tN] = 0

                updateText()
    if playBoard.visible:
        if not greyOut.visible:
            if playBoard.contains(mX,mY):
                rN = -1
                tN = -1
                for r in playBoard:
                    rN +=1
                    tN = -1
                    for t in r:
                        tN += 1
                        if t.contains(mX,mY):
                            if correction:
                                if playBoardArray[rN,tN] == 2: # Won't reprimand player by pressing red cells this way
                                    return
                                elif button == 0 and not playBoardArray[rN,tN] == 1:
                                    print("Wrong")
                                    wrongThing.visible = True
                                    return
                                elif button == 2 and not playBoardArray[rN,tN] == 0:
                                    print("Wrong")
                                    wrongThing.visible = True
                                    return
                            if button == 2:
                                if t.fill == None or t.fill == "black":
                                    t.fill = "blue"
                                    playBoardSelected[rN,tN] = 0
                                elif t.fill == "blue":
                                    t.fill = None
                                    playBoardSelected[rN,tN] = 0
                                wrongThing.visible = False
                            elif button == 0:
                                if t.fill == None or t.fill == "blue":
                                    t.fill="black"
                                    playBoardSelected[rN,tN] = 1
                                elif t.fill == "black":
                                    t.fill = None
                                    playBoardSelected[rN,tN] = 0
                                wrongThing.visible = False # I'm writing YanDev code here at this point
                            if autofill:
                                if np.array_equal(playBoardSelected[:, tN],playBoardArray[:, tN]): # This is ugly code. Sorry
                                    #print(len(playBoardArray[:,0]))
                                    countauto = -1
                                    countvert = -1
                                    preventions = 0
                                    for k in playBoard:
                                        countvert += 1
                                        for l in k:
                                            if preventions == countvert:
                                                countauto += 1
                                            #print(tN,countauto,preventions,countvert)
                                            if tN == countauto and preventions == countvert:
                                                preventions += 1
                                                countauto = -1
                                                if l.fill == None:
                                                    l.fill = "blue"
                                if np.array_equal(playBoardSelected[rN],playBoardArray[rN]):
                                    countvert2 = -1
                                    for c in playBoard:
                                        countvert2 += 1
                                        if countvert2 == rN:
                                            for v in c:
                                                if v.fill == None:
                                                    v.fill = "blue"
                print(playBoardSelected)
                if np.array_equal(playBoardArray,playBoardSelected):
                    #print("ya win buster!")
                    winCelebration.visible = True


def createExportBoard():
    createBoardJson = {
        "boardData": [
            {"boardW": createSizeX},
            {"boardH": createSizeY}
        ],
        "boardArray": createBoardSelected.tolist()
    }
    #print(json.dumps(createBoardJson))
    directory = filedialog.asksaveasfilename(defaultextension=".json")
    with open(directory,"w") as f:
        #print(directory)
        json.dump(createBoardJson,f,indent=4)

def onKeyPress(key):
    global createSizeX
    global createSizeY
    if playBoard.visible:
        if key == "c":
            showPlayConfig()
        if key == "j":
            playCreateBoard()
        if key == "up":
            playBoard.centerY -= 10
            playBoardNumbersX.centerY -= 10
            playBoardNumbersY.centerY -= 10
        if key == "down":
            playBoard.centerY += 10
            playBoardNumbersX.centerY += 10
            playBoardNumbersY.centerY += 10
        if key == "left":
            playBoard.centerX -= 10
            playBoardNumbersX.centerX -= 10
            playBoardNumbersY.centerX -= 10
        if key == "right":
            playBoard.centerX += 10
            playBoardNumbersX.centerX += 10
            playBoardNumbersY.centerX += 10
    if createBoard.visible:
        if key == "c":
            showCreateConfig()
        if key == "g":
            createCreateBoard()
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