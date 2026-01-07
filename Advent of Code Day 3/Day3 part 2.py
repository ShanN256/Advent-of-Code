def getValue(line, num): #number of the value, say the 12th digit, line, return index
    global indexes
    value=0
    #we want the value of the index before it

    if num == 12: #If the value is the first value, we start from zero
        for i in range(0, len(line)-(num-1)):
            if int(line[i])>value:
                value=int(line[i])
                indexes[12-num]=i #storing the index of the first largest number
    else: 
        for i in range(indexes[11-num]+1, len(line)-(num-1)):
            if int(line[i])>value:
                value=int(line[i])
                indexes[12-num]=i #storing the index of the first largest number

with open("Day3 Input.txt", "rt") as f:
    lines=f.readlines() #Creates an array list of the line in the input

count=0 #We count up all the values in this variable


for line in lines: #Iterates through each line
    line=line.strip() #Remove '/n'

    indexes=[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0] #Placeholder for the indexes of the largest numbers

    for i in range(12):
        getValue(line, 12-i)

    something=0

    for i in range(len(indexes)):
        something+=int(line[indexes[i]]+"0"*(len(indexes)-i-1))

    print(something)
    count+=something
print("Answer:", count)

"""
So we hav a line and 12 digits
first we look at the first couple digits leaving 11 digits remaining
Then starting from the digit after that we search for largest digit leaving 10 remaining at a minimum
Then starting from that digit we search for larges leaving 9 remainging

we are having indexing issues
"""