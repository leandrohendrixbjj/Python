"""
    Por que existem exceções?
      1- Para evitar que o programa continue em estado inconsistente.
      2- Para informar o usuário sobre o erro ocorrido.
      3- Para facilitar o debug, mostrando exatamente onde e por que falhou.
"""

try:
    data = 1 / 0
except ZeroDivisionError as error:
    print(f"Error: {error}")
