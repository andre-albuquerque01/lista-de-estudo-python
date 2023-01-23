import modulo 
# exercicio 1
lista = []
while True:
    desejo = input("Digite ou nome ou Fim para terminar")
    if desejo.lower() == "fim":
        break
    else:
       nome = input("Digite o nome dos conviadados! ")
    lista.append(nome)
    

lista.sort()
for lista in lista:
    print(lista)



# exercicio 2
# palavra = input("Digite uma palavra! ")
dicio = {}

dicio['cor'] = 'verde'
dicio['ponto'] = 'contagem'
continuar = ""
while True:
    continuar = input("Deseja continuar? S/N")
    if continuar.lower() == "n":
        break
    else:
        palavra = input("Digite em uma palavra")
        if palavra.lower() in dicio:
            print(dicio[palavra.lower()])
        else: 
            print("Não há palavras no dicionario")

# if  dicionario[palavra]:
    # print(dicionario[palavra])
# else:
    # print("Não há palavra pesquisada")




# exercicio 3
pergunta = "sim"
while pergunta.lower() == "sim":
    opcao = input("Escolha uma opçao\n 1 - soma\n2 - divisao\n3 - subtracao\n4 - multiplicacao")
    num = int(input("Digite umo primeiro número"))
    num2 = int(input("Digite um o segundo número"))
    if opcao == "1":
        soma = modulo.soma(num, num2)
        print(soma)
    elif opcao == "2":
        div = modulo.div(num, num2)
        print(div)
    elif opcao == "3":
        sub = modulo.sub(num, num2)
        print(sub)
    elif opcao == "4":
        mu = modulo.mul(num, num2)
        print(mu)
    else:
        print("Escolha uma opção mencionada")
    
    pergunta = input("Deseja continuar? Sim ou não").lower()


# exercicio 3
desejo = "sim"

while desejo == "sim":
    jogador = int(input("Escolha 1 - Par e 2 - ímpa\n"))
    
    num = int(input("Digite umo primeiro número"))
    num2 = int(input("Digite um o segundo número"))
    rs = modulo.resto(num, num2, jogador)
    
    if rs == "Ímpa":
        if jogador == 2:
            print("Parabéns jogador 1")
        else:
            print("Parabéns jogador 2")
    else:
        if jogador == 1:
            print("Parabéns jogador 2")
        else:
            print("Parabéns jogador 1")
        
        
    print(rs)
    desejo = input("Deseja continuar?")