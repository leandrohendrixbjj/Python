"""
  Classmethod: diz que a função pode ser acessada diretamente pela classe, sem precisar de uma 
  instância. Geralmente recebe como primeiro parâmetro a própria classe (cls), Isso permite que 
  você acesse atributos e métodos da classe diretamente, sem precisar de uma instância.

  Lembrado que existem diferenças importantes entre classmethod e staticmethod
  """  
  
class Conta:
    taxa = 0.05  # Atributo de classe, taxa de juros

    def __init__(self, saldo=0):
        self._saldo = saldo  # Usando _ para indicar que é um atributo protegido

    @classmethod
    def criar_conta_com_taxa(cls, saldo_inicial):
        """Método de classe para criar uma conta com taxa aplicada."""
        saldo_com_taxa = saldo_inicial + (saldo_inicial * cls.taxa)
        return cls(saldo_com_taxa)
    
conta = Conta.criar_conta_com_taxa(100)
print(f"Saldo inicial com taxa: {conta._saldo}")    