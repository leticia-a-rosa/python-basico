#Faça um Programa que peça dois números, realize as principais operações soma, subtração, multiplicação, divisão
try:
    num1 = float(input("Digite o primeiro número: "))
    num2 = float(input("Digite o segundo número: "))

    soma = num1 + num2
    sub = num1 - num2
    mult = num1 * num2
    div = num1 / num2

    print(f'O resultado da soma é {soma}')
    print(f'O resultado da subtração é {sub}')
    print(f'O resultado da multiplicação é {mult}')
    print(f'O resultado da divisão é {div}')

except ZeroDivisionError:
    print("Erro: Divisão por zero não é permitida.")

# 2. Peça ao usuário para informar o ano de nascimento. Em seguida, calcule e imprima a idade atual.
nasc = int(input('Informe seu ano de nascimento: '))
idade = 2025 - int(nasc)
print(f'sua idade atual é {idade}')



# 3. Faça um Programa que peça a quantidade de quilômetros, transforme em metros, centímetros e milímetros.
km = int(input('Informe a quantidade de quilometros: '))
m = 1000 * int(km)
cm = 1000 * 100 * int(km)
mm = 1000 * 100 * 10 * int(km)
print(f'Isso equivale a {m} metros')
print(f'Isso equivale a {cm} centimetros')
print(f'Isso equivale a {mm} milimetros')


# 4. Receba do usuário a quantidade de litros de combustível consumidos e a distância percorrida. Calcule e imprima o consumo médio em km/l.
litros = int(input('Digite a quantidade de combustível consumidos em litros: '))
distancia = int(input('Digite a distância percorrida em quilometros: '))
consumo = distancia/litros
print(f'O consumo médio é de {consumo} km/l')


# 5. Escreva um programa que calcule o tempo de uma viagem. Faça um comparativo do mesmo percurso de avião, carro e ônibus.
# Levando em consideração:
# ● avião = 600 km/h
# ● carro = 100 km/h
# ● ônibus = 80 km/h

def calcular_tempo_viagem(distancia, velocidade):
    return distancia / velocidade

# Solicitar a distância do percurso ao usuário
distancia = float(input("Digite a distância do percurso em km: "))

# Velocidades dos meios de transporte (em km/h)
velocidade_aviao = 600
velocidade_carro = 100
velocidade_onibus = 80

# Calculando o tempo de viagem para cada meio de transporte
tempo_aviao = calcular_tempo_viagem(distancia, velocidade_aviao)
tempo_carro = calcular_tempo_viagem(distancia, velocidade_carro)
tempo_onibus = calcular_tempo_viagem(distancia, velocidade_onibus)

print(f"Tempo de viagem de avião: {tempo_aviao} horas")
print(f"Tempo de viagem de carro: {tempo_carro} horas")
print(f"Tempo de viagem de ônibus: {tempo_onibus} horas")


# 6. Solicite ao usuário o peso em kg e a altura em metros. Calcule e imprima o Índice de Massa Corporal (IMC) usando a fórmula:
# IMC = peso / (altura x altura).
peso = float(input('Digite seu peso em kg: '))
altura = float(input('Digite sua altura em metros: '))
IMC = peso / (altura*altura)
print(f'Seu IMC é {IMC}')


# 7. Faça um Programa que pergunte quanto você ganha por hora e o
# número de horas trabalhadas no mês.Calcule e mostre o total do seu
# salário no referido mês.
# 8.
# Solicite ao usuário o número de horas de exercício físico por semana.
# Calcule o total de calorias queimadas em um mês, considerando uma
# média de 5 calorias por minuto de exercício.
#9. Faça um Programa que utilize 4 variáveis como preferir e no final print
# uma mensagem amigável utilizando as variáveis criadas.
# Exemplos de variáveis: nome, idade, lugar, profissão ....
# Exemplo de retorno: Olá Maria, prazer te conhecer. Sou de São Paulo
# também e estou migrando de área.
# Lembrando que para o retorno vamos usar print com as variáveis
# criadas e este texto é somente um exemplo, utilizem a criatividade