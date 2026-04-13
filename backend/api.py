from datetime import datetime

from fastapi import FastAPI
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware

import models
print("MODELS CARREGADO DE:", models.__file__)

from models import Usuario
from services.ocorrencias import processar_ocorrencia

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class OcorrenciaEntrada(BaseModel):
    nome: str
    local: str
    veiculo: str
    infracao: str

def gerar_palavra_chave(infracao):
    if "garagem" in infracao:
        return "garagem"
    elif "idoso" in infracao:
        return "idoso"
    elif "deficiente" in infracao:
        return "deficiente"
    elif "faixa" in infracao:
        return "faixa"
    elif "carga e descarga" in infracao:
        return "carga_descarga"
    elif "onibus" in infracao:
        return "onibus"
    elif "esquina" in infracao:
        return "esquina"
    elif "rampa" in infracao:
        return "rampa"
    else:
        return "irregularidade"

def gerar_nome_arquivo(primeiro_nome, palavra_chave):
    agora = datetime.now()
    data_formatada = agora.strftime("%d%m%y_%H%M%S")
    return f"{primeiro_nome}_{palavra_chave}_{data_formatada}.jpg"


@app.post("/ocorrencia")
def criar_ocorrencia(dados: OcorrenciaEntrada):
    primeiro_nome = dados.nome.split()[0].capitalize()
    usuario = Usuario(primeiro_nome)
    print("USUARIO CRIADO:", usuario.__dict__)

    palavra_chave = gerar_palavra_chave(dados.infracao)
    foto = gerar_nome_arquivo(primeiro_nome, palavra_chave)

    resultado = processar_ocorrencia(
        usuario=usuario,
        local=dados.local,
        veiculo=dados.veiculo,
        foto=foto
    )

    return resultado