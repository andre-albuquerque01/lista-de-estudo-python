class Restaurante():
    
    def __init__(self, nome, tipo):
        self.nome = nome
        self.tipo = tipo
        
    def restaurante_descricao(self):
        print("O nome do restaurante é "+ self.nome.title() + " e o seu tipo é "+ self.tipo.title())
    
    def restaurante_aberto(self):
        print("Está aberto")     
    
    def restaurante_fechado(self):
        print("Está fechado")
    
rest1 = Restaurante("Chivas","Mexicana")
rest2 = Restaurante("Amendoin","carne")
rest3 = Restaurante("Barraca do seu zé","churros")
rest1.restaurante_descricao()
rest2.restaurante_descricao()
rest3.restaurante_descricao()
rest1.restaurante_aberto()
    
class Usuario():
    def __init__(self, firt_nome, second_name, idade, sexo):
        self.firt_nome = firt_nome
        self.second_name = second_name
        self.idade = idade
        self.sexo = sexo
    
    def perfil(self):
        print("O seu nome é "+ self.firt_nome.title() + " e o seu sobrenome é "+ self.second_name.title() + " e sua idade é " + str(self.idade) + " e o seu sexo é " + self.sexo.title())
        
    def saudacao(self):
        print("Hi, "+ self.firt_nome.title() + " que bom ter você por aqui!")
        
user = Usuario("André", "Albuquerque", 21, "masculino")
user2 = Usuario("André", "Gonçalves", 21, "masculino")
user.perfil()
user2.perfil()
user.saudacao()