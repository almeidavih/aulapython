import arquivos, os
arquivo = arquivos

sair = False

while sair == False:
    opcao = input("Escolha uma opcao:\n"
                  "1: Cadastrar item\n"
                  "2: listar itens\n"
                  "3: sair\n")
    if opcao == "1":
        item = input("Digite o item a ser adicionado:")
        arquivo.criaArquivo(item)
        os.system('cls')
    elif opcao == "2":
         os.system('cls')
         arquivo.listarArquivos()
    elif opcao == "3":
        sair = True
    else:
        print("opcao invalida")
    
    