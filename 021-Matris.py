#Topic: Lists

n, m = map(int, input().split())

a = []
for i in range(n):
    a.append(list(map(int, input().split())))

b = []
for i in range(n):
    b.append(list(map(int, input().split())))

c = []
for i in range(n):
    for j in range(m):
        c = a[i][j] + b[i][j]
        print(c, end = " ")
    print()