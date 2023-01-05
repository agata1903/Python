p = float(input('Digite seu peso: '))
a = float(input('Digite sua altura: '))
imc = p/(a*a)
print(imc)
if imc < 18.5:
    print('Você está abaixo do índice ideal!')
elif imc >= 18.5 and imc <= 24.9:
    print('Você está no índice ideal!')
else:
    print('Você está acima do peso!')