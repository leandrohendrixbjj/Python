# Impressão diagonal esquerda, CURTA: 1, 5, 9

import os
os.system('cls' if os.name == 'nt' else 'clear')

data = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

for row in range(len(data)):
    column = len(data) - 1 - row
    print(data[row][column])