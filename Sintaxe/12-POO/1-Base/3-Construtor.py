"""
  Construtor
  
  O que é: método especial dentro de uma classe, chamado automaticamente quando 
  você cria um objeto da classe.

  Para que serve: Garantir que o objeto já comece com os dados necessários para funcionar 
  corretamente.

"""
from helper import clear
clear.clear()

class Pessoa:
  def __init__(self, name,age,active):
    self.name = name
    self.age = age
    self._active = active


p = Pessoa('leandro',40,True)

print(f'{p.name} | {p.age} | {p._active}')