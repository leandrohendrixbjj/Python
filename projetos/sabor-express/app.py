from menu import exibir_menu
import selecao
from clear import limpar_tela

def main():
    try:
        limpar_tela()
        exibir_menu()
        selecao.controller()
    except Exception:
        print("Opção inválida")        

if __name__ == "__main__":
    main()
