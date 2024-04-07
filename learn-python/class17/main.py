from fastapi import FastAPI
from typing import Union

app = FastAPI()

total = 10

def process_items(prices: Union[int, str]):
    for item_name, item_price in prices.items():
        print(item_name)
        print(item_price)

@app.get("/items/")
async def read_item(skip: int = 0, limit: int = 10):
    process_items([10,22])
    
    return total