from models import Booking
from db_sqlite import db



def create_booking(phone,email,date,time):
    db_booking = Booking(date=date, time=time, phone=phone, email=email)
    db.add(db_booking)
    db.commit()
    db.refresh(db_booking)
    return db_booking 
