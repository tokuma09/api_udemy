from typing import List, Optional

from fastapi import FastAPI
from pydantic import BaseModel, Field

# Create a FastAPI instance
app = FastAPI()


# データモデルの定義


class ShopInfo(BaseModel):
    name: str
    location: str


class Item(BaseModel):
    name: str = Field(min_length=4, max_length=12)
    description: Optional[str] = None
    price: float
    tax: Optional[float] = None


class Data(BaseModel):
    shop_info: Optional[ShopInfo] = None
    items: List[Item]


@app.post(path="/")
async def index(data: Data):
    return {"data:": data}


# fstringでなく{}で囲むとパスパラメータとなる
@app.get(path="/countries")
# パスパラメータになってない引数はクエリパラメータになる
async def country(country_name: Optional[str] = None, country_no: Optional[int] = None):
    return {"country_name": country_name, "country_no": country_no}
