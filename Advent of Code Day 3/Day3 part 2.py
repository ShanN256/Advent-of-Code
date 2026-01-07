def getValue(line, num): #takes in the line being worked on and the number value, 12 being the 1st of the 12 digits
    global indexes #Enables indexes to be accessed and altered within the function
    value=0 #Stores the current max value in the given range iterated

    if num == 12: #If the value is the first value, we iterate through line starting from the first digit
        for i in range(0, len(line)-(num-1)):
            #len(line)-(num-1) , we limit the range of values we iterate through since there must be some digits left to be selected for our sequence
            #the range changes depending on the index of the digit we are finding for our sequence aswell as the index of the previously selected digit
            if int(line[i])>value:
                value=int(line[i])
                indexes[12-num]=i #storing the index of the first largest number
    else:  #If the value is not the first value, we iterate from the digit after the previous selected digit in our sequence
        for i in range(indexes[11-num]+1, len(line)-(num-1)):
            if int(line[i])>value:
                value=int(line[i])
                indexes[12-num]=i #storing the index of the next largest number

with open("Day3 Input.txt", "rt") as f:
    lines=f.readlines() #Creates an array list of the line in the input

count=0 #We count up all the values in this variable


for line in lines: #Iterates through each line
    line=line.strip() #Remove '/n'

    indexes=[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0] #The Sequence of indexes, Placeholder for the indexes of the largest numbers

    for i in range(12):
        getValue(line, 12-i)
    #Get the sequence of indexes of the line

    sequence=0

    for i in range(len(indexes)):
        sequence+=int(line[indexes[i]]+"0"*(len(indexes)-i-1))
    #Converts the sequence of indexes to digit format so it can be added 

    print(sequence)
    count+=sequence #Adds the sequences for each line together
print("Answer:", count)

"""
So we hav a line and 12 digits
first we look at the first couple digits leaving 11 digits remaining
Then starting from the digit after that we search for largest digit leaving 10 remaining at a minimum
Then starting from that digit we search for largest number leaving 9 remaining
"""
