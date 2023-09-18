import requests
import json


def pula_linha():
    print(f"\n{'-' * 60}\n")


def requisicao(address, headers):
    request = requests.get(address, headers=headers)
    dicionario = json.loads(request.text)

    return dicionario


chave_live = {"Authorization": "Bearer live_a67be47fcd748e0c6188905501384d"}
chave_test = {"Authorization": "Bearer test_efebdd513a55c8d9c3a239c326a36e"}
chave_utilizada = chave_test

campeonato_brasileiro = "https://api.api-futebol.com.br/v1/campeonatos/10"
campeonato_artilharia = "https://api.api-futebol.com.br/v1/campeonatos/10/artilharia"
campeonato_fases = "https://api.api-futebol.com.br/v1/campeonatos/10/fases"

copa_do_brasil = "https://api.api-futebol.com.br/v1/campeonatos/2"
copa_artilharia = "https://api.api-futebol.com.br/v1/campeonatos/2/artilharia"
copa_fases = "https://api.api-futebol.com.br/v1/campeonatos/2/fases"

dicionario_competicoes = requisicao(campeonato_brasileiro, chave_utilizada)


def printar_competicoes():
    print(dicionario_competicoes)
    print(len(dicionario_competicoes))

    print("\n")
    for i in dicionario_competicoes:
        print(f"{i}: {dicionario_competicoes[i]}")


dicionario_artilharia = requisicao(campeonato_artilharia, chave_utilizada)


def printar_artilharias():
    print(dicionario_artilharia)
    print(len(dicionario_artilharia))

    print("\n")
    for i in dicionario_artilharia:
        print(f"{i}")


dicionario_fases = requisicao(campeonato_fases, chave_utilizada)


def printar_fases():
    print(dicionario_fases)
    print(len(dicionario_fases))

    dicionario = dicionario_fases[0]
    print(dicionario)

    print("\n")

    print(len(dicionario))
    for i in dicionario:
        print(f"{i}: {dicionario[i]}")


printar_competicoes()
pula_linha()
printar_artilharias()
pula_linha()
printar_fases()
