def soma(num1, num2):  # Definição da função soma
    calculo = num1 + num2
    print(f'O resultado da soma é {calculo}')

def sub(num1, num2):  # Definição da função subtração
    subtracao = num1 - num2
    print(f'O resultado da subtração é {subtracao}')

def multiplicacao(num1, num2):  # Definição da função multiplicação
    mult = num1 * num2
    print(f'O resultado da multiplicacao é {mult}')
    return mult  # Retorna o valor de mult para ser usado depois

num1 = int(input('Digite o primeiro número: '))
num2 = int(input('Digite o segundo número: '))

soma(num1, num2)  # Chamada da função soma
sub(num1, num2)   # Chamada da função subtração
mult_result = multiplicacao(num1, num2)  # Captura o resultado da multiplicação

# Abertura do arquivo para escrita
file = 'arquivo.txt'
arquivo_escrita = open(file, "w")  # Abre o arquivo para escrita
arquivo_escrita.write(f'O resultado da multiplicacao é {mult_result}')
arquivo_escrita.close()  # Fecha o arquivo após escrever

# Leitura do arquivo
arquivo_leitura = open(file, "r")  # Abre o arquivo para leitura
leitura = arquivo_leitura.read()
print(leitura)
arquivo_leitura.close()  # Fecha o arquivo após ler
