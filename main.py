alvo = 34
quantidadeTentativas = 5
jogadorAcertou = False

while quantidadeTentativas > 0 and not jogadorAcertou:
    
    try:
        chute = int(input("Digite um número inteiro entre 0 e 100: "))

        if chute == alvo:
            print("Parabéns, você acertou!!!")
            jogadorAcertou =True
        elif chute > alvo:
            print("Errou, o número é menor")
            quantidadeTentativas -= 1
        else:
            print("Errou, o número é maior")
            quantidadeTentativas = quantidadeTentativas - 1

    except:
        print("Valor informado não é um numero inteiro")

if not jogadorAcertou:
    print("Que pena, o número era " + str(alvo))
