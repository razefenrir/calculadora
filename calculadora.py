num1 = input('Digite o primeiro numero à ser calculado: ')
num2 = input('Digite o segundo numero à ser calculado: ')
op = input('Digite a operação desejada(+(adição) -(subtração) x(multiplicação) /(divisão)): ')

if num1 and num2.isnumeric() == True:
    num1int = int(num1)
    num2int = int(num2)
    if op == '+':
        ad = num1int + num2int
        print(f'O resultado da soma entre {num1int} e {num2int} é de {ad}')

    elif op == '-':
        sb = num1int - num2int
        print(f'O resultado da subtração entre {num1int} e {num2int} é de {sb}')

    elif op == '/':
        if num1int != 0:
            dv = num1int / num2int
            print(f'O resultado da divisão entre {num1int} e {num2int} é de {dv}')
        else:
            print('0 não é um numero válido para a operação.')

    elif op == 'x' or 'X':
        mt = num1int * num2int
        print(f'O resultado da multiplicação entre {num1int} e {num2int} é de {mt}')

    else:
        print('Operação inválida, por favor tente novamente.')
else:
    print('Apenas numeros são válidos para o programa.')