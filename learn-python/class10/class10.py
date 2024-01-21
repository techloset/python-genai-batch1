
nums = [10,11,30,13,50,19,70,80]
def multi(item):
    return item 
newList = list(filter(multi, nums))
print(newList)


# def multi(item):
#     if item % 2 == 0:
#       return item * 2
#     else:
#         return item
# newList = list(map(multi, nums))
# print(newList)

# userNames = ["Naveed", "john", "Alice", "Ali", "Umar", "Umair"]
# def changeUserNames(item):
#     print(item)
#     return f"Hello {item}"
# newNames = list(map(changeUserNames,userNames))

# print(newNames)  

# for index, item in  enumerate(userNames):
#     print("loop runing", item, index)
#     if item == "Ali":
#         print("Search is found", item ,index ) 
#         break

# for item in  range(0, len(userNames)):
#     print("loop runing", item)
#     if userNames[item] == "Ali":
#         print("Search is found", userNames[item] ,item ) 
#         break
    

# nums = [10,20,30,40,50,60,70,80]
# i = 0
# while i < len(nums):
#     print ("Hello world - while", nums[i])
#     i = i + 1
# write a search program, search the name ali from the list userName if ali found please stop the loop, print ali

    
# output  = list(range(10,50,2))
# print("output",output)

# for j in range(0,10,4):
#     print("for loop range j", j)