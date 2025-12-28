y=0
z=0
w=50
count=0

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

        #Gets the numerical value for each command
        if (len(x)-1) == 4:
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
        
        #Updating lock value
        w+=z
        if w < 0:
            while w<0:
                w+=100
        elif w>99:
            while w>99:
                w-=100
        else:
            w+=0
            
        print("Value:", z, "Lock:", w)
        
        if w == 0:
            count+=1
        else:
            count+=0
            
    print("\nThe answer is: ", count)     