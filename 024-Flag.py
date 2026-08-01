#Topic: Lists

n = int(input())

a = list(map(int, input().split()))

flag = -1
for i in range(n):
    if a[i] == 4:
        flag += 1
        if flag == 1:
            print(i)
            break
else:
    print(-1)