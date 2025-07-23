
data = {
  "nome": "Maria", 
  "idade": 30
}

new_age = {"idade": 40}  # valor sobrescrito

info = {**data, **new_age}

print(info) #{'nome': 'Maria', 'idade': 40}

