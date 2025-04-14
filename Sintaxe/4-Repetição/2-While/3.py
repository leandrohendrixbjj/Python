# While Break
import os
os.system('cls' if os.name == 'nt' else 'clear')

while True:
    data = input("Digite para 'sair' para encerrar:   ")
    if data.lower() == 'sair':
        break;
    print(f"Você digitou {data}")
    continue;
    