numero = int(input('Insira um número qualquer: '))
base = int(input('Agora, a base de conversão: Para binário, digite "1", para octal, digite "2", e para hexadecimal, digite "3"'))

if base == 1:
    print('O número ',numero, 'convertido para binário fica ',bin(numero))
elif base == 2:
    print('O número ',numero, 'convertido para octal fica ',oct(numero))
else:
    print('O número ',numero, 'convertido para hexadecimal fica ',hex(numero))
