#Topic: Lists

n = int(input())

names = []
for i in range(n):
        names.append(list(input()))

num = 0
for i in range(n):
    Letters = []
    for x in names[i]:
        if x not in Letters:
            Letters.append(x)
            if num < len(Letters):
                num = len(Letters)


print(Letters)
print(num)
          