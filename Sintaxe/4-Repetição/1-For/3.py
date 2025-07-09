"""
  Percorre o array data somando o valor de score de cada aluno.
"""

from helper import clear
clear.clear()

data = [
  {'student': 'Alice', 'score': 10},
  {'student': 'Bob', 'score': 9},
  {'student': 'Charlie', 'score': 7.5},
]

total = sum(student['score'] for student in data)  

print(f'Total score: {total}')  