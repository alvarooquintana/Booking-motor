from fastapi import FastAPI,Request,Form
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles


from db_sqlite import engine
from models import Base
from crud import create_booking

app = FastAPI()
# Creamos tablas con esto : 
Base.metadata.create_all(bind=engine)

app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")

@app.get("/booking" , response_class=HTMLResponse)
def booking_get(request:Request):
    return templates.TemplateResponse('/index.html', {"request": request})


@app.post("/booking")
def post_booking(phone : str =  Form(...), email: str = Form(...) , date : str = Form(...), time : str = Form(...)):
    
    return create_booking(phone,email,date,time)
