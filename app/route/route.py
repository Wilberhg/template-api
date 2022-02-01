from app import app
from ..view.get_cpf import get_cpf

@app.get("/{your_name}", status_code=200)
async def say_hi(your_name: str):
    return f"Seja bem vindo(a), {your_name.title()}!"

@app.get("/cpf/{your_tel}")
async def use_tel(your_tel: str):
    cpf = get_cpf(your_tel)
    return {'cpf': cpf}