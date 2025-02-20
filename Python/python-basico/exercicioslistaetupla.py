#1
# Fazendo perguntas para o usuário
p1 = int(input("Telefonou para a vítima? Digite 1 para sim e 0 para não. "))
p2 = int(input("Esteve no local do crime? Digite 1 para sim e 0 para não. "))
p3 = int(input("Mora perto da vítima? Digite 1 para sim e 0 para não. "))
p4 = int(input("Devia para a vítima? Digite 1 para sim e 0 para não. "))
p5 = int(input("Já trabalhou com a vítima? Digite 1 para sim e 0 para não. "))

# Classificando a pessoa
respostas = [p1, p2, p3, p4, p5]
soma = sum(respostas)

if soma == 2:
    print("Suspeita")
elif soma == 3 or soma == 4:
    print("Cúmplice")
elif soma == 5:
    print("Assassino")
else:
    print("Inocente")

#2
notas_alunos = []
medias = []

for i in range(5):  # Para cada um dos 5 alunos
    notas = []
    for j in range(4):  # Para cada uma das 4 notas
        while True:
            nota = float(input(f'Digite a nota {j+1} do aluno {i+1}: '))
            if nota < 0 or nota > 10:
                print("Nota inválida. Digite uma nota entre 0 e 10.")
            else:
                break
        notas.append(nota)
    notas_alunos.append(notas)

for notas in notas_alunos:
    media = sum(notas) / 4
    medias.append(media)

for i, media in enumerate(medias):
    print(f'A média do aluno {i+1} é {media}')

#3
# Criando dicionario do carrinho de compras
carrinho = {
    'Arroz - 5kg': 2,
    'Café - 500gr': 1,
    'Leite Condensado Lata': 3,
    'Ovos - Duzia': 1,
    'Banana - 1kg': 5
}

# Criando dicionário de preços
precos = {
    'Arroz - 5kg': 28,
    'Café - 500gr': 26,
    'Leite Condensado Lata': 9,
    'Ovos - Duzia': 13,
    'Banana - 1kg': 10
}

# Calculando o total do carrinho de compras
total = 0
for produto, quantidade in carrinho.items():
    total += quantidade * precos[produto]

print(f'O total do carrinho de compras é R${total:.2f}')

#4
# Criando dicionario da agenda telefonica
telefones = {
    'Maria': '11-5689-3256',
    'João': '11-7896-4585',
    'Lucas': '11-5632-7412',
    'Luana': '11-9965-7852',
    'Samanta': '11-2365-4528'
}

#chave = Nome
#valor= telefone
Nome = input('Digite o nome do contato que deseja procurar: ')

if Nome in telefones:
  print(f'o telefone do {Nome} é {telefones[Nome]}')
else:
  print('Contato não encontrado na agenda')


#5
# Criando duas tuplas
nomes = ('Leticia', 'Gustavo')
nascimento = (1988, 1997)

# Concatenando as duas tuplas
nova_tupla = nomes + nascimento

# Exibindo a nova tupla
print(nova_tupla)