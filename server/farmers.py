from sqlmodel import Field, Session, SQLModel, create_engine, select

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