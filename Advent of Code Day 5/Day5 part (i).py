#Objective: process ranges and see whether values are within the range

with open("Day5 Input.txt", "rt") as f:
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

print("Lower Range:", lowerRange)
print("Upper Range:", higherRange)

print("Nuber or Ranges:", len(lowerRange)) 
print("Number Values:", len(lines)-(index+1)) #Index + 1 to account for the gap

answer=0

#Checks if a value is in any of the ranges
for x in range(index+1, len(lines)): #Iterates through the values
    value=int(lines[x])
    notChecked=True #Has the value been marked as 'fresh' already or is found in one of the ranges?
    for i in range(len(lowerRange)): #Iterates through all the ranges
        if notChecked and (value >= int(lowerRange[i])) and (value <= int(higherRange[i])):
                answer+=1
                notChecked=False

print("Answer:", answer)
                                 
