"""
    o que é Slice( Fatiar ): forma de pegar uma parte de um objeto/String. 

    sequencia[início:fim:passo]

    início: posição inicial (inclusiva)
    fim: posição final (exclusiva) 

    PEGANDO APENAS UMA PARTE DA STRING   
    
    L E A N D R O
    0 1 2 3 4 5 6
"""

data = 'LEANDRO'

# O retorno é '' pq slice trabalha com o conceito de intervalo de valores.
inicio = 0; fim = 0
print(data[inicio:fim])  # Saida: ''

inicio = 2; fim = 2
print(data[inicio:fim])  # Saida: ''

inicio = 0; fim = 1
print(data[inicio:fim])  # Saida: 'L'

inicio = 3; fim = 4
print(data[inicio:fim])  # Saida: 'D'

inicio = 5; fim = 6
print(data[inicio:fim])  # Saida: 'O'
