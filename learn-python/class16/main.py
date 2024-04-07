from typing import Union

from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}













# user = {}
# num1 = input("enter number1")
# num2 = input("enter number2")
# try: 
#     print("try block")
#     try:
#         sum = num1/num2
#     except Exception as e:
#         print("error")

# except Exception as e:
#     print( e)

# else: 
#     print("it will run if there is no error in try block")
    
# finally: 
#     print("it will run all the times")


# try:
#     file.download
# except ValueError as e:
    
#     print( e)
# except Exception as e:
#     print( e)
# else:
#     print("it will run")
# finally: 
#     print("it will run all the times")
# print("normal rest of code")