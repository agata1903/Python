n1 = int(input('Primeiro valor: '))
n2 = int(input('Segundo valor: '))
opcao = 0
while opcao != 5:
    print('[1]Somar\n''[2]Multiplicar\n''[3]Maior\n''[4]Novos números\n''[5]Sair')
    opcao = int(input('Qual a sua opção? '))
    if opcao == 1:
        print('A soma entre ',n1, 'e',n2,'é ',n1 + n2)
    elif opcao == 2:
        print('A multiplicação entre ',n1, 'e',n2,'é ',n1 * n2)
    elif opcao == 3:
        print('O maior número entre ',n1, 'e',n2,'é ',max(n1,n2))
    elif opcao == 4:
        opcao = print('Digite novamente os números desejados: ')
        n1 = int(input('Primeiro valor: '))
        n2 = int(input('Segundo valor: '))
    elif opcao == 5:
        print('Tchau!')
    else:
        print('Erro, digite uma opção válida!')
print('Fim do programa')