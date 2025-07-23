from restaurante import Resturante

res = Resturante('pizzaria do João', 'Pizzaria')
res.adicionar_avaliacao('João', 0)
res.adicionar_avaliacao('Maria', 0)
res.adicionar_avaliacao('Pedro', 0  )

res.update_ativo

def main():
  Resturante.list()

  
if __name__ == '__main__':
  main()