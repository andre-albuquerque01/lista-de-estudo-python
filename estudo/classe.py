class Carro:
    velMax = 100
    ligado = True
    cor = ""
    
c1 = Carro()

c1.velMax = 200
c1.ligado = False
c1.cor = "Azul"
estado ="Sim" if c1.ligado else "Não"
print("Velocidade máxima: %i"%c1.velMax)
print("Ligado: "+ estado)
print("Qual a cor do carro? "+ c1.cor)