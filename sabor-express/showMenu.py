import logout

def showOptions(opcao):
     match opcao:
        case 1:
            print('Cadastrar um Restaurante')
        case 2:
            print('Listar um Restaurante')
        case 3:
            print('Ativar um Restaurante')
        case _:
            logout.finalizar_app()
