"""
  Desempacotamento com **: unir dois dicionários em um só.
"""

person = {
    "name": "John",
    "age": 30    
}

complement = {"city": "New York"}

# Unindo os dois dicionários:
data = {**person, **complement}

print(data) # {'name': 'John', 'age': 30, 'city': 'New York'}
