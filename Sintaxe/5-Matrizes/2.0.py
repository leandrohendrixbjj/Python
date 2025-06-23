# Impressão diagonal esquerda, Longa: 1, 5, 9

import os 
os.system('cls' if os.name == 'nt' else 'clear')

data = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

for row_index, row in enumerate(data):
    for element_row, result in enumerate(row):
        if (element_row == row_index):
            print(f"{result}", end=" ")
        