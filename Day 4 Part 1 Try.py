#So we have a system of arrays
#we check what's around the @ and count if the are less than 4 @ beside it

with open("Day4 Input.txt", "rt") as f:
    lines=f.readlines() #Creates an array list of the rows in the input

maxCollumn=len(lines[0].strip())
maxRow=len(lines)

print("Collumns:", len(lines[0].strip()), "Rows:", len(lines))

#As we iterate through each point, there is a corresponding row and collumn
#we need to be able to access points easily

#We need logic that automatically checks surrounding positions when given the coordinates
#Logic should have fall backs if the position surpasses a boundary

def checkPosition(row, collumn):
    global lines
    if (row-1 >= 0 and row-1 < maxRow) and (collumn-1 >=0 and collumn-1 < maxCollumn):
        return lines[row-1][collumn-1]
    else:
        return "Invalid"

def positionRight(row, collumn):
    global lines
    if (row-1 >= 0 and row-1 < maxRow) and (collumn >=0 and collumn < maxCollumn):
        return lines[row-1][collumn]
    else:
        return "x"

def positionLeft(row, collumn):
    global lines
    if (row-1 >= 0 and row-1 < maxRow) and (collumn-2 >=0 and collumn-2 < maxCollumn):
        return lines[row-1][collumn-2]
    else:
        return "x"

def positionTop(row, collumn):
    global lines
    if (row-2 >= 0 and row-2 < maxRow) and (collumn-1 >=0 and collumn-1 < maxCollumn):
        return lines[row-2][collumn-1]
    else:
        return "x"

def positionBottom(row, collumn):
    global lines
    if (row >= 0 and row < maxRow) and (collumn-1 >= 0 and collumn-1 < maxCollumn):
        return lines[row][collumn-1]
    else:
        return "x"

def positionBottomRight(row, collumn):
    global lines
    if (row >= 0 and row < maxRow) and (collumn >=0 and collumn < maxCollumn):
        return lines[row][collumn]
    else:
        return "x"

def positionBottomLeft(row, collumn):
    global lines
    if (row >= 0 and row < maxRow) and (collumn-2 >=0 and collumn-2 < maxCollumn):
        return lines[row][collumn-2]
    else:
        return "x"

def positionTopRight(row, collumn):
    global lines
    if (row-2 >= 0 and row-2 < maxRow) and (collumn >=0 and collumn < maxCollumn):
        return lines[row-2][collumn]
    else:
        return "x"

def positionTopLeft(row, collumn):
    global lines
    if (row-2 >= 0 and row-2 < maxRow) and (collumn-2 >=0 and collumn-2 < maxCollumn):
        return lines[row-2][collumn-2]
    else:
        return "x"

#Sees if the "@" is surrounded by less than 4 "@"
def checkCount(row, collumn):
    count=0
    if positionTop(row, collumn)=="@":
        count+=1
    else:
        count+=0
    if positionRight(row, collumn)=="@":
        count+=1
    else:
        count+=0
    if positionLeft(row, collumn)=="@":
        count+=1  
    else:
        count+=0
    if positionBottom(row, collumn)=="@":
        count+=1
    else:
        count+=0
    if positionTopRight(row, collumn)=="@":
        count+=1
    else:
        count+=0
    if positionTopLeft(row, collumn)=="@":
        count+=1
    else:
        count+=0
    if positionBottomRight(row, collumn)=="@":
        count+=1
    else:
        count+=0
    if positionBottomLeft(row, collumn)=="@":
        count+=1
    else:
        count+=0
    
    if count<4:
        return True
    else:
        return False
    

answer=0

#Iterate through input and check if "@" is movable ie. less than 4 "@" adjoining it
for row in range(maxRow):
    for collumn in range(maxCollumn):
        print(row+1, collumn+1)
        if checkPosition(row+1, collumn+1)=="@" and checkCount(row+1, collumn+1):
            answer+=1 

print("Answer:", answer)