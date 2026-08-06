#Topic: Lists

x = list(input())

i = 0
while i < len(x):
    if x[i] == '=':
        x.pop(i)          
        if i > 0:         
            x.pop(i - 1)  
            i -= 1        
    else:
        i += 1

print("".join(x))