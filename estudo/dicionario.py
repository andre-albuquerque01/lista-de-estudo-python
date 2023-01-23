# Criar no dicionario
align0 = {'cor': 'verde', 'ponto': 5}

alig = align0.get('cor')
print(alig)
print(align0['cor'])

print("----------------------------------------------------------------------------")
for x in align0:
    print(x) # Chave
    print(align0[x]) # Valor
print("----------------------------------------------------------------------------")

if "cor" in align0:
    print("Tem cor aaaaaaaaaaaaaaaaaaaaah")

print("----------------------------------------------------------------------------")
align0['cor'] = 'azul'
print(align0['cor'])
print(align0['ponto'])

print("----------------------------------------------------------------------------")
align0['ponto'] -= 4
print(align0['ponto'])

print("----------------------------------------------------------------------------")
# Pontuação
print("A pontuação é de "+str(align0['ponto']))

print(align0)

print("----------------------------------------------------------------------------")
# Adicionar depois
align0['positionX'] = 5
align0['positionY'] = 45

print(align0)

print("----------------------------------------------------------------------------")
# Deletar
del align0['positionY']
print(align0)

print("----------------------------------------------------------------------------")
# Precisa da função items para colocar no for
for atr, val in align0.items():
    print(atr)
    print(val)
    
align0.clear()

print("----------------------------------------------------------------------------")
carros = {
    "Carro1":{
        "Fabricante": "VW",
        "Modelo": "UP",
        "Ano": "2015"
    },
    "Carro2":{
        "Fabricante": "Fiat",
        "Modelo": "UNO",
        "Ano": "2019"        
    }
}

print(carros["Carro1"]["Fabricante"])