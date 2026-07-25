#Topic: Loops

n = int(input())
x = 0
y = 0
y1 = 1

for i in range (1, n, 4) :
    if n == 1 :
        x == 0
        y == 0
    elif n == 2 :
        x == 1
        y == 0
    elif n % 4 == 1 :
        x -= 1
        y -= 1
    elif n % 4 == 2 :
        x += 1
        y1 -= 1
        y = y1
    elif n % 4 == 3 :
        x += 1
        y += 1
    elif n % 4 == 0 :
        x -= 1
        y += 1
print(x, y)