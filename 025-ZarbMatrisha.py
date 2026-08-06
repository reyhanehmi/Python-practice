#Topic: Lists

a, b, c = map(int, input().split())

n = list()
m = list()
x = list()

for i in range(a):
    n.append(list(map(int, input().split())))

for i in range(b):
    m.append(list(map(int, input().split())))

for i in range(a):
    row = []
    for j in range(c):
        sum = 0
        for k in range(b):
            sum += (n[i][k] * m[k][j])
        row.append(sum)
    x.append(row)

for row in x:
    print(*row)
