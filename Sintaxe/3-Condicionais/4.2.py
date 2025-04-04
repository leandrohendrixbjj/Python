"""
   O bloco if é definido pela indentação (espaços ou tabs). Tudo o que estiver indentado após a 
   linha if faz parte do bloco if. Quando a indentação retorna ao nível original, 
   o bloco if acaba.
"""
data = 10

if data > 5:
    print("Data is greater than 1")
    print("Data is greater than 2")
    print("Data is greater than 3")

print("Data is greater than 4")  # Essa linha não faz parte do bloco if e será impressa