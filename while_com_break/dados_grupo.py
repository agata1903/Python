c = 0
contamaiores = 0
contahomem = 0
contamulhermenos = 0
resp1 = str(input('Deseja cadastrar seus dados? ')).strip().upper()
while resp1 == 'S':
    idade = int(input('Digite sua idade: '))
    sexo = str(input('Digite seu sexo: '))
    if idade > 0 and sexo in 'FfMm':
        c += 1
    if idade > 18:
        contamaiores += 1
    if sexo in 'Mm':
        contahomem += 1
    if idade < 20 and sexo in 'Ff':
        contamulhermenos += 1
    resp2 = str(input('Deseja continuar? ')).strip().upper()
    if resp2 == 'S':
        resp1 = str(input('Deseja cadastrar seus dados? ')).strip().upper()
    if resp1 == 'N' or resp2 == 'N':
        print('A quantidade de pessoas cadastradas foi de ', c, 'pessoas.\n', contamaiores, 'pessoas possuem mais de 18 anos.\n', contahomem, 'pessoas são homens.\n', contamulhermenos, 'mulheres possuem menos de 20 anos.')
        break
print('Operação finalizada')