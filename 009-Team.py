#Topic: Conditional Statements

a1 = int(input())
b1 = int(input())
a2 = int(input())
b2 = int(input())
a3 = int(input())
b3 = int(input())

if a1 >= b1 :
    n = b1
else :
    n = a1 
if a2 >= b2 :
    m = b2
else :
    m = a2
if a3 >= b3 :
    o = b3
else :
    o = a3
    
print(n + m + o)