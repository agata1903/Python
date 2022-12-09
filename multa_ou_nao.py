km = int(input('Digite a quilometragem: '))
dif = km - 80
multa = 7*dif

if km > 80:
    print('Seu danadinho, desrespeitando as leis de trânsito, né? Sua multa será de R$', multa, end=',00')
else:
    print('Pode passar, meu jovem, tenha uma boa viagem!')