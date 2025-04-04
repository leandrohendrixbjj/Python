import os

print("""
░██████╗░█████╗░██████╗░░█████╗░██████╗░  ███████╗██╗░░██╗██████╗░██████╗░███████╗░██████╗░██████╗
██╔════╝██╔══██╗██╔══██╗██╔══██╗██╔══██╗  ██╔════╝╚██╗██╔╝██╔══██╗██╔══██╗██╔════╝██╔════╝██╔════╝
╚█████╗░███████║██████╦╝██║░░██║██████╔╝  █████╗░░░╚███╔╝░██████╔╝██████╔╝█████╗░░╚█████╗░╚█████╗░
░╚═══██╗██╔══██║██╔══██╗██║░░██║██╔══██╗  ██╔══╝░░░██╔██╗░██╔═══╝░██╔══██╗██╔══╝░░░╚═══██╗░╚═══██╗
██████╔╝██║░░██║██████╦╝╚█████╔╝██║░░██║  ███████╗██╔╝╚██╗██║░░░░░██║░░██║███████╗██████╔╝██████╔╝
╚═════╝░╚═╝░░╚═╝╚═════╝░░╚════╝░╚═╝░░╚═╝  ╚══════╝╚═╝░░╚═╝╚═╝░░░░░╚═╝░░╚═╝╚══════╝╚═════╝░╚═════╝░
""")

def finalizar_app():
    print('Saindo do aplicativo...')
    os.system('cls' if os.name == 'nt' else 'clear')

def showOptions(opcao):
     match opcao:
        case 1:
            print('Cadastrar um Restaurante')
        case 2:
            print('Listar um Restaurante')
        case 3:
            print('Ativar um Restaurante')
        case _:
            finalizar_app()
    

print('1. Cadastro')
print('2. Listar')
print('3. Ativar')
print('4. Sair \n')

opcoes_list = [1,2,3,4]
opcao_selecionada = int( input('Escolha uma opção:') )

if not opcao_selecionada in opcoes_list:
    print(f"Opção {opcao_selecionada} não consta na lista!")
    finalizar_app()
else:
    showOptions(opcao_selecionada)







