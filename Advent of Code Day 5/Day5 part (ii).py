#Objective, look at the ranges and determines the number of IDs seen as fresh

with open("testInput.txt", "rt") as f:
    lines=f.readlines() #Creates an array list of the rows in the input

#index of the gap between ranges and values
index=0
for i in range(len(lines)):
    if lines[i].strip()=="":
        index=i

#Example Range: '1234-1334'
lowerRange=[] #'1234'
higherRange=[] #'1334       


for i in range(index): #Iterates through all ranges
    lowerRange.append(lines[i].strip().split("-")[0]) #Splits to array list of lowerRange and upperRange
    higherRange.append(lines[i].strip().split("-")[1]) #We append the appropriate value to range collection

    
numbers=[]

newLowerRange=[]
newHigherRange=[]

def ammendNewRange(lowerValue, higherValue):
    global newLowerRange
    global newHigherRange
    b=True
    for y in range(len(newLowerRange)):
            #Checks if the next lower range is within the range of another
            # We then can change the upperRange 
            if lowerValue>newLowerRange[y] and lowerValue<newHigherRange[y] and b:
                newHigherRange[y]=higherValue
                b=False
            
            #if the next higher range is within the range of another
            # We can then change the lowerRange
            elif higherValue>newLowerRange[y] and higherValue<newHigherRange[y] and b:
                newLowerRange[y]=lowerValue
                b=False
            else:
                newLowerRange[y]
    if b==True:
        return True
    else:
        return False
    
def ammend(index):
    #Includes pop function
    global newHigherRange
    global newLowerRange
    lowerValue=newHigherRange[index]
    higherValue=newLowerRange[index]
    for i in range(len(newLowerRange)):
        

for i in range(len(lowerRange)):
    lowerValue=int(lowerRange[i])
    higherValue=int(higherRange[i])
    #iterate through original ranges
    if i == 0:
        newLowerRange.append(lowerValue)
        newHigherRange.append(higherValue)
    else:
        if ammendNewRange(lowerValue, higherValue):
            newLowerRange.append(lowerValue)
            newHigherRange.append(higherValue)
    print(newLowerRange)
    print(newHigherRange)
    #Now we need logic to go through the arrays and check if they are within eachother
        
    for i in range(len(newLowerRange)):
        lowerValue=newLowerRange[i]
        higherValue=newHigherRange[i]

        for y in range(len(newLowerRange)):
            if y!=i:
                ammendNewRange(lowerValue, higherValue)
        """
        Iterate through the new range items
        Say the first item
        skips itself and goes through the list
        if one of it's ranges are within the range
        it changes itself but pops that item

        """


"""
123-134
127-150

new range 123-150
"""


"""
This approach is too long, we need a less complex code to proccess the data quickly
We deal with huge ranges so the current method will take far to long
"""

"""
Have an idea what should be happening
Try identify where the code is going wrong

3-5
10-14
16-20
12-18

3-5
10-14
12-20
"""
