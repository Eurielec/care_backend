from glob import glob
from typing import List
from typing import Optional
import json
import random

from dataclasses import dataclass
from datetime import datetime
from fastapi import FastAPI

DATA_PATH = "data/"

app = FastAPI()


@dataclass
class EKG:
    """Class for an EKG."""

    user: str
    date: datetime
    heart_rate: int
    raw_signal: List[float]


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/random")
def get_random():
    with open(random.choice(glob(DATA_PATH + "*.json"))) as f:
        j = json.load(f)

    return j


@app.get("/items/{item_id}")
def read_item(item_id: int, q: Optional[str] = None):
    return {"item_id": item_id, "q": q}
