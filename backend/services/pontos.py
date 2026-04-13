def calcular_pontos(valida, precisou_validacao_humana, usuario):
    if not valida:
        usuario.sequencia_validas = 0
        usuario.modo_confianca = False
        return 0
    
    if precisou_validacao_humana:
        pontos = 15
    else:
        pontos = 10

    usuario.sequencia_validas += 1

    if usuario.sequencia_validas >= 5:
        usuario.modo_confianca = True

    if usuario.modo_confianca:
        pontos = pontos * 1.05

    return round(pontos, 2)