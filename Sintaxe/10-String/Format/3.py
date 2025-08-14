"""
    format: 
      1-) f'...' indica que é uma f-string (formatação de string moderna do Python).
      2-) {value:.2f} significa:
        1-) value → variável que será exibida.
        2-) :.2f → formato float (f) com 2 casas decimais (.2).

   Dicas extras:
     1-) Se você quisesse 3 casas decimais, usaria {value:.3f} → 125.574

"""      

value = 125.573637

msg_formatada = f'O valor formatado é: {value:.2f}'

print(msg_formatada)