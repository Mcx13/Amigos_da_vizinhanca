def analisar_imagem(nome_arquivo):
    print("Recebi a imagem:", nome_arquivo)

    nome = nome_arquivo.lower()

    if "garagem" in nome:
        return "veiculo estacionado em frente de garagem",0.8
    elif "hidrante" in nome:
        return "estacionamento em frente ao hidrante",0.8
    elif "faixa" in nome:
        return "parar em faixa de pedestre",0.95
    elif "deficiente" in nome:
        return "estacionar em vaga de deficiente sem autorizacao",0.9
    elif "idoso" in nome:
        return "estacionar em vaga de idoso sem autorizacao",0.9
    elif "carga" in nome:
        return "estacionar em local de carga e descarga",0.85
    elif "rampa" in nome:
        return "estacionar em rampa de acessibilidade",0.85
    elif "esquina" in nome:
        return "estacionar em esquina",0.8
    else:
        return None, 0.4