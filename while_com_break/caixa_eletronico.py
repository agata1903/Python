valor = total = 0

valor = float(input('Digite quanto pretende sacar: '))
total = valor
cedula = 50
totalcedula = 0
while True:
    if total >= cedula:
        total -= cedula
        totalcedula += 1
    else:
        print('Total de ', totalcedula, ' cédulas de ', cedula)
        if cedula == 50:
            cedula = 20
        elif cedula == 20:
            cedula = 10
        elif cedula == 10:
            cedula = 5
        totalcedula = 0
        if total == 0:
            break

