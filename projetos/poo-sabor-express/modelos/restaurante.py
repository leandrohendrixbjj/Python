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
    Resturante.data.append(self)

  def __str__(self):
    return f'{self._nome} - {self._categoria} - {self._ativo}'  
  
  """
    classmethod recebe a classe como primeiro argumento, em vez da instância
     1-) Por convenção, chamamos esse primeiro parâmetro de cls (assim como usamos self para instâncias).
     2-) Ele pode ser usado para acessar ou modificar atributos da classe, ou para criar instâncias alternativas.
  """  
  @classmethod
  def list(cls):
    print(f'{"Nome":<25} {"Categoria":<25} {"Situação":<5}')
    for data in Resturante.data:
      print(f'{data._nome.ljust(25)} {data._categoria.ljust(25)} {data._ativo}')  

  def update_ativo(self):
    self._ativo = not self._ativo

  """
  Property: sinaliza ao desenvolvedor (ou a si mesmo no futuro) que esse atributo:
    1- Não deve ser acessado diretamente fora da classe
    2- Pode estar sujeito a mudança
    3- Pode ter lógica especial envolvida no acesso (como uma propriedade @property depois)  
  """
  @property
  def ativo(self):
    return "True" if self._ativo else "False"

