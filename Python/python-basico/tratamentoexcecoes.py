# Tratamento de exceções

def divisao(a, b):
    try:
        calculo = a / b
        print(calculo)
    except ZeroDivisionError:
        print("Erro: impossível dividir um valor por zero")
    except TypeError as e:
        print(f'Erro: o tipo do dado está errado. \n Detalhes: {e}')
    else:
        print('sem excecoes')

# Chamada da função divisao com dados incorretos
divisao(10, 'leticia')
