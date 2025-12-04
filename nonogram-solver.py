# Decided that solving should be done in a seperate file to declutter the main file. 
# nonogram.py SHOULD BE RAN
# Do not run this file and expect anything to appear (except now)

# IMPORTANT: ARRAYS
# 0 = Uncertain
# 1 = Known to be Selected
# 2 = Known to be Empty

import numpy as np

def initalize(hN,wN,size): #heightNumbers,widthNumbers,size, all expects lists, size must be in [height,width]
    solverArray = np.array(([],[]),ndmin=2)
    for height in range(size[0]):
        tempArray = np.array([],ndmin=1)
        for width in range(size[1]):
            tempArray = np.append(tempArray,[0])
        try:
            solverArray = np.vstack((solverArray, tempArray))
        except:
            solverArray = tempArray
    solverArray = checkLaneExact(hN,wN,solverArray)
    solverArray = autoFillKnown(hN,wN,solverArray)
    solverArray = checkLaneOptimistic(hN,wN,solverArray)
    if isSolved(solverArray):
        print(solverArray)
    else:
        print("Failure to solve")

def isSolved(array):
    solved = True
    for i in array:
        for g in i:
            #print(g)
            if g == 0:
                solved = False
    return solved

def checkLaneExact(hN,wN,array1):
    array = array1
    elementVert = -1
    elementHori = -1
    tempExactArray = np.array([],ndmin=1)
    counter1 = 0
    counter1H = 0
    counter2 = -1
    counter2H = -1
    for hL in hN:
        tempExactArray = np.array([],ndmin=1)
        elementVert += 1
        counter1 = 0
        counter2 = -1
        for i in hL:
            counter2 += 1
            if not hL == [0]:
                counter1 += i
                try:
                    print(hL[counter2 + 1])
                    counter1 += 1
                except:
                    print("Going to next")
        if counter1 == len(array[elementVert]):
            for j in hL:
                for u in range(j):
                    tempExactArray = np.append(tempExactArray,[1])
                    print("Adding Value 1 to tempArray.",j)
                tempExactArray = np.append(tempExactArray,[2])
                print("Adding Value 2 to tempArray.",j)
            tempExactArray = tempExactArray[:-1]
            print(tempExactArray,elementVert)
            array[elementVert] = tempExactArray
        else:
            print("Given row does not fill in properly")
    print("Proceeding to Columns")
    tempExactArray = np.array([],ndmin=1)
    for wL in wN:
        tempExactArray = np.array([],ndmin=1)
        elementHori += 1
        counter1H = 0
        counter2H = -1
        for c in wL:
            counter2H += 1
            if not wL == [0]:
                counter1H += c
                print(counter1H,c,wL,counter2H)
                try:
                    print(wL[counter2H + 1])
                    counter1H += 1
                except:
                    print("Going to next")
        if counter1H == len(array[:,elementHori]):
            print("Failure Point 1")
            for a in wL:
                print("Failure Point 1")
                for u in range(a):
                    print("Failure Point 2")
                    tempExactArray = np.append(tempExactArray,[1])
                tempExactArray = np.append(tempExactArray,[2])
            tempExactArray = tempExactArray[:-1]
            print(tempExactArray,elementHori)
            array[:,elementHori] = tempExactArray
        else:
            print("Given row does not fill in properly")
    print("Success in Exacting")
    return array

def autoFillKnown(hN,wN,array):
    autofillHori = -1
    autofillVert = -1
    counterAuto = 0
    horiPos = -1
    horiValue = []
    vertPos = -1
    vertValue = []
    for i in array:
        #print(i)
        tempAutoArray = np.array([],ndmin=1)
        horiValue = []
        autofillVert += 1
        counterAuto = 0
        for g in i:
            horiPos += 1
            if g == 1:
                counterAuto += 1
                try:
                    print(i[horiPos + 1])
                except:
                    horiValue.append(counterAuto)
                    counterAuto = 0
            if (g == 0 or g == 2) and counterAuto > 0:
                horiValue.append(counterAuto)
                counterAuto = 0
        #print(horiValue,hN[autofillVert])
        if horiValue == hN[autofillVert]:
            tempAutoArray = array[autofillVert]
            tempAutoArray[tempAutoArray == 0] = 2
            array[autofillVert] = tempAutoArray
    print(array.T)
    for i in array.T:
        #print(i)
        tempAutoArray = np.array([],ndmin=1)
        vertValue = []
        autofillHori += 1
        counterAuto = 0
        for g in i:
            vertPos += 1
            if g == 1:
                counterAuto += 1
                try:
                    print(i[vertPos + 1])
                except:
                    vertValue.append(counterAuto)
                    counterAuto = 0
            if (g == 0 or g == 2) and counterAuto > 0:
                vertValue.append(counterAuto)
                counterAuto = 0
        #print(vertValue,wN[autofillHori])
        if vertValue == wN[autofillHori]:
            tempAutoArray = array[:,autofillHori]
            tempAutoArray[tempAutoArray == 0] = 2
            array.T[autofillHori] = tempAutoArray
    return array

def checkLaneOptimistic(hN,wN,array): # Assumes that empty spaces are filled in and creates a hint from then. If that hint is the same as its real hint, fill all in
    autofillHori = -1
    autofillVert = -1
    counterAuto = 0
    horiPos = -1
    horiValue = []
    vertPos = -1
    vertValue = [] 
    for i in array:
        #print(i)
        tempAutoArray = np.array([],ndmin=1)
        horiValue = []
        autofillVert += 1
        counterAuto = 0
        for g in i:
            horiPos += 1
            if g == 0 or g == 1:
                counterAuto += 1
                try:
                    print(i[horiPos + 1])
                except:
                    horiValue.append(counterAuto)
                    counterAuto = 0
            if (g == 2) and counterAuto > 0:
                horiValue.append(counterAuto)
                counterAuto = 0
        #print(horiValue,hN[autofillVert])
        if horiValue == hN[autofillVert]:
            tempAutoArray = array[autofillVert]
            tempAutoArray[tempAutoArray == 0] = 1
            array[autofillVert] = tempAutoArray
    for i in array.T:
        #print(i)
        tempAutoArray = np.array([],ndmin=1)
        vertValue = []
        autofillHori += 1
        counterAuto = 0
        for g in i:
            vertPos += 1
            if g == 1 or g == 0:
                counterAuto += 1
                try:
                    print(i[vertPos + 1])
                except:
                    vertValue.append(counterAuto)
                    counterAuto = 0
            if (g == 2) and counterAuto > 0:
                vertValue.append(counterAuto)
                counterAuto = 0
        #print(vertValue,wN[autofillHori])
        if vertValue == wN[autofillHori]:
            tempAutoArray = array[:,autofillHori]
            tempAutoArray[tempAutoArray == 0] = 1
            array.T[autofillHori] = tempAutoArray
    return array

                    
                


initalize([[1,1,1],[1,1],[1],[1],[1]],[[1],[1],[1,3],[1],[1]],[5,5])

"""
Title: Nonogram Solver
Author: TomatOid
Date: December 3th, 2025
Availability: https://github.com/TomatOid/nonogram_solver/blob/master/nonogram_solver.py
Note: I will be studying this file and analyzing how TomatOid did this, and rewriting most of it
to work with the set up I plan for it.
"""