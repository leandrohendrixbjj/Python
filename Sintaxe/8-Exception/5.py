"""
    Capturando a mensagem do erro
        Erro capturado: invalid literal for int() with base 10: 'abc'
"""
try:
    int("abc")
except ValueError as erro:
    print("Erro capturado:", erro)
