def nome(fisrt_name="", mid_name="", last_name=""):
    fisrt_name = fisrt_name
    mid_name = mid_name
    last_name = last_name
    
    if mid_name != "":
        nome_completo = "O nome é "+fisrt_name.title() +" " + mid_name.title() +" "+ last_name.title()
    else:   
        nome_completo ="O nome é "+fisrt_name.title() +" "+ last_name.title()
        
    return nome_completo

def soma(num, num2):
    num = num
    num2 = num2    
    soma = (num) + num2
    return soma
    
def sub(num, num2):
    num = num
    num2 = num2
    sub = num - num2
    return sub

def mul(num, num2):
    num = num
    num2 = num2
    mul = num * num2
    return mul
    
def div(num, num2):
    num = num
    num2 = num2
    div = num // num2
    div1 = num / num2
    return div

def resto(num, num2):
    soma = num + num2
    if soma % 2 == 1:
        return "Ímpa"
    else:
        return "Par"
        
