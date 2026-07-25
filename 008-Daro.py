#Topic: Conditional Statements

n = int(input()) #mobtalaian shekar
k = int(input()) #fotiha shekar
p = int(input()) #mobtalaian namak
q = int(input()) #fotiha namak

if (n - k) > (p - q) :
    print('Shekarestan')
elif (p - q) > (n - k) :
    print('Namakestan')
else :
    print('Equal')