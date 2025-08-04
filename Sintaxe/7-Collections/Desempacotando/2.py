"""
 O Python: escreve o novo dicionário da esquerda para a direita, sobrescrevendo as chaves 
 duplicadas.
"""
person = {
    "name": "John",
    "age": 30,
    "city": "New York"
}

# sobrescreve a chave 'city'
complement = {'city': 'Sao Paulo', 'country': 'Brazil'}

data = {**person, **complement}

print(data)  # {'name': 'John', 'age': 30, 'city': 'Los Angeles', 'country': 'USA'}