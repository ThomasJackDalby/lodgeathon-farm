from sqlmodel import Field, Session, SQLModel, create_engine, select

class PlantBase(SQLModel):
    id: int | None = Field(default=None, primary_key=True)
    type: str = Field()
    x: int = Field()
    y: int = Field()

class Plant(PlantBase, table=True):
    pass

class PlantCreate(PlantBase):
    pass