# Using multiple conditions

data = 10
info = 5

if data > 5 and info < 10:
    print('Both conditions are true')

if (data > 5 or info < 3): 
    print('At least one condition is true')

if not (data < 10):
    print('Data is not greater than 10')
