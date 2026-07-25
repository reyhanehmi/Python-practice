#Topic: Loops

t = int(input())

for i in range(1, t + 1):
    x, y = map(int,input().split())
    if x % 2 == 0: 
        time = (x + y)
    elif x % 2 == 1:
        time = (x + y) - 1
        
    if (x == y) or (x - y == 2):
        print(time)
    else :
        print(-1)
        
        
#((x + y) % 2 == 0) and (x >= y)
