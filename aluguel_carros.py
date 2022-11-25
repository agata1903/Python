dias = int(input('Digite a quantidade de dias alugados: '))
custo_dia = dias * 60
km = float(input('Digite a quantidade de km rodados: '))
custo_km = km * 0.15

custo_total = custo_dia + custo_km
print('Você rodou por ', dias, 'dias e ', km, 'km. Você deverá pagar R$', custo_total)