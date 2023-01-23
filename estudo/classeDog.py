class Cachorro():
    
    """Modelar a classe cachorro"""
    
    def __init__(self, nome, idade):
        """Inicializa o nome e idade pois é o construtor"""
        self.nome = nome
        self.idade = idade
        
    def sentar(self):
        """Um método"""
        print(self.nome.title() + " está sentado.")
        
    def rolar(self):
        """Simula a um comando"""
        print(self.nome.title() + " está rolando, pois já está velho "+ str(self.idade).title() + " anos")
        
doger = Cachorro("Zeus",8)

doger.rolar()
doger.sentar()
