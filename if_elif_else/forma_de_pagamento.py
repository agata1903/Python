print('Para pagamento no dinheiro, digite 1\n')
print('Para pagamento à vista no cartão, digite 2\n')
print('Para pagamento em até 2x no cartão, digite 3\n')
print('Para pagamento em 3x ou mais no cartão, digite 4\n')
preco = float(input('Digite o preço do produto: '))
forma = int(input('Insira a forma de pagamento: '))
if forma == 1:
    total = preco - (10/100 * preco)
    print('Seu produto deu o total de R$',round(total,2))
elif forma == 2:
    total = preco - (5/100 * preco)
    print('Seu produto deu o total de R$',round(total,2))
elif forma == 3:
    total = preco
    print('Seu produto deu o total de R$',round(total,2))
else:
    total = preco + (20/100 * preco)
    print('Seu produto deu o total de R$',round(total,2))
