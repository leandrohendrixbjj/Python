"""
    Slice é uma forma de pegar uma parte de um objeto/String

    sequencia[início:fim:passo]

    início: posição inicial (inclusiva)
    fim: posição final (exclusiva)    
"""

data = ['Ana', 'Bruno', 'Carlos', 'Daniela', 'Eduardo']

print(data[1:3])  # ['Bruno', 'Carlos']

print(data[1:])   # ['Bruno', 'Carlos', 'Daniela', 'Eduardo']

print(data[:3])   # ['Ana', 'Bruno', 'Carlos']

print(data[:])    # ['Ana', 'Bruno', 'Carlos', 'Daniela', 'Eduardo']

print(data[-1])    # 'Eduardo'

print(data[-2:])  # ['Daniela', 'Eduardo']


