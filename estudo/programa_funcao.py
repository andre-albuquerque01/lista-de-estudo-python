# Importa tudo
import modulo
# Apenas essa função div
# from modulo import div
# from modulo import *
# soma = modulo.soma(5,2)
# print(soma)

# print(div(10,2))


# num = input("Digite umo primeiro número")
# num2 = input("Digite um o segundo número")
# rs = resto(num, num2)
# print(rs)


desejo = "sim"

while desejo == "sim":
    jogador = int(input("Escolha 1 - Par e 2 - ímpa\n"))
    
    num = int(input("Digite umo primeiro número"))
    num2 = int(input("Digite um o segundo número"))
    rs = modulo.resto(num, num2)
    
    if rs == "Ímpa":
        if jogador == 2:
            print("Parabéns jogador 1")
        else:
            print("Parabéns jogador 2")
    else:
        if jogador == 1:
            print("Parabéns jogador 1")
        else:
            print("Parabéns jogador 2")
        
        
    desejo = input("Deseja continuar?")