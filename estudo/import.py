from classeCar import carroEletrico
# from classeCar import *
# import classeCar as car

carro_meu = carroEletrico("Corala", "Toyota")
print(carro_meu.desc())

# Chamando a estancia que é a bateria e depois o objeto
print(carro_meu.bateria.bateria)

carro_meu.bateria.altera_bateria(70)
print(carro_meu.bateria.mostra_bateria())