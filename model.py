from sqlmodel import Field, SQLModel, create_engine

class Hero(SQLModel,table = True):
    id : int | None = Field(default=None,primary_key=True)
    name : str
    secret_name : str
    age  : int | None = None



engine = create_engine("postgresql+psycopg2://postgres:newpassword@localhost:5432/mydatabase")


SQLModel.metadata.create_all(engine)