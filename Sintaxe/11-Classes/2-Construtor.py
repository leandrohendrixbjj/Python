# Classe simples com Construtor
from helper import clear
clear.clear()

class Pessoa:
  def __init__(self, name,age,active):
    self.name = name
    self.age = age
    self._active = active


p = Pessoa('leandro',40,True)

print(f'{p.name} | {p.age} | {p._active}')