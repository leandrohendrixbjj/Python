"""
  O que é rjust: um método de string que alinha o texto á DIREITA, e preenche os 
  espaços restantes com caracteres a sua escolha.
"""

names = ['João', 'Maria', 'Pedro']

print(names[2].rjust(10))       # '    Pedro'
print(names[2].rjust(10, '-'))  # '----Pedro'

print("**********************************************")

for name in names:
  print(name.rjust(10), '|', 'Ativo')

