"""
  SELF: é a referência à instância atual da classe
  É obrigatório quando você quer ATRIBUIR valores aos atributos da classe criada

  Em caso de omissão, ele será considerado um variável local que não pode ser
  acessada fora da classe/construtor
"""

from helper import clear
clear.clear()

class Pessoa:
  def __init__(self, name,age):
    self.name = name
    age = age   

  
p = Pessoa('leandro',40)

# AttributeError: 'Pessoa' object has no attribute 'age'
print(f'{p.name} | {p.age}')