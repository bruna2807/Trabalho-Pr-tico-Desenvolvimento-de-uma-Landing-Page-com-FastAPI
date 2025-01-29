from fastapi import FastAPI, Request, Form
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from starlette.staticfiles import StaticFiles

app = FastAPI()

# Configurando a pasta de arquivos estáticos (CSS, imagens, JS)
app.mount("/static", StaticFiles(directory="static"), name="static")

# Configurando os templates
templates = Jinja2Templates(directory="templates")

@app.get("/", response_class=HTMLResponse)
async def home(request: Request):
    return templates.TemplateResponse("home.html", {"request": request})

@app.get("/sobre", response_class=HTMLResponse)
async def sobre(request: Request):
    return templates.TemplateResponse("sobre.html", {"request": request})

@app.get("/produtos", response_class=HTMLResponse)
async def produtos(request: Request):
    return templates.TemplateResponse("produtos.html", {"request": request})

@app.get("/contato", response_class=HTMLResponse)
async def contato(request: Request):
    return templates.TemplateResponse("contato.html", {"request": request})

@app.post("/contato", response_class=HTMLResponse)
async def enviar_contato(request: Request, nome: str = Form(...), email: str = Form(...), mensagem: str = Form(...)):
    return templates.TemplateResponse("contato.html", {"request": request, "mensagem": "Mensagem enviada com sucesso!"})
