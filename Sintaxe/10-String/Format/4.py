from helper.clear import clear
clear()


"""
  Formatar strings:
    - %s: string
    - %d: inteiro
    - %f: float
"""

nome = 'Soares'
age = 30
salary = 1000.50

print('Hello %s, you are %d years old and your salary is %.2f' % (nome, age, salary))