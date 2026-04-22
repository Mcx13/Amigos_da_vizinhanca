import base64
import json
from openai import OpenAI


client = OpenAI()


def imagem_para_base64(caminho):
    with open(caminho, "rb") as f:
        return base64.b64encode(f.read()).decode("utf-8")


def analisar_imagem(caminho_imagem):
    print("recebi a imagem:", caminho_imagem)

    imagem_base64 = imagem_para_base64(caminho_imagem)

    prompt = """
    Analise a imagem e identifique se há uma infração de trânsito
    
    Responda APENAS em JSON neste formato:
    {
        "infracao": "...",
        "confianca": 0.0
    }

    Infrações possíveis:
    - veiculo estacionado em frente de garagem
    - parar em faixa de pedestre
    - estacionar em vaga de deficiente sem autorizacao
    - estacionar em vaga de idoso sem autorizacao
    - estacionar em local de carga e descarga
    - estacionar em rampa de acessibilidade
    - estacionar em esquina
    - estacionar frente ao hidrante

    se não tiver certeza, use infracao como null.
    """

    resposta = client.responses.create(
        model="gpt-5.4-mini",
        input=[
            {
                "role": "user",
                "content":[
                    {"type": "input_text", "text": prompt},
                    {
                        "type": "input_image",
                        "image_url": f"data:image/jpeg;base64,{imagem_base64}"
                    }
                ]
            }
        ]
    )

    texto = resposta.output_text

    try:
        dados = json.loads(texto)
        return dados.get("infracao"), float(dados.get("confianca", 0.0))
    except:
        print("Erro ao interpretar resposta da IA", texto)
        return None, 0.0