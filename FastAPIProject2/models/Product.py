from sqlmodel import SQLModel, Field

class Product(SQLModel, table=True):
    id = Field(default=None, primary_key=True)
    name = str
    description = str
    price = int
    tax = int
