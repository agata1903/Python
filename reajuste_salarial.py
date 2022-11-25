funcionario = input('Digite o nome do funcionário: ')
salario = float(input('Digite o salário atual: '))
reajuste = int(input('Em quantos % você quer reajustar o salário deste funcionário?'))

valor_do_reajuste = reajuste/100

valor_reajustado = salario * valor_do_reajuste

salario_com_reajuste = valor_reajustado + salario
print('O funcionário ', funcionario, ', que recebia R$', salario, ', teve um reajuste salarial, e agora recebe R$', salario_com_reajuste)