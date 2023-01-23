pergunta = "sim"
while pergunta.lower() == "sim":
    opcao = input("Escolha uma opçao\n1 - soma\n2 - divisao\n3 - subtracao\n4 - multiplicacao\n")
    num = int(input("Digite um o primeiro número\n"))
    num2 = int(input("Digite um o segundo número\n"))
    try:
        if opcao == "1":
            soma = num + num2
            print("A soma é de %i" %soma)
        elif opcao == "2":
            div = num / num2
            print("A divisão é de %i"%div)
        elif opcao == "3":
            sub = num - num2
            print("A dubtração é de %i"%sub)
        elif opcao == "4":
            mu = num * num2
            print("A multiplicação é de %i"%mu)
        else:
            print("Escolha uma opção mencionada")
    except:
            print("Não foi possível fazer a operação")
        
    pergunta = input("Deseja continuar? Sim ou não\n").lower()