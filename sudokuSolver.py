from random import randrange, shuffle
from math import floor
from datetime import datetime

# V1 complete

newPuzzle =  [[0,0,0,0,0,0,0,0,0],
              [0,0,0,0,0,0,0,0,0],
              [0,0,0,0,0,0,0,0,0],
              [0,0,0,0,0,0,0,0,0],
              [0,0,0,0,0,0,0,0,0],
              [0,0,0,0,0,0,0,0,0],
              [0,0,0,0,0,0,0,0,0],
              [0,0,0,0,0,0,0,0,0],
              [0,0,0,0,0,0,0,0,0]]

easyPuzzle=[[0,9,0,0,2,0,0,0,5],
              [0,5,7,9,0,0,0,0,0],
              [0,0,0,5,0,0,0,0,6],
              [6,0,2,3,0,1,9,0,0],
              [8,3,0,0,6,9,2,0,0],
              [0,4,0,0,0,0,6,1,3],
              [0,0,0,0,1,5,4,2,9],
              [0,1,0,6,0,0,0,7,0],
              [0,2,8,0,3,4,5,6,0]]

mediumPuzzle=[[2,0,0,0,0,7,5,0,0],
              [0,6,5,0,1,0,0,0,4],
              [7,0,0,0,5,0,0,0,0],
              [0,0,0,0,0,6,9,0,3],
              [6,0,0,0,0,0,0,7,8],
              [0,7,4,0,0,1,0,0,0],
              [0,0,0,4,0,0,0,0,1],
              [4,3,7,0,0,0,0,9,5],
              [9,0,2,5,3,8,0,0,0]]

hardPuzzle =[ [6,0,0,0,0,0,8,0,0],
              [0,0,5,0,0,0,0,3,0],
              [0,0,0,5,0,2,4,0,0],
              [0,8,0,0,4,3,0,0,0],
              [7,1,6,0,0,0,0,0,0],
              [0,3,0,0,0,9,0,0,0],
              [0,0,0,0,7,0,0,0,0],
              [0,0,8,0,1,0,0,0,6],
              [0,0,0,3,0,0,0,7,1]]

solvedPuzzle = [[1,2,3,4,5,6,7,8,9],
              [4,5,6,7,8,9,1,2,3],
              [7,8,9,1,2,3,4,5,6],
              [2,3,4,5,6,7,8,9,1],
              [5,6,7,8,9,1,2,3,4],
              [8,9,1,2,3,4,5,6,7],
              [3,4,5,6,7,8,9,1,2],
              [6,7,8,9,1,2,3,4,5],
              [9,1,2,3,4,5,6,7,8]]

chatgptPuzzle = [[3,9,6,1,2,4,7,8,5],
                [2,5,7,9,8,3,1,4,6],
                [4,8,1,5,7,6,9,3,2],
                [6,7,2,3,4,1,8,5,9],
                [8,3,1,7,6,9,2,4,5],
                [9,4,5,8,2,7,6,1,3],
                [7,6,3,4,1,5,4,2,9],
                [4,1,9,6,5,2,3,7,8],
                [5,2,8,9,3,4,1,6,7]]

chatgptPuzzle2 = [[1, 9, 4, 8, 2, 6, 7, 3, 5],
                [3, 5, 7, 9, 8, 4, 1, 2, 6],
                [2, 6, 8, 5, 7, 1, 4, 9, 3],
                [6, 7, 2, 3, 9, 4, 5, 8, 1],
                [4, 8, 1, 7, 6, 5, 9, 3, 2],
                [9, 3, 5, 2, 1, 8, 6, 7, 4],
                [8, 1, 6, 4, 3, 7, 2, 5, 9],
                [7, 4, 9, 6, 5, 2, 3, 1, 8],
                [5, 2, 3, 1, 4, 9, 8, 6, 7]]

def printSudoku (sudoku):
    print("___________________")
    row = "|"
    for i in range(9):
        for j in range(9):
            if (j in [0,1,3,4,6,7,]):
                row = row + str(sudoku[i][j])+ " "
            else:
                row = row + str(sudoku[i][j]) + "|"
        print(row)
        row = "|"
        if i in [2,5,8]:
            print("___________________")

def validQuadrant(quadrant,sudoku):
    startingPoints = [[0,0],[0,3],[0,6],[3,0],[3,3],[3,6],[6,0],[6,3],[6,6]]
    nums = []
    for i in range(3):
        for j in range(3):
            start = startingPoints[quadrant]
            nums.append(sudoku[start[0]+i][start[1]+j])
   # print("nums in quadrant ", quadrant, nums)

    if checkDuplicate(nums):
        return False
    elif invalidNumber(nums):
        return False
    else:
        return True

def checkQuadrants(sudoku):
    for i in range(9):
        if not (validQuadrant(i,sudoku)):
            return False
    return True

def validRow(row,sudoku):
    nums = sudoku[row]
    if checkDuplicate(nums):
        return False
    elif invalidNumber(nums):
        return False
    else:
        return True

def checkRows(sudoku):
    for i in range(9):
        if not (validRow(i,sudoku)):
            return False
    return True

def validColumn(column,sudoku):
    nums = []
    for i in range(9):
        nums.append(sudoku[i][column])

    if checkDuplicate(nums):
        return False
    elif invalidNumber(nums):
        return False
    else:
        return True

def checkColumns(sudoku):
    for i in range(9):
        if not (validColumn(i,sudoku)):
            return False
    return True

def hasZero(sudoku):
    for row in sudoku:
        if 0 in row:
            return True
    return False 

def checkDuplicate(nums):
    for i in range(9):
        i = i + 1
        if nums.count(i) > 1:
            return True  
    return False

def invalidNumber(nums):
    for i in nums:
        if not (0 <= i <= 9):
            return True
    return False

def checkPuzzle(sudoku):
    return checkColumns(sudoku) & checkQuadrants(sudoku) & checkRows(sudoku)

def getBusiestCell(sudoku):
    cell = [0,0]
    bestClues = 0
    for i in range(9):
        for j in range(9):
            clues = getClues(sudoku, [i,j])
            if clues > bestClues and sudoku[i][j]==0:
                cell = [i,j]
                bestClues = clues
    return cell

def getClues(sudoku, cell):
    clues = 0
    for i in sudoku[cell[0]]:
        if i > 0:
            clues+=1
    for i in range(9):
        if sudoku[i][cell[1]] > 0:
            clues+=1
    
    x = floor(cell[0]/3)
    y = floor(cell[1]/3)

    startingPoints = [[[0,0],[0,3],[0,6]],[[3,0],[3,3],[3,6]],[[6,0],[6,3],[6,6]]]
    start = startingPoints[x][y]

    for i in range(3):
        for j in range(3):
            if sudoku[start[0]+i][start[1]+j] > 0:
                clues+=1

    return clues


def is_valid(sudoku, cell, num):
    sudoku[cell[0]][cell[1]] = num
    if checkPuzzle(sudoku):
        return True
    else:
        sudoku[cell[0]][cell[1]] = 0
        return False

def completePuzzle(sudoku):
    return checkPuzzle(sudoku) & (not hasZero(sudoku))

#### SOLVER LOGIC

def getEmptyCell(sudoku):
    cell = [randrange(0,9), randrange(0,9)]
    while (sudoku[cell[0]][cell[1]] != 0):
        cell = [randrange(0,9), randrange(0,9)]
    return cell

def makeRandomValidMove(sudoku):
    cell = getEmptyCell(sudoku)
    r = list(range(1,10))
    shuffle(r)
    for i in r:
        sudoku[cell[0]][cell[1]] = i
        if checkPuzzle(sudoku):
            return sudoku
    print("game over")
    printSudoku(sudoku)
    return "game over"

def playGameBacktracing(sudoku):
    if completePuzzle(sudoku):
        return [True, sudoku]
    else:
        cell = getBusiestCell(sudoku)

    for num in range(1,10):
        if is_valid(sudoku, cell, num):
            sudoku[cell[0]][cell[1]] = num
            #print("trying num: ", num, " at cell: ", cell)
            #printSudoku(sudoku)
            if playGameBacktracing(sudoku)[0]:
                return [True, sudoku]
            else:
                sudoku[cell[0]][cell[1]] = 0

    return [False, sudoku]

def playRandomGameBacktracing(sudoku):
    if completePuzzle(sudoku):
        return [True, sudoku]
    else:
        cell = getEmptyCell(sudoku)

    for num in range(1,10):
        if is_valid(sudoku, cell, num):
            sudoku[cell[0]][cell[1]] = num
            #print("trying num: ", num, " at cell: ", cell)
            #printSudoku(sudoku)
            if playRandomGameBacktracing(sudoku)[0]:
                return [True, sudoku]
            else:
                sudoku[cell[0]][cell[1]] = 0

    return [False, sudoku]


# print(validQuadrant(2,solvedPuzzle))
#print("Valid Puzzle Quadrants: ", checkQuadrants(solvedPuzzle))
#print("Valid Puzzle Rows: ", checkRows(solvedPuzzle))
#print("Valid Puzzle Columns: ", checkColumns(solvedPuzzle))
#print("Valid Puzzle: ", checkPuzzle(samplePuzzle))
#print("Complete Puzzle: ", completePuzzle(samplePuzzle))

""" printSudoku(samplePuzzle)
results = ""
tries = 0
while results != "win":
    results = playRandomGame(samplePuzzle)
    tries+=1
print("TOTAL TRIES To win: ", tries) """


""" printSudoku(mediumPuzzle)
#print(getBusiestCell(samplePuzzle))
results = playGameBacktracing(mediumPuzzle)
if results[0]:
    print("WINNER WINNER CHICKEN DINNER")
    printSudoku(results[1])
else:
    print("you lose, GAME OVER!")
    printSudoku(results[1]) """

busiestTimes = [0,0,0]
randomTimes = [0,0,0]

print("Random Method")
startTime = datetime.now()
results = playRandomGameBacktracing(easyPuzzle)
randomTimes[0] = datetime.now() - startTime
print("Easy: ", randomTimes[0])

startTime = datetime.now()
results = playRandomGameBacktracing(mediumPuzzle)
randomTimes[1] = datetime.now() - startTime
print("Medium: ", randomTimes[1])

startTime = datetime.now()
results = playRandomGameBacktracing(hardPuzzle)
randomTimes[2] = datetime.now() - startTime
print("Hard: ", randomTimes[2])

print("\nBusiest Method")
startTime = datetime.now()
results = playGameBacktracing(easyPuzzle)
busiestTimes[0] = datetime.now() - startTime
print("Easy: ", busiestTimes[0])

startTime = datetime.now()
results = playGameBacktracing(mediumPuzzle)
busiestTimes[1] = datetime.now() - startTime
print("Medium: ", busiestTimes[1])

startTime = datetime.now()
results = playGameBacktracing(hardPuzzle)
busiestTimes[2] = datetime.now() - startTime
print("Hard: ", busiestTimes[2])
