#Topic: Conditional Statements

r, c = map(int,input().split())
m = 0
n = 0

if c <= 10 :
    m = 11 - r
    n = 11 - c
    print(f'Right {m} {n}')
else :
    m = 11 - r
    n = -(9 - c)
    print(f'Left {m} {n}')