from restaurante import Resturante

res = Resturante('pizzaria do João', 'Pizzaria')
res_1 = Resturante('churrascaria do Zé', 'Churrascaria')

res.update_ativo()

def main():
  Resturante.list()

if __name__ == '__main__':
  main()