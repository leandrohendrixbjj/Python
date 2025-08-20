"""
  SELF:

  O que é: referência para o próprio objeto que está sendo manipulado. 
  
  Outras linguagens têm algo parecido:
    Java / C# → this
    Java / C# → this
   
  Para que serve: 
    Imagine que cada objeto é uma ficha de cadastro, O self é como dizer:
       Este campo pertence a esta ficha em particular, não às outras.
    
    self é o jeito do Python dizer “este objeto aqui”.   
"""

class Person:
  def __init__(self, name,age):
    self.name = name
    age = age   

  def sleep(self):
    print(f"{self.name} está dormindo 8 horas")  

person = Person('leandro',40)
person.sleep()

