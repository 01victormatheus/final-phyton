try:
    dados={"nome": "negão","idade":20}
    print(dados["nome"])
    print(dados["idade"])
    print(dados["localização"])
except(KeyError):
    print("este indice nao existe")

