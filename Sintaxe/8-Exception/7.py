"""
  Um modelo de execeção personalizada 
"""

# Classe Pai
class MinhaExcecao(Exception):
    pass

# Classe Filha
class UsuarioNaoAutorizadoError(Exception):
    def __init__(self, usuario_id):
        mensagem = f"Usuário {usuario_id} não tem permissão para executar essa ação."
        super().__init__(mensagem)
        self.usuario_id = usuario_id


def deletar_usuario(usuario_id, permissao):
    if not permissao:
        raise UsuarioNaoAutorizadoError(usuario_id)

try:
    deletar_usuario(42, False)
except UsuarioNaoAutorizadoError as e:
    print(e)
