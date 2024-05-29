from sqlalchemy.orm import Session
import models, schemas

def get_places(db: Session):
    return db.query(models.Place).all()

def create_place(db: Session, place: schemas.PlaceCreate):
    db_place = models.Place(**place.dict())
    db.add(db_place)
    db.commit()
    db.refresh(db_place)
    return db_place
