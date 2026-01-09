#Objective: process ranges and see whether values are within the range
#This can be done precisely or quickly

with open("testInput.txt", "rt") as f:
    lines=f.readlines() #Creates an array list of the rows in the input

#index of the gap between ranges and values
index=0
for i in range(len(lines)):
    if lines[i].strip()=="":
        index=i

range1=[]
range2=[]

for i in range(index):
    range1.append(lines[i].strip().split("-")[0])
    range2.append(lines[i].strip().split("-")[1])

print("Lower Range:", range1)
print("Upper Range:", range2)

print("Nuber or Ranges:", len(range1)) 
print("Number Values:", len(lines)-(index+1)) #Index + 1 to account for the gap

answer=0

for x in range(index+1, len(lines)):
    value=int(lines[x].strip())
    b=0
    if b==0:
        for i in range(len(range1)):
            print(range1[i], "-", range2[i])
            for y in range(int(range1[i]), int(range2[i])+1):
                if value==y:
                    answer+=1
                    b=1
                    print("Success  ")
print(answer)

"""
for i in range (index + 1, len(lines)):
    value=int(lines[i])
    print("\n", value)
    for y in range(len(range1)):
        lowerRange=int(range1[y])
        upperRange=int(range2[y])
        if (value-lowerRange)>=0: #If value is past lower Range
            if (value-lowerRange) <= upperRange-lowerRange and b==0:
                answer+=1
                b=1

print("Answer:", answer)
"""
                                 
