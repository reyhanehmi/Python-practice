#Topic: Conditional Statements

a, b, c, d, e, f = map(int,input().split())
#a, b, c baray zarf
#d, e, f baray yakh

if (a >= d) and (b >= e) :
    print('zende mimuni')
elif (a >= d) and (b >= f) :
    print('zende mimuni')
elif (a >= e) and (b >= d) :
    print('zende mimuni')
elif (a >= e) and (b >= f) :
    print('zende mimuni')
elif (a >= f) and (b >= e) :
    print('zende mimuni')
elif (a >= f) and (b >= d) :
    print('zende mimuni')
else :
    print('dari mimiri')