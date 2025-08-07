"""
  SELF:

  O que é: é uma convenção, o nome dado para o primeiro parâmetro de qualquer método 
  dentro de uma classe. Representa a própria instância do objeto que está executando o método.
   
  Para que serve: permite que o método acesse os atributos e outros métodos da instância
"""

class Person:
  def __init__(self, name,age):
    self.name = name
    age = age   

  def sleep(self):
    print(f"{self.name} está dormindo 8 horas")  

person = Person('leandro',40)
person.sleep()

