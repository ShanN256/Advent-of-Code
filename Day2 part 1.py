with open("Day2 input.txt", "rt") as f:
    line=f.readline()

IDs=line.split(",")

count=0
for i in IDs: #"2433423-342443"
    now=i.split("-")

    for i in range(int(now[0]), int(now[1])+1):

        value=str(i) #Convert to String

        if len(value)%2==0: #If even

            halfWay=len(value)//2
            part1=value[0:halfWay]
            part2=value[halfWay:halfWay*2]

            if part1==part2:
                count+=i
                print(value)
        
print("Answer:", count)