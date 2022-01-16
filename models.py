from db_sqlite import Base
from sqlalchemy import Column, Integer, String



class Booking(Base):
    __tablename__ = 'Bookings'
    
    id = Column(Integer, primary_key=True)
    phone = Column(Integer)
    email = Column(String)
    date  = Column(String)
    time = Column(String)
    
    class Config:
        orm_mode = True
    