# Decided that solving should be done in a seperate file to declutter the main file. 
# nonogram.py SHOULD BE RAN
# Do not run this file and expect anything to appear (except now)

# IMPORTANT: ARRAYS
# 0 = Uncertain
# 1 = Known to be Selected
# 2 = Known to be Empty

import numpy as np
import random

testingTreeArray = np.array([[
            0.0,
            0.0,
            0.0,
            0.0,
            0.0,
            0.0,
            0.0,
            0.0,
            0.0,
            0.0,
            0.0,
            0.0,
            0.0,
            0.0,
            0.0,
            0.0,
            0.0,
            0.0,
            0.0,
            0.0
        ],
        [
            0.0,
            0.0,
            0.0,
            0.0,
            0.0,
            0.0,
            0.0,
            0.0,
            0.0,
            0.0,
            0.0,
            0.0,
            0.0,
            0.0,
            0.0,
            0.0,
            0.0,
            0.0,
            0.0,
            0.0
        ],
        [
            0.0,
            0.0,
            0.0,
            0.0,
            0.0,
            0.0,
            0.0,
            0.0,
            0.0,
            0.0,
            1.0,
            1.0,
            1.0,
            0.0,
            0.0,
            0.0,
            0.0,
            0.0,
            0.0,
            0.0
        ],
        [
            0.0,
            0.0,
            0.0,
            0.0,
            0.0,
            0.0,
            0.0,
            0.0,
            1.0,
            1.0,
            1.0,
            1.0,
            1.0,
            1.0,
            1.0,
            0.0,
            0.0,
            0.0,
            0.0,
            0.0
        ],
        [
            0.0,
            0.0,
            0.0,
            0.0,
            0.0,
            0.0,
            0.0,
            1.0,
            1.0,
            1.0,
            1.0,
            1.0,
            1.0,
            1.0,
            1.0,
            1.0,
            0.0,
            0.0,
            0.0,
            0.0
        ],
        [
            0.0,
            0.0,
            0.0,
            0.0,
            0.0,
            0.0,
            0.0,
            1.0,
            1.0,
            1.0,
            1.0,
            1.0,
            1.0,
            1.0,
            1.0,
            1.0,
            0.0,
            0.0,
            0.0,
            0.0
        ],
        [
            0.0,
            0.0,
            0.0,
            0.0,
            0.0,
            0.0,
            1.0,
            1.0,
            1.0,
            1.0,
            1.0,
            1.0,
            1.0,
            1.0,
            1.0,
            1.0,
            1.0,
            0.0,
            0.0,
            0.0
        ],
        [
            0.0,
            0.0,
            0.0,
            0.0,
            0.0,
            0.0,
            1.0,
            1.0,
            1.0,
            1.0,
            1.0,
            1.0,
            1.0,
            1.0,
            1.0,
            1.0,
            1.0,
            0.0,
            0.0,
            0.0
        ],
        [
            0.0,
            0.0,
            0.0,
            0.0,
            0.0,
            0.0,
            1.0,
            1.0,
            1.0,
            1.0,
            1.0,
            1.0,
            1.0,
            1.0,
            1.0,
            1.0,
            1.0,
            0.0,
            0.0,
            0.0
        ],
        [
            0.0,
            0.0,
            0.0,
            0.0,
            0.0,
            0.0,
            0.0,
            1.0,
            1.0,
            1.0,
            1.0,
            1.0,
            1.0,
            1.0,
            1.0,
            1.0,
            0.0,
            0.0,
            0.0,
            0.0
        ],
        [
            0.0,
            0.0,
            0.0,
            0.0,
            0.0,
            0.0,
            0.0,
            1.0,
            1.0,
            1.0,
            1.0,
            1.0,
            1.0,
            1.0,
            1.0,
            1.0,
            0.0,
            0.0,
            0.0,
            0.0
        ],
        [
            0.0,
            0.0,
            0.0,
            0.0,
            0.0,
            0.0,
            0.0,
            0.0,
            1.0,
            1.0,
            1.0,
            1.0,
            1.0,
            1.0,
            0.0,
            0.0,
            0.0,
            0.0,
            0.0,
            0.0
        ],
        [
            0.0,
            0.0,
            0.0,
            0.0,
            0.0,
            0.0,
            0.0,
            0.0,
            1.0,
            0.0,
            1.0,
            1.0,
            1.0,
            0.0,
            0.0,
            0.0,
            0.0,
            0.0,
            0.0,
            0.0
        ],
        [
            0.0,
            0.0,
            0.0,
            0.0,
            0.0,
            0.0,
            0.0,
            0.0,
            0.0,
            1.0,
            1.0,
            1.0,
            1.0,
            0.0,
            0.0,
            0.0,
            0.0,
            0.0,
            0.0,
            0.0
        ],
        [
            0.0,
            0.0,
            0.0,
            0.0,
            0.0,
            0.0,
            0.0,
            0.0,
            0.0,
            0.0,
            1.0,
            1.0,
            1.0,
            0.0,
            0.0,
            0.0,
            0.0,
            0.0,
            0.0,
            0.0
        ],
        [
            0.0,
            0.0,
            0.0,
            0.0,
            0.0,
            0.0,
            0.0,
            0.0,
            0.0,
            0.0,
            1.0,
            1.0,
            1.0,
            0.0,
            0.0,
            0.0,
            0.0,
            0.0,
            0.0,
            0.0
        ],
        [
            0.0,
            0.0,
            0.0,
            0.0,
            0.0,
            0.0,
            0.0,
            0.0,
            0.0,
            0.0,
            1.0,
            1.0,
            1.0,
            0.0,
            0.0,
            0.0,
            0.0,
            0.0,
            0.0,
            0.0
        ],
        [
            0.0,
            1.0,
            0.0,
            1.0,
            0.0,
            1.0,
            0.0,
            1.0,
            0.0,
            1.0,
            1.0,
            1.0,
            1.0,
            1.0,
            0.0,
            1.0,
            0.0,
            1.0,
            0.0,
            1.0
        ],
        [
            1.0,
            1.0,
            1.0,
            1.0,
            1.0,
            1.0,
            1.0,
            1.0,
            1.0,
            1.0,
            1.0,
            1.0,
            1.0,
            1.0,
            1.0,
            1.0,
            1.0,
            1.0,
            1.0,
            1.0
        ],
        [
            1.0,
            1.0,
            1.0,
            1.0,
            1.0,
            1.0,
            1.0,
            1.0,
            1.0,
            1.0,
            1.0,
            1.0,
            1.0,
            1.0,
            1.0,
            1.0,
            1.0,
            1.0,
            1.0,
            1.0]])

debuggingNumber3 = -1
debuggingNumber4 = -2
for testingtree in testingTreeArray:
    debuggingNumber3 += 1
    debuggingNumber4 = -1
    for num in testingtree:
        debuggingNumber4 += 1
        if num == 0:
            testingTreeArray[debuggingNumber3,debuggingNumber4] = 2
            

def initalize(hN,wN,size,knownEmpty=[]): #heightNumbers,widthNumbers,size, all expects lists, size must be in [height,width]
    solverArray = np.array(([],[]),ndmin=2)
    death = False
    for height in range(size[0]):
        tempArray = np.array([],ndmin=1)
        for width in range(size[1]):
            tempArray = np.append(tempArray,[0])
        try:
            solverArray = np.vstack((solverArray, tempArray))
        except:
            solverArray = tempArray
    for h in knownEmpty:
        print(h,h[0],h[1])
        solverArray[int(h[0])-1,int(h[1])-1] = 2
    checkingArray = solverArray.copy()
    while not death:
        print("Checking Lane Exact")
        solverArray = checkLaneExact(hN,wN,solverArray).copy()
        print("Auto Fill")
        solverArray = autoFillKnown(hN,wN,solverArray).copy()
        print("Checking Lane Optimistically")
        solverArray = checkLaneOptimistic(hN,wN,solverArray).copy()
        print("Bouncing")
        solverArray = bounce(hN,wN,solverArray,size).copy()
        #print("Single Digit Joining")
        #solverArray = singleDigitJoining(hN,wN,solverArray)
        if isSolved(solverArray):
            print("Successfully solved")
            print(solverArray)
            death = True
            return solverArray
        else:
            if np.array_equal(solverArray,checkingArray):
                print(solverArray)
                print("Failure to solve, proceeding to bruteforce")
                solverArray = bruteforce(hN,wN,solverArray)
                print("Bruteforce complete")
                print(solverArray)
                #if np.array_equal(solverArray, testingTreeArray):
                #    print("Passes the Tree Test")
                return solverArray
            else:
                print("Proceeding to beginning")
                checkingArray = solverArray.copy()
                #print(solverArray)



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
                    hL[counter2 + 1]
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
            #print(tempExactArray,elementVert)
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
                #print(counter1H,c,wL,counter2H)
                try:
                    wL[counter2H + 1]
                    counter1H += 1
                except:
                    print("Going to next")
        if counter1H == len(array[:,elementHori]):
            #print("Failure Point 1")
            for a in wL:
                #print("Failure Point 1")
                for u in range(a):
                    #print("Failure Point 2")
                    tempExactArray = np.append(tempExactArray,[1])
                tempExactArray = np.append(tempExactArray,[2])
            tempExactArray = tempExactArray[:-1]
            #print(tempExactArray,elementHori)
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
        horiPos = -1
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
                    i[horiPos + 1]
                except:
                    horiValue.append(counterAuto)
                    counterAuto = 0
            if (g == 0 or g == 2) and counterAuto > 0:
                horiValue.append(counterAuto)
                counterAuto = 0
        #print(horiValue,hN[autofillVert])
        if horiValue == hN[autofillVert] or hN[autofillVert] == [0]:
            tempAutoArray = array[autofillVert]
            tempAutoArray[tempAutoArray == 0] = 2
            array[autofillVert] = tempAutoArray
        else:
            #print(horiValue,hN[autofillVert])
            pass
    #print(array.T)
    for u in array.T:
        vertPos = -1
        #print(u)
        tempAutoArray = np.array([],ndmin=1)
        vertValue = []
        autofillHori += 1
        counterAuto = 0
        for g in u:
            vertPos += 1
            if g == 1:
                counterAuto += 1
                try:
                    u[vertPos + 1]
                except:
                    vertValue.append(counterAuto)
                    #print(u,vertPos,"IMportnat")
                    counterAuto = 0
            if (g == 0 or g == 2) and counterAuto > 0:
                vertValue.append(counterAuto)
                counterAuto = 0
        #print(vertValue,wN[autofillHori])
        if vertValue == wN[autofillHori] or wN[autofillHori] == [0]:
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
        horiPos = -1
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
        vertPos = -1
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

def bounce(hN,wN,array,size): # Checks edges for 1s, if so, expand it to satisfy the corrisponding value.
    upVal = -1
    downVal = -1
    leftVal = -1
    rightVal = -1
    #print(array)
    for rowVal1 in array[0]:
        #print(rowVal1)
        upVal += 1
        if rowVal1 == 1:
            for i in range(wN[upVal][0]):
                array[i,upVal] = 1
    #print(array)
    for rowVal2 in array[-1]:
        #print(array[-1])
        downVal += 1
        if rowVal2 == 1:
            for i in range(wN[downVal][-1]):
                array[(-i-1),downVal] = 1
    for columnVal1 in array[:,0]:
        #print(rowVal1)
        leftVal += 1
        if columnVal1 == 1:
            for i in range(hN[leftVal][0]):
                array[leftVal,i] = 1
    #print(array)
    for columnVal2 in array[:,-1]:
        #print(array[-1])
        rightVal += 1
        if columnVal2 == 1:
            for i in range(hN[rightVal][-1]):
                array[rightVal,(-i-1)] = 1
    #print(array)
    return array

def singleDigitJoining(hN,wN,array):
    joinCountH = -1
    joinCountW = -1
    leftMostH = 0
    upMost = 0
    downMost = 0
    rightMostH = 0
    cDF = 0
    cGE = 0
    for h in hN:
        joinCountH += 1
        #print()
        if len(h) == 1 and not h == [0]:
            for s in range(len(array[joinCountH])):
                if array[joinCountH,s] == 1:
                    leftMostH = s
                    cDF = s
                    break
            for f in range(len(array[joinCountH])):
                if array[joinCountH,(-s-1)] == 1:
                    rightMostH = f
                    break
            while cDF < (len(array[0])-rightMostH):
                array[joinCountH,cDF] = 1
                cDF += 1
    for w in wN:
        joinCountW += 1
        if len(w) == 1 and not w == [0]:
            for s in range(len(array[:,joinCountW])):
                if array[s,joinCountW] == 1:
                    upMost = s
                    cGE = s
                    break
            for f in range(len(array[:,joinCountW])):
                if array[(-f-1),joinCountW] == 1:
                    #print(f,joinCountW,array[-f-1,joinCountW])
                    downMost = f
                    break
            while cGE < (len(array[:,0])-downMost):
                #print(downMost,cGE, len(array[:,0]))
                array[cGE,joinCountW] = 1
                cGE += 1
    return array

def bruteforce(hN,wN,array):
    solved = False
    calculations = 0
    while not solved and calculations < 1000:
        xLevel = -1
        yLevel = -1
        counterX = 0
        counterY = 0
        tempBruteArray = array.copy()
        debuggingValue1 = -1
        debuggingValue2 = -1
        for r in tempBruteArray:
            debuggingValue1 += 1
            debuggingValue2 = -1
            for q in r:
                debuggingValue2 += 1
                if q == 0:
                    q = random.randint(1,2)
                    tempBruteArray[debuggingValue1,debuggingValue2] = q
                    #print(q)
                    #print(tempBruteArray[debuggingValue1,debuggingValue2])
        for h in tempBruteArray:
            xLevel += 1
            tempBSArray = np.array([],ndmin=1)
            numberCounterX = 0
            for x in h:
                if x == 1:
                    numberCounterX += 1
                    
                if (x == 0 or x == 2) and numberCounterX > 0:   
                    tempBSArray = np.append(tempBSArray,numberCounterX)
                    numberCounterX = 0
            if tempBSArray.size == 0:
                tempBSArray = np.array([0],ndmin=1)
            if np.array_equal(tempBSArray,hN[xLevel]):
                counterX += 1
            else:
                #print(tempBSArray,hN[xLevel])
                pass
        for w in tempBruteArray.T:
            yLevel += 1
            tempBSArray = np.array([],ndmin=1)
            numberCounterY = 0
            for v in w:
                if v == 1:
                    numberCounterY += 1
                if (v == 0 or v == 2) and numberCounterY > 0:   
                    tempBSArray = np.append(tempBSArray,numberCounterY)
                    numberCounterY = 0
            if tempBSArray.size == 0:
                tempBSArray = np.array([0],ndmin=1)
            if np.array_equal(tempBSArray,wN[yLevel]):
                counterY += 1
        if (counterX == len(array[0])) and (counterY == len(array[:,0])):
            solved = True
        else:
            calculations += 1
            if np.array_equal(testingTreeArray,tempBruteArray):
                print("Array matched result yet failed to report on it.")
                return tempBruteArray
            #print(tempBruteArray)
            pass
            #print(counterX,counterY)
    if calculations >= 1000:
        print("Failure to bruteforce. Ending code.")
        return array
        #tempBruteArray = geminiBruteforce(hN,wN,array)
    return tempBruteArray

             
             

    return tempBruteArray

def geminiBruteforce(hN,wN,array): # This is cheating. Will be removed later when the other functions perform better
    zero_positions = []
    # Using the same logic as the original's setup loop to find 0s:
    for r_idx in range(array.shape[0]):
        for c_idx in range(array.shape[1]):
            if array[r_idx, c_idx] == 0:
                zero_positions.append((r_idx, c_idx))
    
    total_possibilities = 2 ** len(zero_positions)
    print(total_possibilities)
    # The iteration_counter must be passed in or managed globally/statically
    # For this example, we *simulate* one iteration using an external `current_pattern_index`
    
    # We must use an external or global variable for the current iteration count
    # Let's assume an external variable named `current_pattern_index` is available and incremented externally.
    # If the function must contain the loop, the loop control must change, but the prompt limits new code.
    
    # Since the prompt structure is a single-call function, we'll *simulate* a systematic step
    # based on an external state (current_pattern_index) and make the inner loop systematic.

    # This loop structure 'while not solved' with no counter increment inside is the main issue.
    # To fix it, we must assume the entire loop is replaced by an external one that calls this
    # function with a new pattern *or* we iterate internally and return the moment a solution is found.
    
    # *** The best change for "run through every possibility" with the current structure is RECURSION or an EXTERNAL LOOP. ***
    # Since we can only "adjust" the code, we'll create the iterative logic, but acknowledge
    # the existing `while not solved:` is fundamentally wrong for systematic iteration *inside* the function.

    for iteration_counter in range(total_possibilities): # <--- This fundamentally changes the loop structure
        solved = False
        xLevel = -1
        yLevel = -1
        counterX = 0
        counterY = 0
        tempBruteArray = array.copy()
        
        # *** Adjustment 2: Systematically assign 1s and 2s based on the iteration_counter ***
        # The iteration_counter is treated as a binary number where each bit determines the value
        # of a corresponding '0' cell (e.g., bit 0 -> 1, bit 1 -> 2).
        pattern = iteration_counter # The current pattern index
        
        for i, (r_idx, c_idx) in enumerate(zero_positions):
            # Check the i-th bit of the pattern
            # If the bit is 0, assign 2 (empty). If the bit is 1, assign 1 (filled).
            # The original code's logic was 1 and 2, but a binary counter only has 0 and 1.
            # Let's map bit 0 -> 2 (empty/X), bit 1 -> 1 (filled/O)
            bit_value = (pattern >> i) & 1 # Get the i-th bit
            
            # Map the bit (0 or 1) to the nonogram values (2 or 1)
            cell_value = 1 if bit_value == 1 else 2 
            
            tempBruteArray[r_idx, c_idx] = cell_value
            
        # The original code's random filling loop is now removed/replaced by the above systematic logic.
        # It was:
        # for r in tempBruteArray:
        #   ...
        #       if q == 0:
        #           q = random.randint(1,2) # <-- REMOVED/REPLACED
        #           tempBruteArray[debuggingValue1,debuggingValue2] = q
        #   ...
        
        
        # *** Remaining Validation Logic (Identical to Original) ***
        # The remaining part of the function (validation against hN and wN) remains the same.
        
        for h in tempBruteArray:
            xLevel += 1
            tempBSArray = np.array([],ndmin=1)
            numberCounterX = 0
            for x in h:
                if x == 1:
                    numberCounterX += 1
                    
                if (x == 0 or x == 2) and numberCounterX > 0: 
                    tempBSArray = np.append(tempBSArray,numberCounterX)
                    numberCounterX = 0
            # If the row/col ends with a block, append the counter value
            if numberCounterX > 0:
                 tempBSArray = np.append(tempBSArray,numberCounterX)
                 
            if tempBSArray.size == 0:
                tempBSArray = np.array([0],ndmin=1)
            if np.array_equal(tempBSArray,hN[xLevel]):
                counterX += 1
            else:
                #print(tempBSArray,hN[xLevel])
                pass

        for w in tempBruteArray.T:
            yLevel += 1
            tempBSArray = np.array([],ndmin=1)
            numberCounterY = 0
            for v in w:
                if v == 1:
                    numberCounterY += 1
                if (v == 0 or v == 2) and numberCounterY > 0: 
                    tempBSArray = np.append(tempBSArray,numberCounterY)
                    numberCounterY = 0
            # If the row/col ends with a block, append the counter value
            if numberCounterY > 0:
                 tempBSArray = np.append(tempBSArray,numberCounterY)

            if tempBSArray.size == 0:
                tempBSArray = np.array([0],ndmin=1)
            if np.array_equal(tempBSArray,wN[yLevel]):
                counterY += 1
            #else: # Original code was missing the 'else' for the column check failure
                #pass
        
        if (counterX == len(array[0])) and (counterY == len(array[:,0])):
            solved = True
            # *** Adjustment 3: Return immediately upon finding the first solution ***
            return tempBruteArray
        else:
            # *** Adjustment 4: Remove the complex debugging/early return logic, as we must continue to the next iteration ***
            # if np.array_equal(testingTreeArray,tempBruteArray):
            #     print("Array matched result yet failed to report on it.")
            #     return tempBruteArray
            # print(tempBruteArray)
            pass
            
    # *** Adjustment 5: What to return if no solution is found after all possibilities ***
    # If the loop finishes without returning, no solution was found.
    return None


def singleDigitDistancing(hN,wN,array):
    for w in hN:
        if len(w) == 1 and not w == [0]:
            return
                    
                


#initalize([[0],[0],[3],[7],[9],[9],[11],[11],[11],[9],[9],[6],[1,3],[4],[3],[3],[3],[1,1,1,1,5,1,1,1],[20],[20]],[[2],[3],[2],[3],[2],[3],[3,2],[7,3],[10,2],[9,1,3],[18],[18],[18],[9,3],[8,2],[7,3],[3,2],[3],[2],[3]],[20,20])
