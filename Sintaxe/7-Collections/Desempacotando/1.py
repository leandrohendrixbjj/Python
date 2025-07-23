"""
  O ** em Python é usado para desempacotar dicionários.
"""

data = {
  "nome": "Maria", 
  "idade": 30
}

complement = {"cidade": "São Paulo"}

# Unindo os dois dicionários:
info = {**data, **complement}
print(info) # {'nome': 'Maria', 'idade': 30, 'cidade': 'São Paulo'}
