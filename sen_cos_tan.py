import math
num = int(input('Digite um número: '))
seno = math.sin(math.radians(num))
cosseno = math.cos(math.radians(num))
tangente = math.tan(math.radians(num))

print('O seno de ',num, ' é ', seno, end='.\n')
print('O cosseno de ',num, ' é ', seno, end='.\n')
print('A tangente de ',num, ' é ', seno, end='.')