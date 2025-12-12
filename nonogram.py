from cmu_graphics import *
import numpy as np
import json
import promptlib
import tkinter as tk
from tkinter import filedialog
import nonogramsolver as ns


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
solverSizeX = 0
solverSizeY = 0
solverSolverSizeX = 0
solverSolverSizeY = 0

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
solverJSONArray = np.array(([],[]),ndmin=2)
solverSolverArray = np.array(([],[]),ndmin=2)

solverY = []
solverX = []

createBoard = Group()
createBoard.visible = False
createBoardNumbersX = Group()
createBoardNumbersX.visible = False
createBoardNumbersY = Group()
createBoardNumbersY.visible = False
createTutorial = Image("data/CreateKeybinds.png",1400,50,visible = False)
createTutorial.width = 500
createTutorial.height = 500

testingList = []

solverBoard = Group()
solverBoard.visible = False
solverPrereq = Group()
solverPrereq.visible = False
solverPrereqLabels = Group()
solverPrereqLabels.visible = False
solverBoardNumbersX = Group()
solverBoardNumbersX.visible = False
solverBoardNumbersY = Group()
solverBoardNumbersY.visible = False
solverFieldWidth = Rect(740,980,200,75,border="black",fill=None,visible = False)
solverFieldXText = Label("Field X",fieldWidth.centerX,fieldWidth.centerY-60,size=30,font="Archivo",visible = False)
solverFieldWidthText = Label("",fieldWidth.centerX,fieldWidth.centerY,size=45,font="Archivo",visible = False)
solverFieldWidth.selected = False
solverFieldHeight = Rect(960,980,200,75,border="black",fill=None,visible = False)
solverFieldYText = Label("Field Y",fieldHeight.centerX,fieldHeight.centerY-60,size=30,font="Archivo",visible = False)
solverFieldHeightText = Label("",fieldHeight.centerX,fieldHeight.centerY,size=45,font="Archivo",visible = False)
solverFieldHeight.selected = False
solverKnownFillField = Rect(500,500,200,100,border="black",fill=None,visible=False)
solverKnownFillField.selected = False
solverKnownFillText = Label(";",solverKnownFillField.centerX,solverKnownFillField.centerY,size=30,font="Archivo",visible = False)

playBoard = Group()
playBoard.visible = False
playBoardNumbersX = Group()
playBoardNumbersX.visible = False
playBoardNumbersY = Group()
playBoardNumbersY.visible = False
winCelebration = Label("Nonogram Solved!",300,540,size=50,font="Archivo",fill="green",visible = False)
wrongThing = Label("Thats wrong!",300,300,size=50,font="Archivo",fill="Red",visible=False)
playTutorial = Image("data/PlayKeybinds.png",1600,200,visible=False)
playTutorial.width = playTutorial.width * 0.55
playTutorial.height = playTutorial.height * 0.55
playTutorialMouse = Image('data/Mouse Play.png',1400,200,visible=False)

info = Image("data/info.png",0,115)

greyOut = Rect(0,0,1920,1080,fill="white",opacity=80,visible = False)
backgroundGUI = Rect(360,180,1200,720,fill="white",border="black",borderWidth=7,visible = False)
xMark = Label("X",1510,230,size=50,visible = False)
titlePlayGUI = Label("Play Mode Settings",1920/2,230,size=40,visible = False)
checkmarkAutofill = Rect(400,320,100,100,fill="white",border="black",borderWidth=3,visible = False)
settingAutofill = Label("Autofill Lane",600,370,size=30,visible = False)
checkmarkCorrection = Rect(400,440,100,100,fill="white",border="black",borderWidth=3,visible = False)
settingCorrection = Label("Correction",600,490,size=30,visible = False)
checkmarkPenalize = Rect(400,560,100,100,fill="white",border="grey",visible=False,borderWidth=3)
settingPenalize = Label("Penalize when Wrong",660,610,size=30,visible = False)
lastEntered = [-1,-1]
autofill = False
correction = False
penalize = False
lives = 5

titleCreateGUI = Label("Create Mode Settings",1920/2,230,size=40,visible = False)
#checkmarkAutofill = Rect(400,320,100,100,fill="white",border="black",borderWidth=3)
#settingAutofill = Label("Autofill Lane",600,370,size=30)
#checkmarkCorrection = Rect(400,440,100,100,fill="white",border="black",borderWidth=3)
#settingCorrection = Label("Correction",600,490,size=30)\

whiteOutTut = Rect(0,0,1920,1080,fill='white',opacity=90,visible=False)
speechBubble = Polygon(100,100, 150,150, 700,150, 700,400, 150,400, 150,200,fill="white",border="black",visible=False)
speechBubble.tutCurrent = False
speechText = Label("Welcome to my Nonogram program!",speechBubble.centerX,speechBubble.centerY+20,size=40,font="Archivo",visible=False)
speechText.count = 0
speechNext = Polygon(0,0, 20,0, 10,20, fill="white",border="black",visible = False)
dialogue = ["Welcome to Nonograms!", "Nonogram is a puzzle game about uncovering a black and white image.","You are given a grid, and numbers for the rows and columns.","If you can't tell, the numbers will help you solve the grid.","The numbers next to the row/column explains the length","of runs or unbroken cells in that lane. We represent those with", "the color black. You can color cells with black with left click.","Right click will fill it blue, which will mean you think its empty.","Sometimes, you might encounter a red cell. That means it is set","as empty from the artist of the nonogram.","The best way of learning nonograms is practice!","Lets place you into a simple board of a nonogram.", "On this board, we can solve by applying what we know,","then filling in what was satisified, Then, we continue","finding places that we can solve.","Look at the top row, you see how it says (1,1,1)?","This must mean that the lane must have one cell,","atleast one empty slot, one cell, empty, cell.","Wait a moment, that pattern! Fill, empty, fill, empty, fill,","at the very minimum, the length of the lane will be 5,", "which is the same length as our lane!","We can fill in the lane with this pattern.","Try solving the rest of the puzzle!","Congrats! You solved your first nonogram.","From here on out, you can access all facutilies of the app.", "Have fun!"]



def adjustSpeechBubbleSize():
    speechText.left = speechBubble.x2 + 20
    speechBubble.x3 = speechText.right + 20
    speechBubble.x4 = speechText.right + 20
    speechNext.right = speechBubble.right - 20
    speechNext.bottom = speechBubble.bottom - 20

def initalizeTutorial():
    whiteOutTut.visible = True
    speechBubble.visible = True
    speechText.visible = True
    speechBubble.tutCurrent = True
    speechNext.visible = True
    info.visible = False
    speechText.value = "Welcome to Nonograms!"
    adjustSpeechBubbleSize()

def checkFirstTimeLaunch():
    try:
        f = open("hasPlayed.txt")
        return False
    except:
        f = open("hasPlayed.txt","x")
        return True

if checkFirstTimeLaunch():
    initalizeTutorial()

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

treeJSON = """{
    "boardData": [
        {
            "boardW": 5
        },
        {
            "boardH": 5
        }
    ],
    "boardArray": [
        [
            1.0,
            0.0,
            1.0,
            0.0,
            1.0
        ],
        [
            0.0,
            1.0,
            0.0,
            1.0,
            0.0
        ],
        [
            0.0,
            0.0,
            1.0,
            0.0,
            0.0
        ],
        [
            0.0,
            0.0,
            1.0,
            0.0,
            0.0
        ],
        [
            0.0,
            0.0,
            1.0,
            0.0,
            0.0
        ]
    ]
}"""

def tutorialCreateBoard(): # Uses play board
    global playBoardArray
    global playBoardSelected
    global lives
    global lastEntered
    playBoard.clear()
    playBoardNumbersY.clear()
    playBoardNumbersX.clear()
    winCelebration.visible = False
    lives = 5
    lastEntered = [-1,-1]
    playBoardSelected = np.array(([],[]),ndmin=2)
    jsonBoard = json.loads(treeJSON)
    playBoardW = 5
    playBoardH = 5
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
    playBoard.centerY = 700
    playBoardNumbersX.bottom = playBoard.top - 5
    playBoardNumbersX.centerX = playBoard.centerX
    playBoardNumbersY.right = playBoard.left - 1
    playBoardNumbersY.centerY = playBoard.centerY
    playUpdateText()



def playCreateBoard():
    global playBoardArray
    global playBoardSelected
    global lives
    global lastEntered
    playBoard.clear()
    playBoardNumbersY.clear()
    playBoardNumbersX.clear()
    winCelebration.visible = False
    lives = 5
    lastEntered = [-1,-1]
    playBoardSelected = np.array(([],[]),ndmin=2)
    try:
        fileBoard = prompter.file()
        fileBoard = open(fileBoard)
        jsonBoard = json.load(fileBoard)
        playBoardW = jsonBoard["boardData"][0]["boardW"]
        playBoardH = jsonBoard["boardData"][1]["boardH"]
        playBoardArray = np.array(jsonBoard["boardArray"])
    except:
        print("Failure to open file")
        return
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



def solverJSONUpdateText():
    iN = -1
    for i in solverBoardNumbersY:
        fN = -1
        iN +=1
        counter = 0
        finalStr = ""
        #print(playBoardArray)
        for f in solverJSONArray[iN]:
            #print(f)
            fN += 1
            if f == 1:
                counter += 1
                #print(f,counter,"1L")
                if fN == len(solverJSONArray[iN])-1:
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
        i.right = solverBoard.left - 5
    iN = -1
    for i in solverBoardNumbersX:
        fN = -1
        iN += 1
        counter = 0
        finalStr = ""
        for f in solverJSONArray[:, iN]:
            #print(f)
            fN += 1
            if f == 1:
                counter += 1
                #print(f,counter,"1L")
                if fN == len(solverJSONArray)-1:
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
        i.bottom = solverBoard.top - 5

def solverSolverUpdateText():
    iN = -1
    for i in solverBoardNumbersY:
        fN = -1
        iN +=1
        counter = 0
        finalStr = ""
        #print(playBoardArray)
        for f in solverSolverArray[iN]:
            #print(f)
            fN += 1
            if f == 1:
                counter += 1
                #print(f,counter,"1L")
                if fN == len(solverSolverArray[iN])-1:
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
        i.right = solverBoard.left - 5
    iN = -1
    for i in solverBoardNumbersX:
        fN = -1
        iN += 1
        counter = 0
        finalStr = ""
        for f in solverSolverArray[:, iN]:
            #print(f)
            fN += 1
            if f == 1:
                counter += 1
                #print(f,counter,"1L")
                if fN == len(solverSolverArray)-1:
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
        i.bottom = solverBoard.top - 5

def solverCreateBoardJSON():
    global solverJSONArray
    solverBoard.clear()
    solverBoardNumbersY.clear()
    solverBoardNumbersX.clear()
    solverFieldHeight.visible = False
    solverFieldHeightText.visible = False
    solverFieldWidth.visible = False
    solverFieldWidthText.visible = False
    solverFieldXText.visible = False
    solverFieldYText.visible = False
    try:
        fileBoard = prompter.file()
        fileBoard = open(fileBoard)
        jsonBoard = json.load(fileBoard)
    except:
        print("Failure to open file")
        return
    solverBoardW = jsonBoard["boardData"][0]["boardW"]
    solverBoardH = jsonBoard["boardData"][1]["boardH"]
    solverJSONArray = np.array(jsonBoard["boardArray"])
    for i in range(solverBoardH):
        tempGroup = Group()
        tempArray = np.array([],ndmin=1)
        for o in range(solverBoardW):
            #print(i,o,playBoardW,playBoardH)
            if solverJSONArray[i,o] == 2:
                tempGroup.add(Rect(100+(o*50),100+(i*50),50,50,fill="red",border="grey"))
            elif solverJSONArray[i,o] == 1:
                #print(playBoardArray[i,o])
                tempGroup.add(Rect(100+(o*50),100+(i*50),50,50,fill="black",border="grey"))
            else:
                tempGroup.add(Rect(100+(o*50),100+(i*50),50,50,fill=None,border="grey"))
            if i == 0:
                solverBoardNumbersX.add(Label("0",50+(o*50),100,align="bottom",font="Archivo",size=25,rotateAngle=90))
        solverBoard.add(tempGroup)
        solverBoardNumbersY.add(Label("0",95,150+(i*50),align="right",font="Archivo",size=25))
    solverBoard.toBack()
    solverBoardNumbersX.toBack()
    solverBoardNumbersY.toBack()
    solverBoard.centerX = 960
    solverBoard.centerY = 450
    solverBoardNumbersX.bottom = solverBoard.top - 5
    solverBoardNumbersX.centerX = solverBoard.centerX
    solverBoardNumbersY.right = solverBoard.left - 1
    solverBoardNumbersY.centerY = solverBoard.centerY
    solverJSONUpdateText()
    pass

def solverSolverShowSize():
    solverFieldHeight.visible = True
    solverFieldHeightText.visible = True
    solverFieldWidth.visible = True
    solverFieldWidthText.visible = True
    solverFieldXText.visible = True
    solverFieldYText.visible = True

def solverSolverCreatePrereq():
    global testingList
    solverBoard.clear()
    solverBoardNumbersX.clear()
    solverBoardNumbersY.clear()
    solverPrereq.clear()
    solverPrereqLabels.clear()
    solverKnownFillField.visible = True
    solverKnownFillText.visible = True
    for i in range(solverSolverSizeX):
        solverPrereq.add(Rect(200+(i*210),200,200,100,fill=None,border="red"))
        testingList.append(Label("0",300+(i*210),250,size=30))
    for i in range(solverSolverSizeY):
        solverPrereq.add(Rect(100,330+(i*120),200,100,fill=None,border="blue"))
        testingList.append(Label("0",200,380+(i*120),size=30))
    
def solverGoshThereAreSoManyFunctions(): # Uses what is inputed by user and solves from there
    global solverSolverArray
    tooManyCounters = -1
    solverY = []
    solverX = []
    for j in solverPrereq:
        tooManyCounters += 1
        if j.border == "red":
            solverX.append((testingList[tooManyCounters].value).split(","))
        if j.border == "blue":
            solverY.append((testingList[tooManyCounters].value).split(","))
    for h in range(len(solverX)):
        for j in range(len(solverX[h])):
            solverX[h][j] = int(solverX[h][j])
    for h in range(len(solverY)):
        for j in range(len(solverY[h])):
            solverY[h][j] = int(solverY[h][j])
    solverKnownList = (solverKnownFillText.value).split(";")
    cOu = -1
    for g in solverKnownList:
        cOu += 1
        solverKnownList[cOu] = g.split(",")
    print(solverX,solverY,solverKnownList)
    solverSolverArray = ns.initalize(solverY,solverX,[len(solverX),len(solverY)],solverKnownList)
    solverCreateBoardSolver()
        
def solverCreateBoardSolver():
    global solverSolverArray
    global testingList
    solverPrereq.clear()
    for q in testingList:
        q.visible = False
    testingList = []
    solverBoard.clear()
    solverBoardNumbersY.clear()
    solverBoardNumbersX.clear()
    solverKnownFillText.visible = False
    solverKnownFillField.visible = False
    solverBoardW = len(solverSolverArray[0])
    solverBoardH = len(solverSolverArray[:,0])
    for i in range(solverBoardH):
        tempGroup = Group()
        for o in range(solverBoardW):
            #print(i,o,playBoardW,playBoardH)
            if solverSolverArray[i,o] == 2:
                tempGroup.add(Rect(100+(o*50),100+(i*50),50,50,fill="red",border="grey"))
            elif solverSolverArray[i,o] == 1:
                #print(playBoardArray[i,o])
                tempGroup.add(Rect(100+(o*50),100+(i*50),50,50,fill="black",border="grey"))
            else:
                tempGroup.add(Rect(100+(o*50),100+(i*50),50,50,fill=None,border="grey"))
            if i == 0:
                solverBoardNumbersX.add(Label("0",50+(o*50),100,align="bottom",font="Archivo",size=25,rotateAngle=90))
        solverBoard.add(tempGroup)
        solverBoardNumbersY.add(Label("0",95,150+(i*50),align="right",font="Archivo",size=25))
    solverBoard.toBack()
    solverBoardNumbersX.toBack()
    solverBoardNumbersY.toBack()
    solverBoard.centerX = 960
    solverBoard.centerY = 450
    solverBoardNumbersX.bottom = solverBoard.top - 5
    solverBoardNumbersX.centerX = solverBoard.centerX
    solverBoardNumbersY.right = solverBoard.left - 1
    solverBoardNumbersY.centerY = solverBoard.centerY
    solverSolverUpdateText()
    pass



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
    createTutorial.visible = False

def hideSolver():
    solverBoard.visible = False
    solverPrereq.visible = False
    solverBoardNumbersX.visible = False
    solverBoardNumbersY.visible = False
    solverPrereqLabels.visible = False
    solverFieldHeight.visible = False
    solverFieldHeightText.visible = False
    solverFieldWidth.visible = False
    solverFieldWidthText.visible = False
    solverFieldXText.visible = False
    solverFieldYText.visible = False
    solverKnownFillText.visible = False
    solverKnownFillField.visible = False

def showSolver():
    solverBoard.visible = True
    solverPrereq.visible = True
    solverPrereqLabels.visible = True
    solverBoardNumbersX.visible = True
    solverBoardNumbersY.visible = True

def showPlayConfig():
    greyOut.visible = True
    backgroundGUI.visible = True
    titlePlayGUI.visible = True
    checkmarkAutofill.visible = True
    checkmarkCorrection.visible = True
    settingAutofill.visible = True
    settingCorrection.visible = True
    xMark.visible = True
    checkmarkPenalize.visible = True
    settingPenalize.visible = True

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
    settingPenalize.visible = False
    checkmarkPenalize.visible = False



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
    createTutorial.visible = True

def showPlay():
    playBoard.visible = True
    playBoardNumbersX.visible = True
    playBoardNumbersY.visible = True
    playTutorial.visible = True

def hidePlay():
    playTutorial.visible = False
    playBoard.visible = False
    winCelebration.visible = False
    playBoardNumbersX.visible = False
    playBoardNumbersY.visible = False
    wrongThing.visible = False
    playTutorialMouse.visible = False

def updatePenalizeText():
    if penalize:
        if lives == 0:
            wrongThing.value = "You have failed."
            playBoard.clear()
            playBoardNumbersX.clear()
            playBoardNumbersY.clear()
        else:    
            wrongThing.value = "Lives left: " + str(lives)
    else:
        wrongThing.value = "Thats wrong!"

def onMouseDrag(mX,mY,button):
    global lastEntered
    global lives
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
                                if playBoardArray[rN,tN] == 2 or t.fill == "blue": # Won't reprimand player by pressing red cells this way
                                    return
                                elif button == [0] and not playBoardArray[rN,tN] == 1:
                                    print("Wrong")
                                    wrongThing.visible = True
                                    if penalize:
                                        if not lastEntered == [rN,tN]:
                                            lives -= 1
                                            lastEntered = [rN,tN]
                                            updatePenalizeText()
                                    return
                                elif button == [2] and not playBoardArray[rN,tN] == 0:
                                    print("Wrong")
                                    wrongThing.visible = True
                                    if penalize:
                                        if not lastEntered == [rN,tN]:
                                            lives -= 1
                                            lastEntered = [rN,tN]
                                            updatePenalizeText()
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
                if speechBubble.tutCurrent:
                    speechBubble.visible = True
                    speechNext.visible = True
                    speechText.visible = True
                    whiteOutTut.visible = True
                else:
                    winCelebration.visible = True
        
def onMousePress(mX,mY,button):
    global autofill
    global correction
    global lives
    global lastEntered
    global penalize
    if speechBubble.tutCurrent:
        if speechBubble.contains(mX,mY):
            speechText.count += 1
            if speechText.count == 26:
                speechText.visible = False
                speechBubble.visible = False
                speechNext.visible = False
                whiteOutTut.visible = False
                speechBubble.tutCurrent = False
                playTutorialMouse.visible = False
                playBoard.clear()
                playBoardNumbersX.clear()
                playBoardNumbersY.clear()
                playBoard.visible = False
                playBoardNumbersY.visible = False
                playBoardNumbersX.visible = False
                info.visible = True
                return
            speechText.value = dialogue[speechText.count]
            if speechText.count == 12:
                tutorialCreateBoard()
                whiteOutTut.visible = False
                playBoard.visible = True
                playBoardNumbersX.visible = True
                playBoardNumbersY.visible = True
            if speechText.count == 15:
                countoml = -1
                for i in playBoard:
                    for g in i:
                        countoml += 1
                        if countoml < 5:
                            g.border = "blue"
            if speechText.count == 21:
                countoml = -1
                for i in playBoard:
                    for g in i:
                        countoml += 1
                        if countoml == 0 or countoml == 2 or countoml == 4:
                            g.fill = "black"
                        if countoml == 1 or countoml == 3:
                            g.fill = "blue"
                        g.border = "grey"
                        playBoardSelected[0,0] = 1
                        playBoardSelected[0,2] = 1
                        playBoardSelected[0,4] = 1
            if speechText.count == 23:
                speechText.visible = False
                speechBubble.visible = False
                speechNext.visible = False
                playTutorialMouse.visible = True
            print(speechText.count)
            adjustSpeechBubbleSize()
        if speechText.count == 23:
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
                                        #print("Failure Point 1",playBoardSelected[:, tN],playBoardArray[:, tN])
                                        if np.array_equal(playBoardSelected[:, tN],playBoardArray[:, tN]): # This is ugly code. Sorry
                                            #print("Failure Point 2")
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
                        #print(playBoardSelected)
                        if np.array_equal(playBoardArray,playBoardSelected):
                            speechBubble.visible = True
                            speechNext.visible = True
                            speechText.visible = True
                            whiteOutTut.visible = True
        return
    if xMark.contains(mX,mY):
        hideConfigs()
    elif buttonCreate.contains(mX,mY):
        showCreate()
        hidePlay()
        hideInfo()
        hideSolver()
    elif buttonInfo.contains(mX,mY):
        hideCreate()
        hidePlay()
        showInfo()
        hideSolver()
    elif buttonPlay.contains(mX,mY):
        hideCreate()
        showPlay()
        hideInfo()
        hideSolver()
    elif buttonSolver.contains(mX,mY):
        hideCreate()
        hidePlay()
        hideInfo()
        showSolver()
    elif solverPrereqLabels.visible:
        for h in solverPrereq:
            try:
                for t in solverPrereq:
                    if t.fill == None:
                        pass
                    else:
                        raise
                if h.contains(mX,mY):
                    h.fill = rgb(255,200,255)
            except:
                pass
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
                checkmarkPenalize.border = "black"
            else:
                checkmarkCorrection.fill = "white"
                checkmarkPenalize.border = "grey"
                penalize = False
                checkmarkPenalize.fill = "white"
        if checkmarkPenalize.contains(mX,mY):
            if checkmarkPenalize.border == "black":
                penalize = not penalize
                if penalize:
                    checkmarkPenalize.fill = "red"
                else:
                    checkmarkPenalize.fill = "white"
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
                                if playBoardArray[rN,tN] == 2 or t.fill == "blue": # Won't reprimand player by pressing red cells or over shooting into blue cells
                                    return
                                elif button == 0 and not playBoardArray[rN,tN] == 1:
                                    print("Wrong")
                                    wrongThing.visible = True
                                    if penalize:
                                        if not lastEntered == [rN,tN]:
                                            lives -= 1
                                            lastEntered = [rN,tN]
                                            updatePenalizeText()
                                    return
                                elif button == 2 and not playBoardArray[rN,tN] == 0:
                                    print("Wrong")
                                    wrongThing.visible = True
                                    if penalize:
                                        if not lastEntered == [rN,tN]:
                                            lives -= 1
                                            lastEntered = [rN,tN]
                                            updatePenalizeText()
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
                                #print("Failure Point 1",playBoardSelected[:, tN],playBoardArray[:, tN])
                                if np.array_equal(playBoardSelected[:, tN],playBoardArray[:, tN]): # This is ugly code. Sorry
                                    #print("Failure Point 2")
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
                #print(playBoardSelected)
                if np.array_equal(playBoardArray,playBoardSelected):
                    #print("ya win buster!")
                    winCelebration.visible = True
    if solverBoard.visible:
        if solverFieldWidth.contains(mX,mY) and not solverFieldWidth.selected and not solverFieldHeight.selected:
                solverFieldWidth.selected = True
                solverFieldWidth.fill = rgb(255,200,255)
        elif solverFieldHeight.contains(mX,mY) and not solverFieldWidth.selected and not solverFieldHeight.selected:
            solverFieldHeight.selected = True
            solverFieldHeight.fill = rgb(255,200,255)
        elif solverKnownFillField.contains(mX,mY) and not solverFieldWidth.selected and not solverFieldHeight.selected and not solverKnownFillField.selected:
            solverKnownFillField.selected = True
            solverKnownFillField.fill = rgb(255,200,255)

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
    global solverSolverSizeY
    global solverSolverSizeX
    if solverBoard.visible:
        if key == "up":
            solverBoard.centerY -= 10
            solverBoardNumbersX.centerY -= 10
            solverBoardNumbersY.centerY -= 10
            solverKnownFillField.centerY -= 10
            solverKnownFillText.centerY -= 10
            solverPrereq.centerY -= 10
            for h in testingList: # Slowly I regret substituting the text to be a list instead of a group
                h.centerY -= 10
        if key == "down":
            solverBoard.centerY += 10
            solverBoardNumbersX.centerY += 10
            solverBoardNumbersY.centerY += 10
            solverPrereq.centerY += 10
            solverKnownFillField.centerY += 10
            solverKnownFillText.centerY += 10
            for h in testingList:
                h.centerY += 10
        if key == "left":
            solverBoard.centerX -= 10
            solverBoardNumbersX.centerX -= 10
            solverBoardNumbersY.centerX -= 10
            solverPrereq.centerX -= 10
            solverKnownFillField.centerX -= 10
            solverKnownFillText.centerX -= 10
            for h in testingList:
                h.centerX -= 10
        if key == "right":
            solverBoard.centerX += 10
            solverBoardNumbersX.centerX += 10
            solverBoardNumbersY.centerX += 10
            solverPrereq.centerX += 10
            solverKnownFillField.centerX += 10
            solverKnownFillText.centerX += 10
            for h in testingList:
                h.centerX += 10
        try:
            solverPrereq.fill == None 
            for t in solverPrereq:
                if t.fill == None:
                    pass
                else:
                    raise
            #print("Woah")
        except: # Could be optimized for my newer system. Remind me later
            #print("Hi")
            FREEME = -1
            for u in solverPrereq:
                FREEME += 1
                if u.fill == rgb(255,200,255):
                    #print(u,FREEME)
                    if key.isnumeric():
                        testingList[FREEME].value = testingList[FREEME].value + key
                    if key == ",":
                        testingList[FREEME].value = testingList[FREEME].value + key
                    if key == "backspace":
                        try:
                            testingList[FREEME].value = testingList[FREEME].value[:-1]
                        except:
                            print("Failure to shorten text")
                            return
                    if key == "enter":
                        try:
                            u.fill = None
                        except:
                            return
        if key == "r":
            #print(solverSolverSizeX,solverSolverSizeY)
            solverSolverCreatePrereq()
        if key == "j":
            solverCreateBoardJSON()
        if key == "b":
            solverGoshThereAreSoManyFunctions()
        if key == "g":
            solverSolverShowSize()
        if solverFieldWidth.selected:
            if key.isnumeric():
                if int(solverFieldWidthText.value + key) <= 20:
                    solverFieldWidthText.value = solverFieldWidthText.value + key
            if key == "backspace":
                try:
                    solverFieldWidthText.value = solverFieldWidthText.value[:-1]
                except:
                    print("Failure to shorten text")
                    return
            if key == "enter":
                try:
                    solverSolverSizeX = int(solverFieldWidthText.value)
                    solverFieldWidth.selected = False
                    solverFieldWidth.fill = "white"
                except:
                    return
        if solverFieldHeight.selected:
            if key.isnumeric():
                if int(solverFieldHeightText.value + key) <= 20:
                    solverFieldHeightText.value = solverFieldHeightText.value + key
            if key == "backspace":
                try:
                    solverFieldHeightText.value = solverFieldHeightText.value[:-1]
                except:
                    print("Failure to shorten text")
                    return
            if key == "enter":
                try:
                    solverSolverSizeY = int(solverFieldHeightText.value)
                    solverFieldHeight.selected = False
                    solverFieldHeight.fill = "white"
                except:
                    return
        if solverKnownFillField.selected:
            if key.isnumeric():
                solverKnownFillText.value = solverKnownFillText.value + key
            if key == "backspace":
                try:
                    solverKnownFillText.value = solverKnownFillText.value[:-1]
                except:
                    print("Failure to shorten text")
                    return
            if key == "enter":
                try:
                    solverKnownFillField.selected = False
                    solverKnownFillField.fill = "white"
                except:
                    return
            if key == "," or key == ";":
                solverKnownFillText.value = solverKnownFillText.value + key

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

def onKeyHold(keys):
    if solverBoard.visible:
        if "up" in keys:
            solverBoard.centerY -= 10
            solverBoardNumbersX.centerY -= 10
            solverBoardNumbersY.centerY -= 10
            solverKnownFillField.centerY -= 10
            solverKnownFillText.centerY -= 10
            solverPrereq.centerY -= 10
            for h in testingList: # Slowly I regret substituting the text to be a list instead of a group
                h.centerY -= 10
        if "down" in keys:
            solverBoard.centerY += 10
            solverBoardNumbersX.centerY += 10
            solverBoardNumbersY.centerY += 10
            solverPrereq.centerY += 10
            solverKnownFillField.centerY += 10
            solverKnownFillText.centerY += 10
            for h in testingList:
                h.centerY += 10
        if "left" in keys:
            solverBoard.centerX -= 10
            solverBoardNumbersX.centerX -= 10
            solverBoardNumbersY.centerX -= 10
            solverPrereq.centerX -= 10
            solverKnownFillField.centerX -= 10
            solverKnownFillText.centerX -= 10
            for h in testingList:
                h.centerX -= 10
        if "right" in keys:
            solverBoard.centerX += 10
            solverBoardNumbersX.centerX += 10
            solverBoardNumbersY.centerX += 10
            solverPrereq.centerX += 10
            solverKnownFillField.centerX += 10
            solverKnownFillText.centerX += 10
            for h in testingList:
                h.centerX += 10
    if playBoard.visible:
        if "up" in keys:
            playBoard.centerY -= 10
            playBoardNumbersX.centerY -= 10
            playBoardNumbersY.centerY -= 10
        if "down" in keys:
            playBoard.centerY += 10
            playBoardNumbersX.centerY += 10
            playBoardNumbersY.centerY += 10
        if "left" in keys:
            playBoard.centerX -= 10
            playBoardNumbersX.centerX -= 10
            playBoardNumbersY.centerX -= 10
        if "right" in keys:
            playBoard.centerX += 10
            playBoardNumbersX.centerX += 10
            playBoardNumbersY.centerX += 10

sND = -3

def onStep():
    global sND
    if speechNext.visible:
        if speechNext.height + sND > 20 or speechNext.height + sND < 0:
            sND = sND * -1
        speechNext.height += sND
        speechNext.bottom = speechBubble.bottom - 20

cmu_graphics.run()