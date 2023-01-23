def soma(num, num2):

    # num = 2
    # num2 = 3
    
    soma = num + num2
    return soma
    
def sub(num, num2):
    sub = num - num2
    return sub

def mul(num, num2):
    mul = num * num2
    return mul
    
def div(num, num2):
    div = num // num2
    div1 = num / num2
    return div
    
soma = soma(5,8)
sub = sub(80, 60)
mul = mul(8,2)
div = div(10,2)

# print(soma + sub + mul + div)

def texto(*txt):
    for t in txt:
        print(t)

texto("Andŕe","Num sei", "Aqui", "Agora", "Senhores")