carro = ['ferrari', 'gol', 'impala']
print(carro)
# ['ferrari', 'gol', 'impala']

# Altera

carro[1] = "Civic"
carro.append("Bmw")
print(carro)
# ['ferrari', 'Civic', 'impala', 'Bmw']

# Insere

carro.insert(0, "Mercedes")
print(carro)
# ['Mercedes', 'ferrari', 'Civic', 'impala', 'Bmw']

carro2 = ['Fit', 'Coralla', 'Fusca']
carro3 = carro + carro2
print("União dos carros "+ str(carro3))

carro.extend("mustang")
print(carro)
# ['Mercedes', 'ferrari', 'Civic', 'impala', 'Bmw', 'm', 'u', 's', 't', 'a', 'n', 'g']

# Remove

del carro[3]
print(carro)
# ['Mercedes', 'ferrari', 'Civic', 'Bmw', 'm', 'u', 's', 't', 'a', 'n', 'g']

# Remove o último

carro.pop()
print(carro)
# ['Mercedes', 'ferrari', 'Civic', 'Bmw', 'm', 'u', 's', 't', 'a', 'n']

# Remove o selecionado

carro.pop(2)
print(carro)
# ['Mercedes', 'ferrari', 'Bmw', 'm', 'u', 's', 't', 'a', 'n']

# Remove o que pede

carro.remove("m")
print(carro)
# ['Mercedes', 'ferrari', 'Bmw', 'u', 's', 't', 'a', 'n']

# Ordena e altera a lista de principio

carro.sort()
print(carro)

carro.sort(reverse=True)
print(carro)

# Reveso da lista

carro.reverse()
print(carro)

# Não Altera a lista de principio

print(sorted(carro))

# Tamanho da lista

print(len(carro))

# Cria lista
marca = ['VW', 'GM','BMW','FIAT']
print(marca)

# Adicionar
marca.append('MERCEDES')
print(marca)

# Remove
marca.pop()
print(marca)

# Remove
del marca[1]
print(marca)