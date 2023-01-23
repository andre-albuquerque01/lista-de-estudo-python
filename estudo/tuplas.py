# Não dar para fazer alteração na tupla
alimentos = ('Carne','Hamburge','Churrasco')
# Gambiarra para mudar uma tupla
l_alimentos = list(alimentos)
l_alimentos[1] = "Cheiro verde"
alimentos = tuple(l_alimentos)
for a in alimentos:
    print(a)