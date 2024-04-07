from fastapi import FastAPI
import uvicorn

app = FastAPI()

students:list[dict] = [{
    "id":"123324",
    "name":"Naveed Sarwar",
    "email":"naveed@techloset.com",
    "address":"Fsd",
    "rollNumber":2342,
},
            {
    "id":"9234",
    "name":"Umair",
    "email":"umair@techloset.com",
    "address":"Fsd",
    "rollNumber":9123,
}
            ]


@app.get("/students")
def students_list():
    return students

currentId = 0
def filterRecord(student:dict | None):
    if currentId == student["id"]:
        return True
    else:
        return False

@app.get("/students/{id}")
def students_list_single(id):
    studentsList = list(filter(filterRecord,students))
    return studentsList

@app.put("/students/{id}")
def students_update(id):
    global students
    students = list(map(lambda item:item["id"] == id if {"id":"s","abc":"sdf"} else item ,students))


@app.get("/test")
def RouteHandler():
    return "api is working fine"

def start():
    uvicorn.run("api.main:app",host="127.0.0.1", port=8080, reload=True)
    
    
def production():
    uvicorn.run("api.main:app",host="0.0.0.0", port=80)