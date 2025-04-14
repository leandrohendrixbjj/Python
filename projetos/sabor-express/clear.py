import os

def limpar_tela():
    comando = "cls" if os.name == "nt" else "clear"
    os.system(comando)
