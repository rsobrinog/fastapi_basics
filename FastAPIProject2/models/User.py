from sqlmodel import SQLModel, Field

class User(SQLModel, table=True):
    id: int | None =  Field(default=None, primary_key=True)
    name: str
    lastname: str
    age:int
    passwd: str

class UserRequest(SQLModel):
    name: str
    lastname: str
    age: int
    passwd: str

class UserResponse(SQLModel):
    id: int
    name: str
    lastname: str
    age: int


