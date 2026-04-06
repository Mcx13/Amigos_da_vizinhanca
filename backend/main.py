from datetime import datetime
from models import Usuario
from services.ocorrencias import processar_ocorrencia
from data.infracoes import infrações

def apresentar(resultado):
    print("\n=== RESULTADO DA OCORRÊNCIA ===")
    print(f"Usuário: {resultado['nome']}")
    print(f"Local: {resultado['local']}")
    print(f"Veículo: {resultado['veiculo']}")
    print(f"Foto: {resultado['foto']}")
    print(f"Infração identificada: {resultado['infracao']}")
    print(f"Confiança da IA: {resultado['confianca'] * 100:.1f}%")
    print(f"Status: {resultado['status']}")
    print(f"Ocorrência válida: {resultado['valida']}")
    print(f"Precisou validação humana: {resultado['precisou_validacao_humana']}")
    print(f"Pontos ganhos agora: {resultado['pontos_ganhos']}")
    print(f"Pontos totais: {resultado['pontos_totais']}")
    print(f"Sequência de válidas: {resultado['sequencia_validas']}")
    print(f"Modo confiança ativo: {resultado['modo_confianca']}")

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
    

#============================
# 🟢Entrada de dados
#============================


nome_usuario = input("Digite seu nome completo: ")
primeiro_nome = nome_usuario.split()[0].capitalize()

usuario = Usuario(primeiro_nome)

def gerar_nome_arquivo(primeiro_nome):
    agora = datetime.now()
    data_formatada = agora.strftime("%d%m%y_%H%M%S")
    return f"{primeiro_nome}_{data_formatada}.jpg"

while True:
    print("\n--- Nova Ocorrência ---")

    local = input("digite o endereço da ocorrência: ")
    veiculo = input("Digite o tipo de veículo (Carro, Moto, Caminhao, Onibus): ")
    
    lista_infracoes = list(infrações.keys())

    print("\nSelecione a infração identificada:")
    for i, infracao in enumerate(lista_infracoes, start=1):
        print(f"{i}. {infracao}")

    opcao = int(input("Digite o número correspondente à infração: "))
    infracao_selecionada = lista_infracoes[opcao - 1]

    palavra_chave = gerar_palavra_chave(infracao_selecionada)
    foto = gerar_nome_arquivo(primeiro_nome, palavra_chave)
    print(f"Nome do arquivo: {foto}")

    resultado = processar_ocorrencia(usuario, local, veiculo, foto)
    
    apresentar(resultado)

    continuar = input("\nDeseja processar outra ocorrência? (s/n): ").lower()
    if continuar != 's':
        break