class carro():

    def __init__(self, modelo, fabricante):
        self.modelo = modelo
        self.fabricante = fabricante
        self.odometro = 0
        self.combsutivel = 100

    def desc(self):
        nome_logo = self.modelo + " " + self.fabricante
        return nome_logo.title()

    def leia_odometro(self):
        return self.odometro

    def altera_odometro(self, new_odometro):
        self.odometro = new_odometro

    def incrementa_odometro(self, new_odometro):
        self.odometro += new_odometro

    def tanque_combustivel(self):
        return "O tanque de combustível está com " + str(
            self.combsutivel) + "%"


carro1 = carro("opala", "gm")
print(carro1.tanque_combustivel())


# Herança apenas passando parâmetro
class carroEletrico(carro):
    # Iniciliza os atributos da classe pai
    def __init__(self, modelo, fabricante):
        # Para estanciar a super class do pai
        super().__init__(modelo, fabricante)
        self.bateria = bateria()

    def tanque_combustivel(self):
        return "Carro elétrico usa energia"


# carroElectric = carroEletrico("Tesla", "opala")
# print(carroElectric.desc())
# print(carroElectric.tanque_combustivel())


class bateria():

    def __init__(self, bateria=100):
        self.bateria = bateria

    def altera_bateria(self, novo_valor):
        self.bateria = novo_valor

    def mostra_bateria(self):
        return "A bateria está com " + str(self.bateria) + "%"


carro_meu = carroEletrico("Corola", "Toyota")
print(carro_meu.desc())

# Chamando a estancia que é a bateria e depois o objeto
print(carro_meu.bateria.bateria)

carro_meu.bateria.altera_bateria(70)
print(carro_meu.bateria.mostra_bateria())

# meu_carro = carro("sedan","fiat")
# print(meu_carro.desc())
# print(meu_carro.leia_odometro())
# print(" ")

# meu_carro.odometro = 8
# print("Leia odomêtro")
# print(meu_carro.leia_odometro())

# print(" ")
# print("Leia odomêtro")
# meu_carro.altera_odometro(87)
# print(meu_carro.leia_odometro())

# print(" ")
# print("Leia odomêtro")
# meu_carro.incrementa_odometro(10)
# print(meu_carro.leia_odometro())

# carro2 = carro("veloster", "Hundai")
# print(carro2.desc())
# print(carro2.leia_odometro())

# print("Leia odomêtro")
# carro2.odometro = 0
# print(carro2.leia_odometro())
# print(" ")

# print("Leia odomêtro")
# carro2.altera_odometro(10)
# print(carro2.leia_odometro())
# print(" ")

# print("Leia odomêtro")
# carro2.incrementa_odometro(-10)
# print(carro2.leia_odometro())
# print(" ")
