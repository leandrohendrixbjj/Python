from src.model.restaurantes import *

def options(input_data: int):
    match input_data:
        case 1:
            print('➕ Cadastrar um Restaurante')
            nome = input('Informe o nome do Restaurante: ')
            store(nome)
        case 2:
            print('🚧 Ativar um Restaurante')
            nome = input('Informe o nome do Restaurante: ')
            active(nome)        
        case 3:
            show()
            input("\nPressione Enter para voltar ao menu...")       
        case 4:
            print('🚧 Editar um Restaurante')
            nome = input('Informe o nome do Restaurante: ')
            edit(nome)            
        case _:
            print(f"❌ Opção {input_data} inválida")
