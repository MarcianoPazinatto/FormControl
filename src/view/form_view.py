from fastapi import Depends, UploadFile, File
from src.model.form_model import AdvancedForm
from fastapi import APIRouter, Request, Form

from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

form_data_views = APIRouter()
templates = Jinja2Templates(directory="view/templates/")


@form_data_views.get('/', response_class=HTMLResponse)
def get_home(request: Request):
    return templates.TemplateResponse("home.html", {"request": request})


@form_data_views.get('/basic', response_class=HTMLResponse)
def get_basic_form(request: Request):
    return templates.TemplateResponse("basicform.html", {"request": request})


@form_data_views.post('/basic', response_class=HTMLResponse)
async def post_basic_form(request: Request, username: str = Form(...), password: str = Form(...),
                          file: UploadFile = File(...)):
    print(f'username: {username}')
    print(f'password: {password}')
    content = await file.read()
    print(content)
    return templates.TemplateResponse("basicform.html", {"request": request,
                                                         "username": username,
                                                         "password": password})


@form_data_views.get('/advanced', response_class=HTMLResponse)
def get_form(request: Request):
    return templates.TemplateResponse("advancedform.html", {"request": request})


@form_data_views.post('/advanced', response_class=HTMLResponse)
def post_form(request: Request, form_data: AdvancedForm = Depends(AdvancedForm.as_form)):
    print(form_data)
    print(form_data.username)
    username = form_data.username
    password = form_data.password
    return templates.TemplateResponse("advancedform.html", {"request": request,
                                                            "username": username,
                                                            "password": password})
