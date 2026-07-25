#Topic: Loops

n, k = map(int, input().split()) 
c = 1 
p = k % n + 1 

while p != 1:  
    p = (p + k) % n  
    c += 1 

print(c)