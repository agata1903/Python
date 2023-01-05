termo = int(input('Digite o primeiro termo: '))
razao = int(input('Digite a razão: '))
dec = termo + (10 - 1) * razao
for i in range(termo,dec + razao,razao):
    print(i, end=' ')