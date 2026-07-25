#Topic: Loops

n = str(input( ))
count = 0
sum = 1

for j in n :
    count += 1
    if (count == 1) and (j == "a" or j == "i" or j == "e" or j == "o" or j == "u") :
        sum *= 2
    elif (count == 2) and (j == "a" or j == "i" or j == "e" or j == "o" or j == "u") :
        sum *= 2
    elif (count == 3) and (j == "a" or j == "i" or j == "e" or j == "o" or j == "u") :
        sum *= 2
    elif (count == 4) and (j == "a" or j == "i" or j == "e" or j == "o" or j == "u") :
        sum *= 2
    elif (count == 5) and (j == "a" or j == "i" or j == "e" or j == "o" or j == "u") :
        sum *= 2
    elif (count == 6) and (j == "a" or j == "i" or j == "e" or j == "o" or j == "u") :
        sum *= 2
    else:
        sum == 1
print(sum)