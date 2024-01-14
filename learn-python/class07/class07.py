

print("line1")
print("line2")
if 2==3: 
    print("line3")
    print("line10")
    if 5 == 2: 
        print("nested if")
    elif 5 == 5: 
        print("nested else if")
        
elif 5 == 5:
    print("elif")
else: 
    print("else line")
def printSomething():
    print("line4")
    if 2 == 2:
      print("line5")


n = int(input("Enter week day number"))

if n == 1: 
    print("Monday")
elif n == 2:
    print("Tuesday")
elif n == 3:
    print("Wednesday")
elif n == 4:
    print("Thursday")
elif n == 5:
    print("Friday")
elif n == 6:
    print("Saturday")
elif n==7:
    print("Sunday")
else: 
    print("not a vaild number")

match n:
    case 1:
        print("Monday")
    case 2:
        print("Tuesday")
    case 3:
        print("Wednesday")
    case 4:
        print("Thursday")
    case 5:
        print("Friday")
    case 6:
        print("Saturday")
    case 7:
        print("Sunday")
        

     

day = input("Enter week day")
match day:
    case "Monday":
        print(1)
    case "Tuseday":
        print(2)
    case _:
        print("default value")