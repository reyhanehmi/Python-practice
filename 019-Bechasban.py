n, k = map(int,input().split())

for a in map(int,input().split()) :
    if a > k :
        print('YES')
        break
    
else :
    print('NO')