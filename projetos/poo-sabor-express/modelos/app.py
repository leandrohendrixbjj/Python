from restaurante import Resturante

res = Resturante('pizzaria do João', 'Pizzaria')
res.adicionar_avaliacao('João', 5)
res.adicionar_avaliacao('Maria', 4)
res.adicionar_avaliacao('Pedro', 3)

res.update_ativo()

def main():
  Resturante.list()

  for avaliacao in res._avaliacoes:
    print(avaliacao._cliente, avaliacao._nota)


if __name__ == '__main__':
  main()