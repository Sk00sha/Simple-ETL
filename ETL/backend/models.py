from sqlalchemy import Boolean, Column, ForeignKey, Integer, String,REAL
from sqlalchemy.orm import relationship
from sqlalchemy.sql.sqltypes import Float

from database import Base

class Tests(Base):
    __tablename__ = 'TESTS'
  
    id = Column(Integer, primary_key=True, index=True)
    positivity_rate = Column(Float)
    date_updated = Column(String)
    positive = Column(Integer)
    negative = Column(Integer)

class Region(Base):
    __tablename__ = "REGION"
  
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String)
    code = Column(String)
    abbreviation = Column(String)



class Hospitals(Base):
    __tablename__ = "Hospitals"
    id = Column(Integer, primary_key=True, index=True)
    region_id =  Column(Integer, ForeignKey("REGION.id"))
    free_all = Column(Integer)
    occupied_jis_covid = Column(Integer)
    occupied_oaim_covid = Column(Integer)
    occupied_o2_covid = Column(Integer)
    occupied_other_covid = Column(Integer)
    updated_at= Column(String)


class HospitalStaff(Base):
    __tablename__ = "HOSPITAL_STAFF"
    id = Column(Integer, primary_key=True, index=True)
    hospital_id = region_id =  Column(Integer, ForeignKey("Hospitals.id"))
    oow_doctors = Column(Integer)
    oow_nurses = Column(Integer)
    oow_other = Column(Integer)

   