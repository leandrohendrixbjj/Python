class Person:
  def __init__(self, name: str):
    self._name = name

  def show(self):
    print(f'Seu nome é {self._name}')  


p = Person('leandro') 
p.name = 'soares'
p.show()