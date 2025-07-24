"""
  O que é um objeto?
  E a instância da classe. A classe é a planta do prédio, enquanto o objeto é o prédio construído
  a partir dessa planta.

  O objeto pronto segue o que está na planta, mas é uma entidade independente, que ocupa espaço
  tem endereço, e pode ser manipulado.
"""


class Predio:
    def __init__(self, nome: str, andares: int):
        self.nome = nome
        self.andares = andares

    def descricao(self):
        return f"Prédio {self.nome} com {self.andares} andares."

# Objetos são instâncias da classe Predio    
predio1 = Predio("Edifício Central", 10)
print(predio1.descricao())

predio3 = Predio("Torre Sul", 20)
print(predio3.descricao())