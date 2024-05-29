from pydantic import BaseModel

class PlaceBase(BaseModel):
    address: str
    placename: str
    placetype: str

class PlaceCreate(PlaceBase):
    pass

class Place(PlaceBase):
    id: int

    class Config:
        orm_mode = True
