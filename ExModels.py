def exercicio01():
    A = 10
    B = 20
    msg = 'Antes da troca: A = {}, B = {}'.format(A, B)
    aux = A
    A = B
    B = aux
    msg = msg + '\nDepois da Troca: A = {}, B = {}'.format(A, B)
    return msg


def exercicio02():
    A = int(input('Digite o número que você deseja: '))
    B = A - 1
    print('O seu número A {}, e o seu antecessor é B = {}'.format(A, B))


def exercicio03():
    bas = float(input('Digite a Base: '))
    alt = float(input('Digite a Altura: '))
    c = bas * alt
    return print('O Resultado é de : c {} '.format(c))


def exercicio04():
    idade = int(input('Qual sua idade? '))
    ano = 365
    mes = 30
    A = idade * ano + mes

    print('O tatal vidas que você tem é de A {} '.format(A))


def exercicio05():
    votos = int(input('Quantos votos teve no municipio? '))
    white = int(input('Quantos votos Brancos? '))
    nulos = int(input('Quantos votos Nulos? '))
    validos = int(input('Quantos vatos invalidos? '))
    d = 100
    A = (votos / white) * d
    B = (votos / nulos) * d
    C = (votos / validos) * d

    print('A porcentagem dos votos Branco é de white: {} '.format(A))
    print('A porcentagem dos votos Branco é de nulos: {} '.format(B))
    print('A porcentagem dos votos Branco é de validos: {} '.format(C))


def exercicio06():
    salario = float(input('Qual é o seu salário? '))
    perc = float(input('Qual a porcentagem que você quer adicionar? '))
    A = salario + (salario * perc / 100)
    print('Seu novo salario é de A = {}  '.format(A))


def exercicio07():
    fabrica = float(input('Qual valor do carro? '))
    novoValor = (fabrica + fabrica * 0.45 + fabrica * 0.28)
    print('O novo valor do carro é de novoValor = {}'.format(novoValor))


def exercicio08():
    nota1 = float(input('Qual a primeira nota?'))
    nota2 = float(input('Qual a segunda nota? '))
    nota3 = float(input('Qual a terceira nota? '))
    notaFinal = (nota1 + nota2 + nota3 / 10)
    print('A nota total do aluno foi de notaFinal = {} '.format(notaFinal))


def exercicio09():
    maca = 1.30
    maca2 = 1.00
    question = int(input(('Qual a quantidade de maças você quer comprar? ')))

    if maca > 11:
        maca * 1
        print('A Maça custa maca = {}'.format(maca))
    else:\
        maca2 < 12
    maca2 * 1
    print('A Maça custa maca2 = {} '.format(maca2))

def exercicio10():
    for n in range(0, 11):
        print('Os némeros na ordem crescentes são numero = {} '.format(n))

def exercicio11():
    salario = float(input('Digite seu salário fixo em R$:'))
    vendas = float(input('Digite o total das suas vendas em R$: '))
    if vendas >= 1500.0:
            c5 = (5*(vendas-1500))/100
            c3 = (3*vendas)/100
            total = salario+c3+c5

            return 'Parabéns, além do comissionamento de 3%, você atigiu o bônus de 5%, seu salário total será R${}'.format(total)
    else:
            c3 = (3/vendas)*100
            total = salario + c3

            return 'Seu salário total será R${}'.format(total)

def exercicio12():
    conta = int(input('Digite o número da sua conta:'))
    saldo = float(input('Digite seu saldo em R$:'))
    debito = float(input('Digite o débito que você possui em R$:'))
    credito = float(input('Digite o seu crédito em R$:'))

    saldoatual = saldo - debito + credito
    if saldoatual >= 0:
        return 'Saldo Positivo, seu saldo atual é de R${}'.format(saldoatual)

    else:
        return 'Saldo Negativo, seu saldo atual é de -R${}' .format(saldoatual)

def exercicio13():
    n = int(input('Digite um valor entre 1 e 10: '))
    if n > 10:
        return 'Opção inválida, digite um valor entre 1 e 10'
    elif n<0:
        return 'Opção inválida, digite um valor entre 1 e 10'
    else:
        for i in range(1, 11):
            resultado = n*i
            print('{} * {} = {}'.format(n, i, resultado))

def exercicio14():
    n = int(input('Digite um número: '))
    for i in range(1, n+1):
        print(i)

def exercicio15():
    lista = 0
    for i in range(1,11):
        n = int(input('Digite um número: '))
        if n<0:
            lista += +1

    return '\nSua lista possui {} números negativos' .format(lista)

def exercicio16():
    lista = 0
    for i in range(1, 11):
        n = float(input('Digite um número: '))
        if n<40:
            lista += n

    return '\nO resultado da sua soma é {}' .format(lista)

def exercicio17():
    aux = 0
    quantidade = 0
    for i in range(1, 101):

        aux += i
        quantidade += +1
        result = aux/quantidade

    return '\n{} / {} = {}' .format(aux, quantidade, result)

def exercicio18():
   n = int(input('Quantos números deseja digitar? '))
   if n<=0:
       print('Obrigado!')
   else:
    aux3 = 0
    quantidade = 1

    maior = float(input('Digite um número: '))
    for i in range(2, n + 1):
        num = float(input('Digite um número: '))

        aux2 = maior
        aux3 += num
        quantidade += +1
        media = (aux2+aux3)/quantidade

        if num>maior:
            maior = num

    print ('O maior número digitado foi {}'.format(maior))
    print('A média dos números digitados foi {}' .format(media))

def exercicio19():
    total = 0
    maior = 0
    lista = []
    for i in range(20):
        notas = float(input('Digita sua nota de 0 a 10: '))
        lista.append(notas)
        if notas>10:
            print('Digite uma nota válida')
        elif notas<0:
            print('Digite uma nota válida')
        else:
            total += notas
            mediag = total / 20

    for i in range(20):
       if lista[i] > mediag:
          maior += 1

    print('A média da turma foi {}.'.format(mediag))
    print('{} aluno(s) tiveram nota maior que a média'.format(maior))

def exercicio20():
    medias = 0
    mediaf = 0
    aux = 0
    abaixo = 0

    habitantes = int(input('Digite a quantidade de habitantes: '))
    for i in range(1, habitantes+1):
        salario = float(input('Digite seu salário em R$: '))
        if salario<=150.0:
            abaixo = +1
        if aux<salario:
            aux = salario
        if salario<0:
            print('Salário inválido')
        filhos = int(input('Digite a quantidade de filhos que você possui: '))
        if filhos<0:
            print('Quantidade inválida')

        medias += salario
        mediaf += filhos
    results = medias/habitantes
    resultf = mediaf/habitantes
    resultmenor = (abaixo/habitantes)*100

    print('Média do salário da população R$:{}' .format(results))
    print('Média número de filhos por habitante: {}' .format(resultf))
    print('Maior salário dos habitantes, R$:{}'.format(aux))
    print('Há {}% de pessoas com salário abaixo de R$150.0'.format(resultmenor))
