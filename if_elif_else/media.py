nota1 = float(input('Digite a primeira nota: '))
nota2 = float(input('Digite a segunda nota: '))
nota3 = float(input('Digite a terceira nota: '))
nota4 = float(input('Digite a quarta nota: '))

media = (nota1 + nota2 + nota3 + nota4)/4

if media <=5:
    print('O aluno está reprovado!')
elif 5.1 <= media <= 6.9:
    print('O aluno está em recuperação!')
else:
    print('O aluno está reprovado!')
