import logout
import showMenu
from menu import exibir_menu

def controller():
    opcoes_list = [1,2,3,4]
    opcao_selecionada = int( input('Escolha uma opção:') )
    
    if not opcao_selecionada in opcoes_list:
        print(f"Opção {opcao_selecionada} não consta na lista!")           
        exibir_menu()     
    else:
        showMenu.showOptions(opcao_selecionada)
