y=0
w=50
count=0
z=0
with open("input.txt", "rt") as f:
    #Find the length of the file
    for x in f:
        y+=1
    f.seek(0)

    #Iterate through file until 2nd last
    for i in range(y):
        if i==y-1:
            x=f.readline() + " "
        else:
            x=f.readline()
            996
        #Gets the numerical value for each command
        if (len(x)-1) == 5:
            if x[0] == "L":
                z=(int(x[1])*1000 + int(x[2])*100 + int(x[3])*10 + int(x[4])) - (int(x[1])*1000 + int(x[2])*100 + int(x[3])*10 + int(x[4]))*2
            else:
                z=int(x[1])*1000 + int(x[2])*100 + int(x[3])*10 + int(x[4])
        elif (len(x)-1) == 4:
            if x[0] == "L":
                z=(int(x[1])*100 + int(x[2])*10 + int(x[3])) - (int(x[1])*100 + int(x[2])*10 + int(x[3]))*2
            else:
                z=int(x[1])*100 + int(x[2])*10 + int(x[3])
        elif (len(x)-1) == 3:
            if x[0] == "L":
                z=(int(x[1])*10 + int(x[2]))-(int(x[1])*10 + int(x[2]))*2
            else:
                z=int(x[1])*10 + int(x[2])
        elif (len(x)-1) == 2:
            if x[0] == "L":
                z=int(x[1])-int(x[1])*2
            else:
                z=int(x[1])
        else:
            print("Unrecognised Input");

        #Count how many times lock goes to 0
        #lock goes to zero by landing on it or passing it

        #if the lock is already at zero and it transitions, we should not increase count
        x=w
        w+=z
        b=0
        if w < 0:
            numCount=0
            while w<0:
                w+=100
                b=1
                numCount+=1
                if numCount==1 and x!=0:
                    count+=1
                elif numCount>1:
                    count+=1
        elif w>99:
            numCount=0
            while w>99:
                w-=100
                b=1
                numCount+=1
                if numCount==1 and x!=0:
                    count+=1
                elif numCount>1:
                    count+=1
        else:
            w+=0

        if w==0 and b==0:
            count+=1

        print("Value:", z, "Lock:", w, "Count:", count)
    print("\nThe answer is", count)