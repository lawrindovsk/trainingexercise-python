import this
import ExModels
this.opcao = 1
this.bas = -1
this.alt = -1
def Menu():
    print('Menu \n\n ' +
          '\n1. Exercicio 01 ' +
          '\n2. Exercicio 02 ' +
          '\n3. Exercicio 03 ' +
          '\n4. Exercicio 04 ' +
          '\n5. Exercicio 05 ' +
          '\n6  Exercicio 06 ' +
          '\n7  Exercicio 07 ' +
          '\n8  Exercicio 08 ' +
          '\n9  Exercicio 09 ' +
          '\n10 Exercicio 10 ' +
          '\n10 Exercicio 11 ' +
          '\n10 Exercicio 12 ' +
          '\n10 Exercicio 13 ' +
          '\n10 Exercicio 14 ' +
          '\n10 Exercicio 15 ' +
          '\n10 Exercicio 16 ' +
          '\n10 Exercicio 17 ' +
          '\n10 Exercicio 18 ' +
          '\n10 Exercicio 19 ' +
          '\n10 Exercicio 20 ' +
          '\n0. Sair' +
          '\nEscolha uma das opções acima: ')
    this.opcao = int (input())

def Executar():
    while(this.opcao != 0):
        Menu()
        if this.opcao == 0:
            print("Obrigado!")
        elif this.opcao == 1:
            print(ExModels.exercicio01())
        elif this.opcao == 2:
            print(ExModels.exercicio02())
        elif this.opcao == 3:
            while bas <= 0:
                if bas <= 0:
                    print('Informe a base do retângulo:')
                    if this.bas <= 0:
                        print('Informe uma base com valor positivo')

                        while this.alt <= 0:
                            print('Informe a altura do retângulo: ')
                        this.alt = float(input())
                        if this.alt <= 0:
                            print('Informe uma altura com valor positivo')

            print(ExModels.exercicio03(this.bas, this.alt))
        elif this.opcao == 4:
            print(ExModels.exercicio04())
        elif this.opcao == 5:
            print(ExModels.exercicio05())
        elif this.opcao == 6:
            print(ExModels.exercicio06())
        elif this.opcao == 7:
            print(ExModels.exercicio07())
        elif this.opcao == 8:
            print(ExModels.exercicio08())
        elif this.opcao == 9:
            print(ExModels.exercicio09())
        elif this.opcao == 10:
            print(ExModels.exercicio10())
        elif this.opcao == 11:
            print(ExModels.exercicio11)
        elif this.opcao == 12:
            print(ExModels.exercicio12)
        elif this.opcao == 13:
            print(ExModels.exercicio13)
        elif this.opcao == 14:
            print(ExModels.exercicio14)
        elif this.opcao == 15:
            print(ExModels.exercicio15)
        elif this.opcao == 16:
            print(ExModels.exercicio16)
        elif this.opcao == 17:
            print(ExModels.exercicio17)
        elif this.opcao == 18:
            print(ExModels.exercicio18)
        elif this.opcao == 19:
            print(ExModels.exercicio19)
        elif this.opcao == 20:
            print(ExModels.exercicio20)


        else:
            print('Opção informada não é válida!')