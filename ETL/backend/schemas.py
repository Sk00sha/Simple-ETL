from pydantic import BaseModel


class Test(BaseModel):
    id:int
    positivity_rate:float
    date_updated:str
    positive:int
    negative:int

    class Config:
        orm_mode = True