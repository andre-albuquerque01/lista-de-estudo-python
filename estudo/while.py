# O input transforma todo entrada em string

while True:
    print("Para encerrar digite sair\n")
    digite = input('Digite um bairro: ')
    
    if digite == "continuar":
        # Serve para quebrar o laço if
        continue
    elif digite == "sair":
        # Serve para quebrar o laço while
        break
    else: 
        print("O bairro digitado foi: "+ digite)
        
print("\nEsyout fora do laço")