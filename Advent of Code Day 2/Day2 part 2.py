with open("Day2 Test Input.txt", "rt") as f:
    line=f.readline()

IDs=line.split(",")

count=0
for i in IDs: #"2433423-342443"
    idRange=i.split("-")

    for i in range(int(idRange[0]), int(idRange[1])+1):

        value=str(i) #Convert to String

        #Logic to detect patterns in the value
        b=0

        if value[0]*len(value)==value:
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
Checks if the first number is repeated
Checks if length is divisible by two and sees if two halves are equal
Say 6 length then you can have sets of 3 also
Check if divisible by 3
Check if divisible by 4
Check if divisible by 5
"""

#That logic allows for length of 3 times 1 equal to value