with open("Day3 Input.txt", "rt") as f:
    lines=f.readlines() #Creates an array list of the line in the input

count=0 #We count up all the values in this variable

for line in lines: #Iterates through each line
    value=0 #Placeholder for the maximum value in a line
    line=str(int(line)) #Remove '/n'
    indexes=[0, 0]

    #Get first largest number
    #This number cannot be the last number
    for i in range(len(line)-1):
        if int(line[i])>value:
            value=int(line[i])
            indexes[0]=i #storing the index of the first largest number

    #Get second largest number that is after the first largest number
    value=0 #Re-using placeholder for max value
    for i in range(indexes[0]+1, len(line)):
        if int(line[i])>value:
            value=int(line[i])
            indexes[i]=i #Storing the index of the largest number after the index of the previous largest number

    print("Line:", line, "Index:", indexes, "Value:", int(line[min(indexes)])*10 + int(line[max(indexes)]))

    count+=int(line[min(indexes)])*10 + int(line[max(indexes)])

print("Answer:", count)

"""
#Indexing issue, i was going back and getting the index of a "value" not the "value", not the specific one i am looking at that moment
line.index(line[i])
line[i] could be "5"
but when we call line.index("5"), it returns the index of the first "5" rather than the one at our required index
So I used the i in the for loop that was already iterating through the index values of the 'line'
"""