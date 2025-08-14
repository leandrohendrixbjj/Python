"""
  O que é ljust: um método de string que alinha o texto á ESQUERDA, e preenche os 
  espaços restantes com caracteres a sua escolha.
"""

names = ['João', 'Maria', 'Pedro']

print(names[2].ljust(10))       # 'Pedro      '
print(names[2].ljust(10, '-'))  # 'Pedro------'

print("**********************************************")

for name in names:
    print(name.ljust(10), '|', 'Ativo')

