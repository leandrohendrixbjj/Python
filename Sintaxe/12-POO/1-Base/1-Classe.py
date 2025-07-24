"""
  O que é uma classe?
  E a representação de um elemento do mundo real, com seus atributos e comportamentos.

| Elemento  | Classe (representação) | Atributos                  | Métodos                  |
| ----------| ---------------------- | ---------------------------| ------------------------ |
| Pessoa    | `Pessoa`               | `nome`, `idade`, `cpf`     | `falar()`, `andar()`     |
| Carro     | `Carro`                | `marca`, `modelo`, `cor`   | `ligar()`, `acelerar()`  |
| Livro     | `Livro`                | `titulo`, `autor`, `isbn`  | `abrir()`, `fechar()`    |

Para que serve uma classe?
 - Permite modelar situações do mundo real
 - Simular comportamentos, validar regras de negócio
 - Interagir com dados

"""

class Pessoa:
  def __init__(self, nome: str, idade: int):
    self.nome = nome
    self.idade = idade
  
pessoa = Pessoa("João", 30)
print(f"Nome: {pessoa.nome}, Idade: {pessoa.idade}")  