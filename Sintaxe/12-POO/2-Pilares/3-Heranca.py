"""
  O que é Herança?
  E quando uma classe filha herda características de uma classe pai ( ou base ).

  Para que serve?
  Para reutilizar código e especializar comportamentos.
"""

class Animal:
    def __init__(self, nome: str):
        self.nome = nome

    def comer(self):
        return "Come alguma coisa"
    
class Cachorro(Animal):
    pass

class Gato(Animal):
    pass

dog = Cachorro("Rex")
cat = Gato("Mia")

print(f"{dog.nome} come: {dog.falar()}")  # Rex diz: Au Au
print(f"{cat.nome} come: {cat.falar()}")  # Mia diz:            