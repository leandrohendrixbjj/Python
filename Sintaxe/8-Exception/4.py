"""
  finally: bloco que sempre será executado, independente se houve exceção ou não.
"""

try:
    resultado = 10 / 0
except ZeroDivisionError:
    print("Erro: divisão por zero.")
finally:
    print("Este bloco sempre será executado.")
