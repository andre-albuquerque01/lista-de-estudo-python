def calculo(num1, num2):
    num1 = num1
    num2 = num2
    soma = num1 + num2
    equacao = soma % 2
    result = ""
    if equacao == 0:
        result = "Par"
    elif equacao == 1:
        result = "Ímpa"

    return result
