"""
  Atributos Privados:

  O que são: são variáveis dentro de uma classe que não devem ser acessadas diretamente 
  de fora do objeto. É uma forma de encapsulamento, um princípio da orientação a objetos.

  Para que serve: Servem para proteger dados internos, evitando que sejam modificados ou 
  lidos de forma indevida.
"""

class Person:
  def __init__(self, name):
    self._name = name    

  def sleep(self):
    print(f"{self._name} está dormindo 8 horas")  

person = Person('Leandro')
person.name = 'Hendrix'
person.sleep()

