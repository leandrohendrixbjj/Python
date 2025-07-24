"""
  O que é polimorfismo? ( Significa muitas formas )

  Para que serve?
  Permite usar o mesmo método em diferentes classes, com o comportamentos diferentes

"""
class Animal:
    def falar(self):
        return "Som de animal"

class Cachorro(Animal):
    def falar(self):
        return "Au au!"

class Gato(Animal):
    def falar(self):
        return "Miau"

class Vaca(Animal):
    def falar(self):
        return "Muu"
