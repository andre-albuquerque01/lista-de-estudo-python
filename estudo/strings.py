nome1 = "andre"
nome2 = 'albuquerque'
nomeCompleto = " "+ nome1 + ' ' + nome2 + "  "
nomeCompleto2 = nomeCompleto.title()

print(nomeCompleto2)
print(nomeCompleto2.lower())
print(nomeCompleto.upper())
num = 24

# Apelidando a variavel com o %s
print("Olá %s, %i como que estas?"%(nomeCompleto2, num))
print("Olá"+ nomeCompleto+" ,"+ str(num) +", como que estas")
# print("Olá %d, como que estas?"%num)

# Remove o espaço do lado esquerdo
print("Acabou o espaço aqui " + nomeCompleto.lstrip() + ", tem espaço aqui")
# Remove o espaço do lado direito
print("Tem espaço aqui, " + nomeCompleto.rstrip()+ ", tinha coisa aqui")
# Remove o espaço dos lados
print("Tem espaço aqui, " + nomeCompleto.strip()+ ", tinha coisa aqui\n kkkkk")

# Para localizar a palavra em
texto = "Python is here"
palavra = "Python"
a = palavra in texto
print(a)
a = palavra not in texto
print(a)

cidade = "BSB"
dia = 15
mes = "Dezembro"
ano = 2022
# Placeholder
data = "{}, {} de {} de \b \"{}\""


print(data.format(cidade,dia,mes,ano))