r1 = float(input('Digite o primeiro segmento: '))
r2 = float(input('Digite o segundo segmento: '))
r3 = float(input('Digite o terceiro segmento: '))

if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print('Pode ser um triângulo')
    if r1 == r2 and r1 == r3:
        print('Este triângulo é um triângulo EQUILÁTERO')
    elif r1 == r2 and r1 != r3:
        print('Este triângulo é um triângulo ISÓSCELES')
    else:
        print('Este triângulo é um triângulo ESCALENO')
else:
    print('Não pode ser um triângulo')


