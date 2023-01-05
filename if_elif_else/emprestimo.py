valor = float(input('Insira o valor da casa: R$'))
salario = float(input('Insira o valor do seu salário: R$'))
meses = int(input('Insira a quantidade de parcelas: '))
prestacao = valor/meses
desconto = (30/100 * salario)
print(desconto)
if prestacao < desconto:
    print('Empréstimo aprovado!')
else:
    print('Empréstimo negado!')
