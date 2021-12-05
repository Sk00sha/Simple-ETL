from fastapi import FastAPI
from sqlalchemy.sql import schema
from database import SessionLocal,engine
from fastapi import Depends, FastAPI, HTTPException
from sqlalchemy.orm import Session
import models,schemas
from fastapi.middleware.cors import CORSMiddleware
from typing import List


models.Base.metadata.create_all(bind=engine)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
    allow_credentials=True,
)

@app.get("/")
def home():
    return {"Data":"Test"}

@app.get("/tests")
def tests(db:Session=Depends(get_db)):
    tests=db.query(models.Tests).all()
    return tests

@app.get("/hospitals")
def hospitals(db:Session=Depends(get_db)):
    hospitals=db.query(models.Hospitals).all()
    return hospitals

@app.get("/hospital_staff")
def hospital_staff(db:Session=Depends(get_db)):
    hospital_staff=db.query(models.HospitalStaff).all()
    return hospital_staff
