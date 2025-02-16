#funcoes:grupo de instruções relcaionadas que executa uma tarefa
#declaração def mostrar_mensagem(): instruções ficam dentro da funcao
#chamada da função mostrar_mensagem()
#declara/define e depois chama a função
#variaveis nao pode ter o mesmo nome da função

#def soma(): #definicao da funcao soma
#    calculo = 10+2
#    print(f'o resultado da soma é {calculo}')

#def sub(): #definição da funcao subtração
#    subtracao = 10-8
#    print(f'o resultado da subratação é {subtracao}')
#    multiplicacao() #chamada de função dentro da funcao

#def multiplicacao(): #definicao da funcao multiplicação
#    mult = 10*2
#    print(f'o resultado da multiplicacao é {mult}')

#soma() #chamada da subtração
#sub()

#parametros - nao ter numeros fixos - deixar o usuario digitar. o que é enviado precisa ser chamado
def soma(num1, num2):  # Definição da função soma
    calculo = num1 + num2
    print(f'O resultado da soma é {calculo}')

def sub(num1, num2):  # Definição da função subtração
    subtracao = num1 - num2
    print(f'O resultado da subtração é {subtracao}')

def multiplicacao(num1, num2):  # Definição da função multiplicação
    mult = num1 * num2
    print(f'O resultado da multiplicação é {mult}')

num1 = int(input('Digite o primeiro número: '))
num2 = int(input('Digite o segundo número: '))

soma(num1, num2)  # Chamada da função soma
sub(num1, num2)   # Chamada da função subtração
multiplicacao(num1, num2)  # Chamada da função multiplicação


