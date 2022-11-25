produto = input('Digite o nome do produto:')
valor_total = float(input('Digite o valor total do produto:'))
desconto = int(input('Qual o desconto que você quer aplicar nesse produto?'))
porcentagem_do_desconto = desconto/100
valor_com_desconto = valor_total * porcentagem_do_desconto
valor_final = valor_total - valor_com_desconto
print('O produto', produto, 'com desconto agora custa R$', round(valor_final,2))