#Topic: Functions

n = int(input())

def sum(a):
    sum1 = 0
    while a > 0 :
        sum1 += a % 10
        a //= 10
    return sum1


def is_prime(n):
    if n <= 1:
        return 0
    for j in range(2, n):
        if n % j == 0:
            return 0
    return 1


count = 0
num = n + 1
while count != sum(n):
    if is_prime(num) == 1:
        count += 1
        if count == sum(n):
            print(num)
    num += 1

