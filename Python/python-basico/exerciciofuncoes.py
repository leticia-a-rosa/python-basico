#nome = input('Digite seu nome (em letras minusculas): ')
#print(nome[:])   #Pegando a string do início ao fim
#print(nome[::-1]) # Slicing com passo negativo


# 1 Faça um programa, com uma função que necessite de três argumentos, e que forneça a soma desses três argumentos

# Função para calcular as calorias da tapioca
def calcular_calorias_crepioca (tapioca, ovo, queijo):
    return tapioca + ovo + queijo

# Definir as calorias por unidade
tapioca = 50  # Calorias por tapioca
ovo = 10      # Calorias por ovo
queijo = 15   # Calorias por queijo

# Solicitar a quantidade de tapiocas
qtde= int(input('Digite a quantidade de tapiocas que irá comer: '))

calorias_totais = qtde*(calcular_calorias_crepioca (tapioca, ovo, queijo))
print(f'A quantidade de calorias são {calorias_totais}')

#2. Reverso do número. Faça uma função que retorne o reverso de um número inteiro informado. Por exemplo: 127-> 721

nome = input('Digite seu nome (em letras minusculas): ')
print(nome[:])   #Pegando a string do início ao fim
print(nome[::-1]) # Slicing com passo negativo


numero = (input('Digite o numero que voce deseja o reverso: '))
print(numero[:]) #pegando o numero do inicio ao fim
print(numero[::-1]) #slicing com o passo negativo

numero = input('Digite o numero que voce deseja o reverso: ')
numero_lista = list(numero)  # Converte a string em uma lista de caracteres
numero_lista.reverse()  # Reverte a lista
numero_reverso = ''.join(numero_lista)  # Junta a lista de volta em uma string
print(numero_reverso)  # Imprime o número reverso

#3. Escreva um script que pergunta ao usuário se ele deseja converter
 #uma temperatura de grau Celsius para Fahrenheit ou vice-versa. Para
 #cada opção, crie uma função.

# Função para converter Celsius para Fahrenheit
def celsius_para_fahrenheit(celsius):
    return (celsius * 9/5) + 32

# Função para converter Fahrenheit para Celsius
def fahrenheit_para_celsius(fahrenheit):
    return (fahrenheit - 32) * 5/9

# Pergunta ao usuário qual conversão ele deseja
opcao = input("Você deseja converter de Celsius para Fahrenheit (C) ou de Fahrenheit para Celsius (F)? ")

if opcao.lower() == 'c':
    celsius = float(input("Digite a temperatura em Celsius: "))
    fahrenheit = celsius_para_fahrenheit(celsius)
    print(f"{celsius}°C é igual a {fahrenheit}°F")
elif opcao.lower() == 'f':
    fahrenheit = float(input("Digite a temperatura em Fahrenheit: "))
    celsius = fahrenheit_para_celsius(fahrenheit)
    print(f"{fahrenheit}°F é igual a {celsius}°C")
else:
    print("Opção inválida! Por favor, digite 'C' ou 'F'.")


 #4. Crie um programa que leia quanto dinheiro uma pessoa tem na
 #carteira, e calcule quanto poderia comprar de cada moeda estrangeira.
 #Considere a tabela de conversão abaixo:
 #Dólar Americano: R$ 4,91
 #Peso Argentino: R$ 0,02
 #Dólar Australiano: R$ 3,18
 #Dólar Canadense: R$ 3,64
 #Franco Suiço: R$ 0,42
 #Euro: R$ 5,36
 #Libra esterlina: R$ 6,21
# Tabela de conversão
taxas = {
    "dolar_americano": 4.91,
    "peso_argentino": 0.02,
    "dolar_australiano": 3.18,
    "dolar_canadense": 3.64,
    "franco_suico": 0.42,
    "euro": 5.36,
    "libra_esterlina": 6.21
}

# Pergunta ao usuário quanto ele tem na carteira
euro = float(input("Quantos euros você tem? "))
dolar_americano = float(input("Quantos dólares americanos você tem? "))
dolar_australiano = float(input("Quantos dólares australianos você tem? "))
dolar_canadense = float(input("Quantos dólares canadenses você tem? "))
peso_argentino = float(input("Quantos pesos argentinos você tem? "))
franco_suico = float(input("Quantos francos suíços você tem? "))
libra_esterlina = float(input("Quantas libras esterlinas você tem? "))

# Calcula o valor total em reais
total_reais = (euro * taxas["euro"] +
               dolar_americano * taxas["dolar_americano"] +
               dolar_australiano * taxas["dolar_australiano"] +
               dolar_canadense * taxas["dolar_canadense"] +
               peso_argentino * taxas["peso_argentino"] +
               franco_suico * taxas["franco_suico"] +
               libra_esterlina * taxas["libra_esterlina"])

print(f"O valor total em reais é: R$ {total_reais:.2f}")

# 5 Crie uma função chamada contar_vogais que recebe uma string
#  como parâmetro. Implemente a lógica para contar o número de vogais
#  na string e retorne o total de vogais. Solicite ao usuário para inserir uma
#  frase e utilize a função para contar as vogais.

# vogais = "aeiouAEIOU"
# num_vogais = 0

# consoantes ="bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ"
# num_consoantes = 0

# palavra = input('digite a palavra: ')

# for char in palavra:
#     if char in vogais:
#         num_vogais += 1
#     elif char in consoantes:
#         num_consoantes += 1

# print(f'O número de vogais é: {num_vogais}')
# print(f'O número de consoantes é: {num_consoantes}')

def contar_vogais_consoantes(palavra):
    vogais = "aeiouAEIOU"
    consoantes = "bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ"
    num_vogais = 0
    num_consoantes = 0

    for char in palavra:
        if char in vogais:
            num_vogais += 1
        elif char in consoantes:
            num_consoantes += 1

    return num_vogais, num_consoantes

# Usuario digitando a palavra
palavra = input('Digite a palavra: ')
num_vogais, num_consoantes = contar_vogais_consoantes(palavra)
print(f'O número de vogais é: {num_vogais}')
print(f'O número de consoantes é: {num_consoantes}')


#  6. Vamos construir um jogo de forca. O programa escolherá
#  aleatoriamente uma palavra secreta de uma lista predefinida. A palavra
#  secreta será representada por espaços em branco, um para cada letra
# da palavra. O jogador terá um número limitado de 6 tentativas. Em cada
#  tentativa, o jogador pode fornecer uma letra. Se a letra estiver presente
#  na palavra secreta, ela será revelada nas posições correspondentes. Se
#  a letra não estiver na palavra, uma mensagem de erro deverá ser
#  informada. Após um número máximo de erros, o jogador perde. O jogo
#  continua até que o jogador adivinhe a palavra ou exceda o número
#  máximo de tentativas.
#  Dica: Você precisará importar uma biblioteca para resolver esse
#  exercício


import random

palavras = []
palavra_aleatoria = random.choice(palavras)
