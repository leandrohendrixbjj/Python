# Impressão diagonal direita Longa: 3, 5, 7

import os
os.system('cls' if os.name == 'nt' else 'clear')

data = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

for index_row, row in enumerate(data):
    for index_element, element in enumerate(row):
        if (index_row + index_element == 2):
            print(f"{element}", end=' ')
    print()

