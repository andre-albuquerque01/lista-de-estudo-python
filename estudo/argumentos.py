# Para ter valor padrão e omitindo o valor
def animal(nome, especie="cat"):
    especie = especie
    nome = nome
    print("Eu tenho um "+ especie + " chamado de "+ nome)

# De acordo com posição    
animal("tobias","cat")

# Passando pelo proprio argumento
animal(especie="Dog", nome="Zeus")


animal(nome="Zeus")
animal("Zeus", "dog")


def nome(fisrt_name="", mid_name="", last_name=""):
    fisrt_name = fisrt_name
    mid_name = mid_name
    last_name = last_name
    
    if mid_name != "":
        nome_completo = "O nome é "+fisrt_name.title() +" " + mid_name.title() +" "+ last_name.title()
    else:   
        nome_completo ="O nome é "+fisrt_name.title() +" "+ last_name.title()
        
    return nome_completo
nome = nome("André","Albuquerque")
print(nome)