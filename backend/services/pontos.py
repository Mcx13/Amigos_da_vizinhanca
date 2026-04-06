def calcular_pontos(valida, precisou_de_validacao_humana, usuario):
    if not valida:
        usuario.sequecia_valida = 0
        usuario.modo_confiança = False
        return 0
    
    if precisou_de_validacao_humana:
        pontos = 15
    else:
        pontos = 10

    usuario.sequencia_validas += 1

    if usuario.sequencia_validas >= 5:
        usuario.modo_confiança = True

    if usuario.modo_confiança:
        pontos = pontos * 1.05

    return round(pontos, 2)