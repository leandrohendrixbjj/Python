"""
  Property: recomendado principalmente quando você quer encapsular acesso a atributos:
  acesso pareça direto (obj.atributo), mas nos bastidores haja lógica adicional      
  Você quer que saldo funcione normalmente, mas internamente ele calcula o juros.

  Devemos usar property para validar os valores
"""

from helper import clear
clear.clear()

class Conta:
  def __init__(self, saldo_inicial):
    self._saldo = saldo_inicial

  @property
  def saldo(self):
    if self._saldo < 0:
      raise ValueError("Saldo deve ser maior que zero.")
    return self._saldo * 1.1 # aplica juros, por exemplo
  
conta = Conta(10)
print(f"Saldo real: {conta._saldo}")
print(f"Saldo real: {conta.saldo}")