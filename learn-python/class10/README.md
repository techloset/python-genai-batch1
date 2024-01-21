# Class Topics

## Python - loops
```
list = [2,30,30,50]
for i in list:
    print(i)


list = [2,30,30,50]
for i,item in enumerate(list, start=10):
    print(f"{i},{item}")


    for i in range(1,10,2):
    for j in range(1,10,2):
        print(i,j)

list3 = [2,30,30,50]
list2 = [203,3023,3023,32450]
def sumCal(i):
    print(i)
    return i * 2
output = list(filter(sumCal, list3))
print(output)
```
