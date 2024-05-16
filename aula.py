def boasVindas(nome, idade):
    print("ola {}, nem parece que voce tem {} anos".format(nome, idade))

def ePar(numero):
    if (numero%2) == 0:
        print("{} é par".format(numero))
    else:
        print("{} é impar".format(numero))

if __name__ == "__main__":
    #nome = input("qual o seu nome?")
    #idade = int(input("qual sua idade? "))
    #boasVindas(nome, idade)
    ePar(int(input("digite o número: ")))