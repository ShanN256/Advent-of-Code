#Now we must run through the input, change the "@" to "x", create function to rewrite
#loop around again, and check if the answer has changed, keep looping untill there is zero change

with open("Day4 Test Input.txt", "rt") as f:
    lines=f.readlines() #Creates an array list of the rows in the input

maxCollumn=len(lines[0].strip())
maxRow=len(lines)

print("Collumns:", len(lines[0].strip()), "Rows:", len(lines))

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

def positionRewrite(row, collumn):
    global lines
    newRow="" #Temporary holds the new line as we construct it
    for i in range(maxCollumn):
        if i != collumn-1: #If not the selected index, keep the position the same as before
            newRow+=lines[row-1][i]
        else:
            newRow+="x"
    lines[row-1]=newRow #changes the recorded input to new


def printInput():
    #Prints as seperate strings for rows rather than array list format
    for line in lines:
        print(line)

def move():
    global lines
    global answer

    count=0 #We store the number of @'s moved during each run
    #Store indexes of movable "@"
    rows=[]
    collumns=[]

    #Iterate through input and check if "@" is movable ie. less than 4 "@" adjoining it
    for row in range(maxRow):
        for collumn in range(maxCollumn):
            if checkPosition(row+1, collumn+1)=="@" and checkCount(row+1, collumn+1):
                count+=1
                #Store indexes of movable "@"
                rows.append(row+1)
                collumns.append(collumn+1)

    #Rewrites input with all possible "@"s moved
    for i in range(len(rows)):
        positionRewrite(rows[i], collumns[i])

    #Initially i tried to rewrite the input as i count the @'s movable however i ran into indexing issues
    #So i stored the indexes separately and rewrote everything at the end not while counting movable @'s

    print("Removed", len(rows), "@'s:")
    printInput()
    print()

    answer+=count #Add up the number of "@"s moved after each run

    if count>0:
        return True
    else:
        print("All movable @'s moved")
        print("Answer:", answer)
        return False
    
    
answer=0
while True: #Loops through runs until no movable @'s are found
    if move()==False:
        break



#Issue, Line Rewrite function is not functioning correctly and thus causes the answer to be wrong
#I must test the logic of the function
#Complex indexng issuesprintInput()
