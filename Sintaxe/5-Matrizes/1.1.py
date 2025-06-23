# Impressão diagonal esquerda, CURTA: 3,5,7

from helper.clear import clear
clear()

data = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

for data_idx in range(len(data)):
    column = len(data) - 1 - data_idx
    print(data[data_idx][column])