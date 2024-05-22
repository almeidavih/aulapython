def criaArquivo(texto):
    try:
        with open("arquivo.txt", "r+") as arquivo:
            conteudo = arquivo.readlines()
            conteudo.append(texto + "\n")
            arquivo.close()
        arquivo = open("arquivo.txt", "w")
        arquivo.writelines(conteudo)
        arquivo.close()
    except Exception as e:
        print("Falha ao abrir o arquivo:{}".format(e))

def listarArquivos():
    with open("arquivo.txt", "r") as arquivo:
        conteudo = arquivo.read()
    for item in conteudo:
        print(item, end="")

