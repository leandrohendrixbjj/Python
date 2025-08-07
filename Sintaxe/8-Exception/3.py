"""
   else: O bloco else é executado se o bloco try não levantar uma exceção.
"""

try:
    resultado = 10 / 2
except ZeroDivisionError:
    print("Erro: divisão por zero.")
else:
    print("Resultado:", resultado)
