car = "red 2342 324 honda 4"

car = ["red" , 23432, 24, 4, "honda", "civic"]

car[2]

car = {
     "color": "red",
    "price": 324234,
    "numberOfDoors": 4,
    "company": "honda",
    "model": "civic 2023",
    "info":{
        "address":"sdf",
        "city": "fsd",
    }
}

listOfCars = [{
     "color": "red",
    "price": 324234,
    "numberOfDoors": 4,
},
              {
     "color": "red",
    "price": 324234,
    "numberOfDoors": 4,
},
              {
     "color": "red",
    "price": 324234,
    "numberOfDoors": 4,
}
              ]
# dictionary data read
price = car["price"]
print(price)
color = car.get("color",{})
# dictionary data update
car["price"] = 500

# dictionary data add
car["engineCC"] = "1200cc"
print(car)


# dictionary data delete
del car["engineCC"] 
car.pop("color",{})
car.popitem()
print(car)
















userName = "Naveed Sarwar"
userName1 = "Ali"
userName2 = "Zain"
userName3 = "Abu bakar"
userNames = ["Naveed", "Zain", "Abu"]
car = "Black 234234 4 tanksize 234"
car = ["color","Black",2342, 4, 234]
nums= [10,20,30,40,50]

car = {
    "color": "black",
    "price": 234234,
    "numberOfSeats": 4,
    "numOfDoors": 4,
    "type": "auto",
    "isNew": True,
}
# how to read data from dictionary
getValue = car.get("price")
getValue = car["color"]
# how to add to dictionary
car["engineCC"] = 1200

# how to update to dictionary
car["engineCC"] = 1800

# how to delete from dictionary
del car["engineCC"]
car.pop("price")
car.popitem()


# loop
# .values
# .keys
# print("Car price: ", car)


























# create student app in python, 
# default 5 students entities should be there in list by default
# add new student 
# update any student
# delete any student
# show all student's emails and id's
# students = [{
#     "id": 1,
#     "name": "Naveed",
#     "email":"student1@gmail.com",
#     "rollNo": 2344,
#     "class": "WMA"
# },
# {
#     "id": 2,
#     "name": "Ali",
#     "email":"student2@gmail.com",
#     "rollNo": 9234,
#     "class": "Python development"
# },
# {
#     "id": 3,
#     "name": "Zain",
#     "email":"student3@gmail.com",
#     "rollNo": 8352,
#     "class": "WMA"
# },
# {
#     "id": 4,
#     "name": "Umar",
#     "email":"student4@gmail.com",
#     "rollNo": 9234,
#     "class": "Nextjs"
# },
# {
#     "id": 5,
#     "name": "Mudasir",
#     "email":"student5@gmail.com",
#     "rollNo": 2342,
#     "class": "Python development"
# }

#             ]
# email = input("Please enter new student email address: ")
# newStudent = {
#     "id": len(students)+1,
#     "name": "Mudasir",
#     "email":email,
#     "rollNo": 2342,
#     "class": "Python development"
# }
# students.append(newStudent)

# for student in students:
#     print("Student Email: " + student["email"], "Id: ", student["id"])

# update_id = int(input("Enter the id of student you want to update: "))
# updatedEmail = input("Please enter the updated email of student you want to update: ")

# def updateStudent(student):
#     if student["id"] == update_id:
#         return {
#             "id": student["id"],
#             "name":student["name"],
#             "email":updatedEmail,
#             "rollNo": student["rollNo"],
#             "class": student["class"]
#         }
#     else:
#         return student

# # update requrired student
# students = list(map(updateStudent, students))
# print("students",students)

# # delete requrired student
# id = int(input("Enter the id of student you want to delete: "))
# def deleteStudent(student):
#     print(student)
#     if student["id"] != id:
#         return student
    
# students = list(filter(deleteStudent, students))

# # show all student's emails and id's

# for student in students:
#     print("Student Email: " + student["email"], "Id: ", student["id"])


# students = list(filter(lambda student: student['id'] != id, students))


# laptop = {}
# laptop["color"]  = input("Enter color of lapopt")



# laptop = {
#     "company":"dell",
#     "price":234234,
#     "generation":"2nd",
#     "ram":32,
#     "storage":500,
#     "size":15
# }
# laptop["color"] = "black"
# laptop["model"] = "1235",
# laptop["color"] = "red"
# del laptop["color"]
# print("laptop color", laptop["color"])



# car = {
#     "color":"red",
#     "price": 234234,
#     "engineCC": "1200cc",
#     "isNew": True,
#     "anything": None,
#     "seatHeights":[30,40,50,20],
     
# }

# result = car["seatHeights"]

# print("car",result[0])

# student = {
#     "name": "Ali",
#     "email": "student@gmail.com",
#     "rollNo": "1",
#     "age": 18,
#     "class": "WMA",
#     "cnic":234234234,
    
# }
# print("student",student["cnic"])

# message =  {
#     "text": "Hello, Sir"
# }

# post = {
#     "title": "Hello Frields",
#     "caption": "lrore",
#     "meda": "url",
#     "postAt": "10/11/123",
#     "postTime": "23:234:234",
#     "comments": [],
#     "likesCount": 234,
#     "shareCount": 13,
# }
# order = {
#     "total": 23423,
#     "isDelivered": True,
#     "time": "23:324:21",
#     "type": "dining",
#     "menu": ["piza", "pasta", "showarma","burger"],
#     "customer": {
#         "address":"sdf",
#         "name": "Naveed",
#         "paymentMethod": "cash"
#     }
# }
# output = order["customer"]
# print("total", order["paymentMethod"])



# order1 = {
#     "total": 9234,
#     "isDelivered": True,
#     "time": "23:324:21",
#     "type": "dining",
#     "menu": ["piza", "pasta", "showarma","burger"],
#     "customer": {
#         "address":"sdf",
#         "name": "Naveed",
#         "paymentMethod": "cash"
#     }
# }

# order2 = {
#     "total": 24,
#     "isDelivered": True,
#     "time": "23:324:21",
#     "type": "dining",
#     "menu": ["piza", "pasta", "showarma","burger"],
#     "customer": {
#         "address":"sdf",
#         "name": "Naveed",
#         "paymentMethod": "cash"
#     }
# }

# orders = [{
#     "total": 23423,
#     "isDelivered": True,
#     "time": "23:324:21",
#     "type": "dining",
#     "menu": ["piza", "pasta", "showarma","burger"],
#     "customer": {
#         "address":"sdf",
#         "name": "Naveed",
#         "paymentMethod": "cash"
#     }
# }, {
#     "total": 90234,
#     "isDelivered": True,
#     "time": "23:324:21",
#     "type": "dining",
#     "menu": ["piza", "pasta", "showarma","burger"],
#     "customer": {
#         "address":"sdf",
#         "name": "Naveed",
#         "paymentMethod": "cash"
#     }
# }, {
#     "total": 234,
#     "isDelivered": True,
#     "time": "23:324:21",
#     "type": "dining",
#     "menu": ["piza", "pasta", "showarma","burger"],
#     "customer": {
#         "address":"sdf",
#         "name": "Naveed",
#         "paymentMethod": "cash"
#     }
# }]

# carList = [10,20]
# userName = "Naveed"
# carColor = "red"
# carSpeed= 130
# numberOfDoors = 4

# car = ["carColor","red", 130, 4]
# nums = [10,20,30,40,50,60]

