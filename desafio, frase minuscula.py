def primeiraMaiuscula(frase):
    frase = frase[0].upper() + frase[1:]
    return frase, len(frase)

if __name__== "__main__":
    frase = input("digite uma frase:")
    frase_maiuscula, tamanho = primeiraMaiuscula(frase)
    print("o tamanho da frase é: {}".__format__(tamanho))
    print(frase_maiuscula)