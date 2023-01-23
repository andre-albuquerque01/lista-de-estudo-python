import random
import os
contador = 0
numero = random.randrange(1,5)
digite = int(input("Digite um número:\n"))
while numero != digite:
    os.system("clear")
    if numero > digite:
        print("O número é maior")
    elif numero < digite:
        print("O número é menor")
    contador += 1
    digite = int(input("Digite um número:\n"))
print("Parabéns, você acertou\n"+ "Suas tentativas foi de " + str(contador)+"\n")