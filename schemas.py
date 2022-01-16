from pydantic import BaseModel

class BookingResponse(BaseModel):
    phone: str
    email: str
    date : str


    
     
    

   