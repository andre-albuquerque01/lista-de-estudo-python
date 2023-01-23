nome = input("Digite seu nome: ")
idade = int(input('Digite sua idade: '))
voto = int(input("1 - Bolsonaro e 2 - Ciro"))
bolsonaro = 0
ciro = 0
# Menor de 16 não volta
# Maior de 16 ate 18 e acima de 64 voto opcional
# O resto tudo vota ainda

if idade >= 16 & idade <= 18 & idade > 64:
    desejo = int(input('Deseja votar:\n1 - sim\n2- Não'))
    if desejo == 1:
        if voto == 1:
            bolsonaro += 1
        elif voto == 2:
            ciro += 1
        else:
            print('Voto inválido')
    else:
        print('Obrigado')
elif idade > 18 & idade < 64:
    if voto == 1:
        bolsonaro += 1
    elif voto == 2:
        ciro += 1
    else:
        print('Voto inválido')
else:
    print("Não tem idade para votar")
    
print("Bolsonaro está com %i"%bolsonaro)
print("Ciro está com %i"%ciro)