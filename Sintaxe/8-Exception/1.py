"""
    O que é uma Exception em Python?
    Uma Exception (exceção) é um erro que ocorre durante a execução de um programa. 
    
    Tipos de erros: 
        1-tentar dividir por zero
        2-acessar um índice que não existe
        3-abrir um arquivo que não existe    

    Python interrompe o programa e "lança" uma exceção.    
"""

print("Início")

x = 10 / 0  # ZeroDivisionError

print("Fim")  # Nunca será executado
