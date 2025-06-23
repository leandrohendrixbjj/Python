# Impressão diagonal direita Curta: 1, 5, 9

from helper.clear import clear
clear()

data = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

for data_row in range(len(data)):
    column = data_row
    print(data[data_row][column])