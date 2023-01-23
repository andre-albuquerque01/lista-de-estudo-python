carros = ['audi', 'bwm', 'honda']

for c in carros:
    if c != 'bwm':
        print(c.title())
    else:
        print(c.upper())


alimento = []
for i in range(1,10):
    alimento.append(i)
    
for a in alimento:
    if (a % 2) == 0:
        print('É par %s'%a)
    elif (a % 2) == 1:
        print('Não é ímpa com o resto 1, %s'%a)
    else:
        print('Não é ímpa %s'%a)        
        