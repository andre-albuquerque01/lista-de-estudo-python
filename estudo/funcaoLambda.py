# Função aninomas 
soma = lambda a,b:a+b
mult = lambda a,b,c,d: (a + b) * (c + d)

s = soma(1,2)
print(s)
print(mult(2,2,2,2))

print((lambda a,b:a/b)(5,2))
print("---------------------")

r = lambda x, func: x + func(x)
res = r(2, lambda x:x+x)
print(res)