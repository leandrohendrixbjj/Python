"""
    format: 
      1-) {0} será substituído pelo primeiro argumento passado para format() (name).
      2-) {1} será substituído pelo segundo argumento (age).      
"""

name = 'Lucas'
age = 30

msg_formatada = 'Olá, meu nome é {0} e tenho {1} anos.'.format(name, age)

print(msg_formatada)