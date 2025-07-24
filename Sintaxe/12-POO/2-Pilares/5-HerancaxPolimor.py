"""
  Diferença entre herança e polimorfismo

  Herança: significa que a classe filha herda os atributos e métodos da classe pai exatamente como 
  estão, ou seja, ela ganha tudo que a classe pai tem, sem precisar reescrever.
"""
class Animal:
    def comer(self):
        print("Animal comendo")

# Herança está acontecendo — Cachorro herda de Animal.
class Cachorro(Animal):
    pass

c = Cachorro()
c.comer()  # Herdou o método da classe Animal


"""
  Polimorfismo: a classe filha pode herdar o método da classe pai, mas pode também sobrescrevê-lo 
  (ou “sobrescrever”) para alterar o comportamento. Ou seja, o método existe na classe pai, mas a 
  classe filha pode implementar a sua própria versão, com comportamento diferente.

"""
class Animal:
    def falar(self):
        return "Som genérico"

class Cachorro(Animal):
    def falar(self):
        return "Au au!"

class Gato(Animal):
    def falar(self):
        return "Miau"

def fazer_animal_falar(animal: Animal):
    print(animal.falar())

