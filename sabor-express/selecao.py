import logout
import showMenu

def controller():
    opcoes_list = [1,2,3,4]
    opcao_selecionada = int( input('Escolha uma opção:') )
        
    if not opcao_selecionada in opcoes_list:
        print(f"Opção {opcao_selecionada} não consta na lista!")
        logout.finalizar_app()
    else:
        showMenu.showOptions(opcao_selecionada)
