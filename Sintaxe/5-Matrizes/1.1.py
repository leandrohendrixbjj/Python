# Impressão diagonal direita Curta: 3, 5, 7

import os
os.system('cls' if os.name == 'nt' else 'clear')

data = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

for row in range(len(data)):
    column = row
    print(data[row][column])