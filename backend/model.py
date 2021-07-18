# pydantic allows for auto creation of JSON schemas from models
from pydantic import BaseModel


class Todo(BaseModel):
    title: str
    description: str
