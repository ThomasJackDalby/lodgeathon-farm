import random
from rich import traceback, print
traceback.install()
from fastapi import FastAPI
from sqlmodel import Field, Session, SQLModel, create_engine, select
from sqlmodel.pool import StaticPool

from farmers import Farmer, FarmerPublic, FarmerCreate, FarmerUpdate, MoveCommand, DigCommand
from plants import Plant

sqlite_file_name = "database.db"
# sqlite_url = f"sqlite:///{sqlite_file_name}"
sqlite_url = f"sqlite://"

app = FastAPI()
engine = create_engine(sqlite_url, connect_args={"check_same_thread": False}, poolclass=StaticPool)

def create_db_and_tables():
    SQLModel.metadata.create_all(engine)

@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.on_event("startup")
def on_startup():
    create_db_and_tables()

    with Session(engine) as session:

        for farmer_name in ["Matt", "Tom"]:
            farmer = Farmer(name=farmer_name, token="abcde", x=0, y=0)
            session.add(farmer)
            session.commit()
            session.refresh(farmer)

        for _ in range(100):
            x = random.randint(0, 64)
            y = random.randint(0, 32)
            plant = Plant(type="carrot", x=x, y=y)
            session.add(plant)
            session.commit()
            session.refresh(plant)

@app.post("/farmers/", response_model=FarmerPublic)
def post_farmers(farmer: FarmerCreate):
    with Session(engine) as session:
        farmer.x = 0
        farmer.y = 0
        db_farmer = Farmer.model_validate(farmer)
        session.add(db_farmer)
        session.commit()
        session.refresh(db_farmer)
        return db_farmer
    
@app.post("/farmers/{farmer_id}")
def post_farmer(farmer_id: int, farmer_update: FarmerUpdate):
    with Session(engine) as session:
        farmer = session.exec(select(Farmer).where(Farmer.id == farmer_id)).one()

        for command in farmer_update.commands:
            if command.type == "move": command = MoveCommand.model_validate(command)
            elif command.type == "dig": command = DigCommand.model_validate(command)

            print("ACTION")
            command.action(farmer)

            session.add(farmer)
            session.commit()

@app.get("/farmers/", response_model=list[FarmerPublic])
def get_farmers():
    with Session(engine) as session:
        return session.exec(select(Farmer)).all()
    
@app.get("/farmers/{farmer_id}", response_model=FarmerPublic)
def get_farmers(farmer_id: int):
    with Session(engine) as session:
        return session.exec(select(Farmer).where(Farmer.id == farmer_id)).first()
    
@app.get("/plants/", response_model=list[Plant])
def get_plants():
    with Session(engine) as session:
        return session.exec(select(Plant)).all()
