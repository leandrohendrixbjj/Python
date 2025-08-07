"""
  Como tratar vários tipos de erros com exceções
"""

try:    
    resultado = 10 / 0 # Divisão por zero ( ZeroDivisionError )
    numero = int("abc") # Conversão inválida ( ValueError ) 
    resultado = value + 10 # Variável 'value' não definida ( Exception)
except ZeroDivisionError:
    print("Não é possível dividir por zero ( ZeroDivisionError )")
except ValueError:
    print("Erro de valor ( ValueError )")
except Exception as e:
    print(f"Erro inesperado ( Exception ): {e}")
