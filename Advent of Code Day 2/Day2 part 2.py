with open("Day2 input.txt", "rt") as f:
    line=f.readline() 
    #Data is in one line so we just read the first line

IDs=line.split(",") #ID ranges are split with commas, this function splits the string input into an array of String ID ranges separated by ","

count=0 #We use variable to add up all the invalid ID values

for i in IDs:  #"2433423-342443"
    idRange=i.split("-")  #['5210718', '5346163']
    print(idRange)

    for i in range(int(idRange[0]), int(idRange[1])+1):

        value=str(i) #Convert to String

        
        b=0 #Checks if a sequence has already been detected

        #Logic to detect patterns in the value
        if value[0]*len(value)==value and len(value)>1:
            count+=i
            print(value)
            b=1

        if len(value)%2==0 and len(value)//2>1 and b==0:

            if value[0:2]*(len(value)//2) == value:
                count+=i
                b=1
                print(value)

        if len(value)%3==0 and len(value)//3>1 and b==0:

            if value[0:3]*(len(value)//3) == value:
                count+=i
                b=1
                print(value)
                
        
        if len(value)%4==0 and len(value)//4>1 and b==0:

            if value[0:4]*(len(value)//4) == value:
                count+=i
                b=1
                print(value)
        
        if len(value)%5==0 and len(value)//5>1 and b==0:

            if value[0:5]*(len(value)//5) == value:
                count+=i
                b=1
                print(value)
        
        
print("Answer:", count)

"""
Checks if the first number is repeated throughout the ID
Checks if divisiable by 2
Check if divisible by 3
Check if divisible by 4
Check if divisible by 5
"""
