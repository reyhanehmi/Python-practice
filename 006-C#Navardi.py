#Topic: Conditional Statements

n = int(input())
m = int(input())

if (n == 1 or n == 4) and (m == 2 or m == 3) :
    print(1)
elif ((n == 1) and (m == 4)) or ((n == 4) and (m == 1)) :
    print(2)
elif (n == 2 or n == 3) and (m == 1 or m ==4) :
    print(1)
elif ((n == 2) and (m == 3)) or ((n == 3) and (m == 2)) :
    print(2)
else :
    print(0)