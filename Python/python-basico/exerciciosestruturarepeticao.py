#1. Faça um Programa que peça dois números e imprima o maior deles.
num1=int(input("Digite o primeiro número: "))
num2=int(input("Digite o segundo número: "))
lista_numeros=[num1,num2]
maximo=max(lista_numeros)
print(f"O maior número é: {maximo}")


#2. Faça um Programa que pergunte em que turno você estuda. Peça para digitar M-matutino ou V-Vespertino ou N- Noturno. Imprima a mensagem "Bom Dia!", "Boa Tarde!" ou "Boa Noite!" ou "Valor Inválido!", conforme o caso.
turno = input("Em qual turno você estuda? Digite M para matutino, V para vespertino ou N para noturno: ")
if turno.upper() == "M":
    print("Bom Dia!")
elif turno.upper() == "V":
    print("Boa Tarde!")
elif turno.upper() == "N":
    print("Boa Noite!")
else:
    print("Valor Inválido!")

# 3. Faça um programa que peça uma nota, entre zero e dez. Mostre uma mensagem caso o valor seja inválido e continue pedindo até que o usuário informe um valor válido.
nota = float(input('Digite uma nota entre 0 e 10: '))
if nota < 0 or nota > 10:
    print('Nota inválida')
else:
    print('Nota válida')

# 4. Implemente um programa que classifique um aluno com base em sua pontuação em um exame. O programa deverá solicitar uma nota de 0 a 10. Se a pontuação for maior ou igual a 7, o aluno é aprovado; caso contrário, é reprovado.
nota = float(input('Digite uma nota entre 0 e 10: '))
if nota < 0 or nota > 10:
    print('Nota inválida')
else:
    if nota >= 7:
        print('Aluno aprovado')
    else:
        print('Aluno reprovado')

 5. Desenvolva um programa que solicite ao usuário os comprimentos dos três
 lados de um triângulo e classifique-o como equilátero, isósceles ou escaleno.
 equilátero: todos os lados com o mesmo valor
 isósceles: dois lados com o mesmo valor
 escaleno: todos os lados com medidas distintas.
 6. Crie um programa que solicite ao usuário um login e uma senha. O
 programa deve permitir o acesso apenas se o usuário for "admin" e a senha
 for "admin123", caso contrário imprima uma mensagem de erro.
 7. Desenvolver um programa que solicite a idade do usuário e identifique se
 ele é uma criança, um adolescente, adulto ou idoso.
 8. Criar um programa em Python que solicite três números ao usuário, utilize
 estruturas condicionais para determinar o maior entre eles e apresente o
 resultado