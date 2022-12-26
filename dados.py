soma = 0
media = 0
menos = 0
for d in range(1,5):
    nome = str(input('Digite seu nome: '))
    sexo = str(input('Digite seu sexo: '))
    idade = int(input('Digite sua idade: '))

    soma = soma + idade
    media = soma / 4
    if idade < 20:
        menos = menos + 1
    print('Dados computados com sucesso!')
print('A soma entre as idades é ', soma,'.\n A média entre as idades é ', media, '.\n Existem ', menos,'pessoas com menos de 20 anos.')
