#Topic: Conditional Statements

w1, w2, w3, w4, w5 = map(int,input().split())

if max(w1, w2, w3, w4, w5) == w1 :
    print(1)
elif max(w1, w2, w3, w4, w5) == w2 :
    print(2)
elif max(w1, w2, w3, w4, w5) == w3 :
    print(3)
elif max(w1, w2, w3, w4, w5) == w4 :
    print(4)
elif max(w1, w2, w3, w4, w5) == w5 :
    print(5)