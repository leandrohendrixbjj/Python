"""
  Property: Método pode ser acessado como um atributo, mas na verdade é um método. 
  Exemplo: conta.saldo ao invés de conta.saldo(). Encapsulamento com sintaxe limpa, 
  Você esconde a lógica interna de um atributo, mas permite o acesso como se fosse um atributo comum

  Temos outras vantagens de usar property, essa é a que aplicamos neste exemplo.
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
