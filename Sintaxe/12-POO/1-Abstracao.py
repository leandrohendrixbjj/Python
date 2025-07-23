"""
  O que é Abstração?

  Abstração é um dos pilares da Programação Orientada a Objetos (POO) que permite simplificar a 
  complexidade de um sistema, focando apenas nos aspectos essenciais e ocultando os detalhes 
  desnecessários.

  Você não precisa saber como um carro funciona internamente para usá-lo. O que importa é: 
  volante, pedais, câmbio... Isso é abstração!

  Na classe abaixo foi abstraido os detalhes mecânicos e eletrônicos de ligar e desligar um carro.

"""

class Carro:
    def __init__(self, modelo: str):
        self.modelo = modelo
        self.__ligado = False
        self.__velocidade = 0

    def ligar(self):
        if not self.__ligado:
            self.__ligado = True
            print(f"{self.modelo} ligado.")
        else:
            print(f"{self.modelo} já está ligado.")
    
    def desligar(self):
        if self.__ligado and self.__velocidade == 0:
            self.__ligado = False
            print(f"{self.modelo} desligado.")
        elif self.__velocidade > 0:
            print("Pare o carro antes de desligar.")
        else:
            print(f"{self.modelo} já está desligado.")

    def status(self):
        print(f"Modelo: {self.modelo}")
        print(f"Ligado: {self.__ligado}")        

carro = Carro("Fusca")
carro.ligar()           
carro.status()          
carro.desligar()        



