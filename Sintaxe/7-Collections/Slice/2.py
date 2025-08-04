"""
    o que é Slice( Fatiar ): forma de pegar uma parte de um objeto/String. 

    sequencia[início:fim:passo]

    início: posição inicial (inclusiva)
    fim: posição final (exclusiva) 

    PEGANDO DUAS PARTES DA STRING
    
    L E A N D R O
    0 1 2 3 4 5 6
"""

data = 'LEANDRO'

inicio = 0; fim = 2
print(data[inicio:fim])  # Saida: 'LE'

inicio = 2; fim = 4
print(data[inicio:fim])  # Saida: 'AN'

inicio = 4; fim = 6
print(data[inicio:fim])  # Saida: 'DR'

