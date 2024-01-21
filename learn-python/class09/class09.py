i = 0
inputList = [10,20,19, 18,30,40,50,255, 333]
evenSum = 0
oddSum = 0
print("before while")
while i < len(inputList):
    if inputList[i] % 2 == 0:
        evenSum = evenSum + inputList[i]
    else:
        oddSum = oddSum + inputList[i]
    i += 1
print("even",evenSum, "odd", oddSum )