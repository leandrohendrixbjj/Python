"""
  O que é Encapsulamento?

  Um dos pilares da Programação Orientada a Objetos (POO) é o encapsulamento, que permite
  proteger os dados de uma classe, tornando-os acessíveis apenas através de métodos específicos.

  Para que serve? 
  - Segurança: impede acesso direto a atributos sensíveis
  - Controle: você define como os dados podem ser lidos ou alterados    
  - Clareza: separa o como funciona do como se usa
  - Manutenção fácil: mudanças internas não afetam quem usa a classe
"""

class ContaBancaria:
    def __init__(self, titular: str, saldo_inicial: float = 0):
        self.titular = titular
        self.__saldo = saldo_inicial  # atributo privado

    def depositar(self, valor: float):
        if valor > 0:
            self.__saldo += valor
        else:
            print("Valor de depósito inválido.")

    def sacar(self, valor: float):
        if 0 < valor <= self.__saldo:
            self.__saldo -= valor
        else:
            print("Saque inválido ou saldo insuficiente.")

    def consultar_saldo(self):
        return self.__saldo
    
try:
    conta = ContaBancaria("Maria", 1000)

    conta.depositar(200)
    conta.sacar(500)

    print(f'Saldo: R$ {conta.consultar_saldo()}')  # 700

    # Acesso direto é bloqueado
    print(conta.__saldo)  # Erro: atributo privado
except AttributeError as e:
    print(f"Erro: {e}")    
