from services.analise_ia import analisar_imagem
from services.pontos import calcular_pontos


def processar_ocorrencia(usuario, local, veiculo, foto):
    infracao_id, confianca = analisar_imagem(foto)

    if infracao_id and confianca >= 0.8:
        status = "classificado automaticamente"
        valida = True
        precisou_de_validacao_humana = False
    elif infracao_id and confianca < 0.8:
        status = "precisa de validação humana"
        valida = True
        precisou_de_validacao_humana = True
    else:
        status = "rejeitado"
        valida = False
        precisou_validacao_humana = False
    
    pontos_ganhos = calcular_pontos(valida, precisou_validacao_humana, usuario)
    usuario.pontos += pontos_ganhos

    return {
        "nome": usuario.nome,
        "local": local,
        "veiculo": veiculo,
        "foto": foto,
        "infracao": infracao_id,
        "confianca": confianca,
        "status": status,
        "valida": valida,
        "precisou_validacao_humana": precisou_validacao_humana,
        "pontos_ganhos": pontos_ganhos,
        "pontos_totais": usuario.pontos,
        "sequencia_validas": usuario.sequencia_validas,
        "modo_confianca": usuario.modo_confianca 
    }