#Topic: Lists

n, m = map(int, input().split())

a = []
for i in range(n):
        a.append(list(input()))

stars = 0
for i in range(n):
    for j in range(m):
        if a[i][j] == "*":
             stars += 1

print(stars)
	

