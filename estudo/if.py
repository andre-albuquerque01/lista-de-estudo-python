cor = "red"
num = 1
# Indendação é importante para funcionar
if num >= 5:
    if cor == 'Blue':
        print('Cor é azul, %s'%cor)
    # Else if
    elif cor == 'red':
        print('Cor é red, %s'%cor)    
    else:
        print('Cor não é azul, %s'%cor)
else:
    print(num)