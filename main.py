from fastapi import FastAPI, Depends, HTTPException, Request, Form
from fastapi.staticfiles import StaticFiles
from fastapi.responses import RedirectResponse
from fastapi.templating import Jinja2Templates
from sqlalchemy.orm import Session
from database import get_db
from models import Categoria, Produto

app = FastAPI(title="Sistema de Loja")

app.mount("/static", StaticFiles(directory="static"), name="static")

templates = Jinja2Templates(directory="templates")

@app.get("/")
def exibir_home(request: Request):
    return templates.TemplateResponse(
        request,
        "index.html",
        {"request": request}

    )

@app.get("/categorias")
def exibir_categorias(request: Request, db: Session = Depends(get_db)):
    categorias = db.query(Categoria).all()
    return templates.TemplateResponse(
        request,
        "categorias.html",
        {"request": request,
         "categorias": categorias
        }
    )

@app.post("/categorias")
def cadastrar_categorias(
    nome: str = Form(...),
    descricao: str = Form(...),
    db: Session = Depends(get_db)
):
    nova_categoria = Categoria(nome=nome, descricao=descricao)
    db.add(nova_categoria)
    db.commit()
    return RedirectResponse(url="/categorias", status_code=303)
