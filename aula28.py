"""
Exercicio com classes
1 - Crie uma classe Carro
2 - Crie uma classe Motor
3 - Crie uma classe Fabricante
4 - Faça a ligação entre Carro tem um Motor
obs: Um motor pode ser de varios carros

5 - Faça a ligacao entre Carro e um Fabricante
obs: Um fabricante pode fabricar varios carros

exiba o nome do carro,motor e fabricante na tela
"""
#CARRO
class Carro:
    def __init__(self,marca,motor,fabricante):
        self.marca = marca
        self.motor = motor
        self.fabricante = fabricante

#MOTOR
class Motor:
    def __init__(self,nome):
        self.carros = []
        self.nome = nome

    def listar_carros(self):
        for carro in self.carros:
            print(carro.marca, carro.fabricante.nome, carro.motor.nome)


#FABRICANTE
class Fabricante:
    def __init__(self,nome):
        self.carros = []
        self.nome = nome


    def listar_carros(self):
        for carro in self.carros:
            print(carro.marca, carro.motor.nome,carro.fabricante.nome)


#MOTOR
motor = Motor("XXX 30")
motor2 = Motor("XXX 444")

#FABRICANTE
fabricante = Fabricante("Marcos")
fabricante2 = Fabricante("Miguel")

#CARROS
carro1 = Carro("Fiat" , motor , fabricante)
carro2 = Carro("Fusca" , motor2, fabricante2)

#MOTOR PODE TER VARIOS CARROS
motor.carros.append(carro1)
motor2.carros.append(carro2)

#FABRICANTE PODE FABRICAR VARIOS CARROS
fabricante.carros.append(carro1)
fabricante2.carros.append(carro2)

#LISTAGEM
fabricante.listar_carros()
motor.listar_carros()
print("-----------------------")
motor2.listar_carros()
fabricante2.listar_carros()
