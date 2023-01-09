cont = total = precoalto = 0
maisbarato = ' '

resp1 = str(input('Deseja cadastrar um produto? '))
while resp1 in 'Ss':
    produto = str(input('Digite o nome do produto: '))
    preco = float(input('Digite o preço deste produto: '))
    cont += 1
    total += preco
    if preco > 1000:
        precoalto += 1
    if cont == 1 or preco < menor:
        menor = preco
        maisbarato = produto
    resp2 = str(input('Deseja continuar? ')).strip().upper()
    if resp2 in 'Ss':
        resp1 = str(input('Deseja cadastrar um produto? '))
    if resp1 in 'Nn' or resp2 in 'Nn':
        print('O total de compras foi de R$', total, '.\n A quantidade de produtos que custam mais de R$1000.00 é de ', precoalto,'\n O produto mais barato é ', maisbarato,'.')
        break
print('Fim')