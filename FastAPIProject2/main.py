from fastapi import FastAPI, Depends
from dotenv import load_dotenv
from sqlmodel import create_engine, Session, SQLModel
from .models.User import User, UserRequest, UserResponse
from sqlmodel import select
import os
app = FastAPI()


load_dotenv()

DATABASE_URL= os.getenv("DATABASE_URL")
engine = create_engine(DATABASE_URL)

SQLModel.metadata.create_all(engine)

def get_db():
    db = Session(engine)
    try:
        yield db
    finally:
        db.close()

@app.post("/user", response_model=dict, tags=["CREATE"])
def addUser(user: UserRequest,db:Session = Depends(get_db)):
    #Convertir les dades del client a un model compatible amb la taula User
    insert_user = User.model_validate(user)
    db.add(insert_user)
    db.commit()
    return {"msg":"Afegit usuari correctament"}


@app.get("/user/{id}", response_model=UserResponse, tags=["READ by ID"])
def getUser(id: int, db:Session = Depends(get_db)):
    # Amb els statments de sqlalchemy es crea la consulta i es guarda a stmt
    stmt = select(User).where(User.id == id)
    result = db.exec(stmt).first()
    return UserResponse.model_validate(result)

'''
class User(BaseModel):
    name: str
    lastname: str
    age: int

@app.post("/user", response_model=User)
def addName(user:User, db:Session=Depends(get_db)):
    user_db = User(**user.dict())

    return user
'''








