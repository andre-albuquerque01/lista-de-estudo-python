import modulo 
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