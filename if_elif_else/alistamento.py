from datetime import date
hoje = date.today().year
nascimento = int(input('Digite o ano de nascimento: '))
idade = date.today().year - nascimento
falta = 18 - idade
passou = idade - 18
if idade < 18:
    print('Você ainda não está no tempo de se alistar. Ainda faltam ', falta, 'anos para você se alistar!')
elif idade == 18:
    print('Você está no tempo de se alistar, se não foi, vá logo!')
else:
    print('Você passou do tempo de alistamento! Já fazem ', passou, 'anos que você se alistou!')
