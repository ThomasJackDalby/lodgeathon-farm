from sqlmodel import Field, SQLModel

class FarmerBase(SQLModel):
    name: str = Field()
    token: str = Field()
    x: int = Field(default=0)
    y: int = Field(default=0)

class Farmer(FarmerBase, table=True):
    id: int | None = Field(default=None, primary_key=True)

class FarmerCreate(FarmerBase):
    pass

class FarmerPublic(SQLModel):
    id: int
    name: str
    x : int
    y : int

class FarmerCommand(SQLModel):
    type: str

class MoveCommand(FarmerCommand):
    direction: str

class OtherCommand(FarmerCommand):
    stuff: str

class FarmerUpdate(SQLModel):
    token: str
    commands: list[MoveCommand | OtherCommand]