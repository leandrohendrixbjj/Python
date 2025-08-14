    """"
  Exemplo do uso do método ljust para impressão de dados em formato de tabela.
""""

# Define o cabeçalho da tabela
header = ["Nome", "Idade", "Profissão"]

# Define a largura de cada coluna
widthes = [10, 8, 12]

# Define os dados da tabela
dados = [
    ["Alice", "30", "Engenheira"],
    ["Bruno", "25", "Designer"],
    ["Carlos", "28", "Programador"]
]

# Imprime o cabeçalho formatado
linha = ""
for headerText, width in zip(header, widthes):
    linha += headerText.ljust(width)
print(linha)

# Imprime uma linha separadora
print("-" * sum(widthes))

# Imprime os dados
for nameText in dados:
    row = ""
    for name, width in zip(nameText, widthes):
        row += name.ljust(width)
    print(row)
