desejo = "sim"
while desejo.lower() == "sim":
    with open('texto.txt', 'a') as arquivo:
        texto = input("Escreva algo\n")
    
        arquivo.write(texto)
        
    desejo = (input("Deseja continuar?\n")).lower()
    