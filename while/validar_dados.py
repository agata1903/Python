sexo = str(input('Digite seu sexo: Escolha "M" para masculino e "F" para feminino: ')).strip().upper()[0]
while sexo not in 'MmFm':
    sexo = str(input('Dados inválidos, digite novamente: ')).strip().upper()[0]
print('Registrado com sucesso!')