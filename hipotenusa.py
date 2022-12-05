import math
cat1 = float(input('Insira o valor do cateto oposto: '))
cat2 = float(input('Insira o valor do cateto adjacente: '))
hipo = math.hypot(cat1,cat2)
print('O valor da hipotenusa é: ', hipo)