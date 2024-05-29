from fastapi import FastAPI, HTTPException, Request, Depends
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from sqlalchemy.orm import Session
from database import SessionLocal, engine
import models, schemas, crud
import uvicorn

app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.get("/", response_class=HTMLResponse)
async def read_root():
    return {"asdf"}
@app.post("/api/register", response_model=schemas.Place)
def register_place(place: schemas.PlaceCreate, db: Session = Depends(get_db)):
    db_place = crud.create_place(db=db, place=place)
    return db_place

@app.get("/api/data", response_model=list[schemas.Place])
def get_data(db: Session = Depends(get_db)):
    places = crud.get_places(db)
    return places
