from avaliacao import Avaliacao

class Resturante:
 
  data = []

  """
     Todos os atributos que possuem "_" indica que seu valor deve ser alterado dentro da classe. 
     Isso é recomendado por convesão.
     
     Ele não impede que o atributo seja alterado fora da classe, é uma indicação ao DEV 
     que isso não deve ser feito. Por convesão todo atributo deve ter o "_"

  """
  def __init__(self,nome, categoria):
    self._nome = nome.title() 
    self._categoria = categoria.upper()
    self._ativo = False
    self._avaliacoes = []
    Resturante.data.append(self)

  def __str__(self):
    return f'{self._nome} - {self._categoria} - {self._ativo}'  
  
  """
  Classmethod: diz que a função pode ser acessada diretamente pela classe, sem precisar de 
  uma instância.
  
  Geralmente recebe como primeiro parâmetro a própria classe (cls), Isso permite que você acesse
  atributos e métodos da classe diretamente, sem precisar de uma instância.

  Lembrado que existem diferenças importantes entre classmethod e staticmethod
  """  
  @classmethod
  def list(cls):
    print(f'{"Nome":<25} {"Categoria":<25} {"Situação":<10} {"Média":<5}')
    for data in Resturante.data:
      print(f'{data._nome.ljust(25)} {data._categoria.ljust(25)} {str(data._ativo):<10} {data.calcular_media:<5.2f}')  

  def update_ativo(self):
    self._ativo = not self._ativo

  """
  Property: Método pode ser acessado como um atributo, mas na verdade é um método. 
  Exemplo: r.ativo ao invés de r.ativo(). Encapsulamento com sintaxe limpa, 
  Você esconde a lógica interna de um atributo, mas permite o acesso como se fosse um atributo comum

  Temos outras vantagens de usar property, essa é a que aplicamos no contexto atual.
  """
  @property
  def ativo(self):
    return "True" if self._ativo else "False"
  
  @property
  def calcular_media(self):
    if not self._avaliacoes:
      return 0
    total = sum(avaliacao._nota for avaliacao in self._avaliacoes)
    return total / len(self._avaliacoes)  


  def adicionar_avaliacao(self, cliente, nota):
    score = self._validar_nota(nota)
    avaliacao = Avaliacao(cliente,score)
    self._avaliacoes.append(avaliacao)

  def _validar_nota(self, nota):
    if nota > 5:
      return 5    
    
    return nota

  
