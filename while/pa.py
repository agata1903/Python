primeiro = int(input('Primeiro termo: '))
razao = int(input('Razão: '))
termo = primeiro
cont = 1
while cont <=10:
    print(termo, '-> ',end='')
    termo += razao
    cont +=1
print('Fim do programa')