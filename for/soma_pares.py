soma = 0
cont = 0
for i in range(1,7):
    num = int(input('Digite um número: '))
    if num %2 == 0:
        soma = soma + num
        cont = cont + 1
print('A soma entre os ', cont, 'números é igual a ',soma)