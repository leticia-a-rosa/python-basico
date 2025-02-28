#import sqlite3

#try:
    #conexao = sqlite3.connect('C:/Users/letti/OneDrive/Área de Trabalho/Estudos/Bootcamp Data Analyst Womakercode/SQL/meu_primeiro_banco')
    #cursor = conexao.cursor()
    #cursor.execute('CREATE TABLE usuarios (id INT, nome varchar(100), endereco varchar(150), email varchar(100));')
    #cursor.execute('CREATE TABLE gerente (id INT, nome varchar(100), endereco varchar(150), email varchar(100));')
    #cursor.execute('ALTER TABLE usuarios RENAME TO usuario')
    #cursor.execute('ALTER TABLE usuario ADD COLUMN telefoni INT')   
    #cursor.execute('ALTER TABLE usuario RENAME COLUMN telefoni TO telefone') 
    #cursor.execute('INSERT INTO usuario(id,nome,endereco,email,telefone) VALUES (1,"Isadora","França", "isa@gmail.com", 125463)')
    #cursor.execute('INSERT INTO usuario(id,nome,endereco,email,telefone) VALUES (2,"Maria","Brasilia", "maria@gmail.com", 789654)')
    #cursor.execute('INSERT INTO usuario(id,nome,endereco,email,telefone) VALUES (3,"Jose","Salvador", "jose@gmail.com", 963258)')
    #cursor.execute('INSERT INTO usuario(id,nome,endereco,email,telefone) VALUES (4,"Gustavo","São Paulo", "gustavo@gmail.com", 741258)')
    #cursor.execute('INSERT INTO usuario(id,nome,endereco,email,telefone) VALUES (5,"Heloisa","Rio de Janeiro", "heloisa@gmail.com", 789321)')
    #cursor.execute('DROP TABLE produtos')
    #cursor.execute('DELETE FROM usuario where id=1')
    #cursor.execute('UPDATE usuario SET endereco = "Minas Gerais" WHERE nome = "Jose"')
      
    #dados = cursor.execute('SELECT * FROM usuario ORDER BY nome ASC')
    
    #dados = cursor.execute('SELECT id FROM usuario GROUP BY nome having id>3')
    #cursor.execute('INSERT INTO gerente(id,nome,endereco,email) VALUES (1,"Isadora","França", "isa@gmail.com")')
    #cursor.execute('INSERT INTO gerente(id,nome,endereco,email) VALUES (2,"Maria","Brasilia", "maria@gmail.com")')
    #cursor.execute('INSERT INTO gerente(id,nome,endereco,email) VALUES (3,"Jose","Salvador", "jose@gmail.com")')
    #cursor.execute('INSERT INTO gerente(id,nome,endereco,email) VALUES (4,"Gustavo","São Paulo", "gustavo@gmail.com")')
    #cursor.execute('INSERT INTO gerente(id,nome,endereco,email) VALUES (5,"Heloisa","Rio de Janeiro", "heloisa@gmail.com")')
    #cursor.execute('INSERT INTO gerente(id,nome,endereco,email) VALUES (6,"Guilherme","Salvador", "guilherme@gmail.com")')
    #cursor.execute('INSERT INTO gerente(id,nome,endereco,email) VALUES (7,"Ana Paula","São Paulo", "anapaula@gmail.com")')
    #cursor.execute('INSERT INTO gerente(id,nome,endereco,email) VALUES (8,"Isabela","Goiania", "isabela@gmail.com")')

    #dados = cursor.execute('SELECT * FROM usuario INNER JOIN gerente on usuario.id = gerente.id')
    #dados = cursor.execute('SELECT * FROM usuario LEFT JOIN gerente on usuario.id = gerente.id')
    #dados = cursor.execute('SELECT * FROM usuario RIGHT JOIN gerente on usuario.id = gerente.id')
    #dados = cursor.execute('SELECT * FROM usuario FULL JOIN gerente on usuario.id = gerente.id')

#     dados = cursor.execute('SELECT * FROM usuario WHERE nome IN (SELECT nome FROM gerente)')
#     for usuario in dados:
#         print(usuario)
   
#     conexao.commit()
#     print("Tabela criada com sucesso!")
# except sqlite3.Error as erro:
#     print("Erro ao criar tabela:", erro)
# finally:
#     conexao.close()



import sqlite3


conexao = sqlite3.connect('C:/Users/letti/OneDrive/Área de Trabalho/Estudos/Bootcamp Data Analyst Womakercode/SQL/meu_primeiro_banco.db')
cursor = conexao.cursor()

    # Criar a tabela
    # cursor.execute('CREATE TABLE alunos (id INT, nome varchar(100), idade INT, curso varchar(100));')
    
    # Inserir 5 registros ou mais na tabela alunos
    # cursor.execute('INSERT INTO alunos(id,nome,idade,curso) VALUES (1,"Isadora",8, "financas pessoais")')
    # cursor.execute('INSERT INTO alunos(id,nome,idade,curso) VALUES (2,"Maria",9, "ingles para adolescentes")')
    # cursor.execute('INSERT INTO alunos(id,nome,idade,curso) VALUES (3,"Joao",10, "design grafico")')
    # cursor.execute('INSERT INTO alunos(id,nome,idade,curso) VALUES (4,"Pedro",11, "programação para iniciantes")')
    # cursor.execute('INSERT INTO alunos(id,nome,idade,curso) VALUES (5,"Ana",12, "programação para iniciantes")')
    # cursor.execute('INSERT INTO alunos(id,nome,idade,curso) VALUES (6,"Tereza",13, "programação para iniciantes")')
    # cursor.execute('INSERT INTO alunos(id,nome,idade,curso) VALUES (7,"Bento",14, "financas pessoais")')
    # cursor.execute('INSERT INTO alunos(id,nome,idade,curso) VALUES (8,"Luan",15, "redação e comunicação")')
    # cursor.execute('INSERT INTO alunos(id,nome,idade,curso) VALUES (9,"Camila",14, "ingles para adolescentes")')
    # cursor.execute('INSERT INTO alunos(id,nome,idade,curso) VALUES (10,"Patricia",15, "programação para iniciantes")')
    # cursor.execute('INSERT INTO alunos(id,nome,idade,curso) VALUES (10,"Patricia",15, "programação para iniciantes")')
    # cursor.execute('INSERT INTO alunos(id,nome,idade,curso) VALUES (11,"Bento",23, "engenharia")')
    # cursor.execute('INSERT INTO alunos(id,nome,idade,curso) VALUES (12,"Luan",27, "engenharia")')
    # cursor.execute('INSERT INTO alunos(id,nome,idade,curso) VALUES (13,"Camila",20, "nutricao")')
    # cursor.execute('INSERT INTO alunos(id,nome,idade,curso) VALUES (14,"Patricia",22, "programação para iniciantes")')
    
#Consultas Básicas
#Escreva consultas SQL para realizar as seguintes tarefas:
#a) Selecionar todos os registros da tabela "alunos".

    # dados = cursor.execute('SELECT * from alunos')
    # for alunos in dados:
    #      print(alunos)

#b) Selecionar o nome e a idade dos alunos com mais de 20 anos.

    # dados = cursor.execute('SELECT nome, idade FROM alunos WHERE idade>20')
    # for alunos in dados:
    #      print(alunos)



#c) Selecionar os alunos do curso de "Engenharia" em ordem alfabética.

# dados = cursor.execute('SELECT nome FROM alunos WHERE curso="engenharia" ORDER BY nome DESC')
# for alunos in dados:
#         print(alunos)


#d) Contar o número total de alunos na tabela

# dados = cursor.execute('SELECT COUNT(DISTINCT id) FROM alunos')
# for total in dados:
#     print(total[0])

# 4. Atualização e Remoção
# a) Atualize a idade de um aluno específico na tabela.
# cursor.execute('UPDATE alunos SET idade = 19 WHERE nome = "Maria"')

# b) Remova um aluno pelo seu ID.
#cursor.execute('DELETE FROM alunos where id=10')


# 5. Criar uma Tabela e Inserir Dados
# Crie uma tabela chamada "clientes" com os campos: id (chave primária), nome (texto), idade (inteiro) e saldo (float). Insira alguns registros de clientes na tabela.
#conexao.execute('CREATE TABLE clientes (id INT PRIMARY KEY, nome VARCHAR(100), idade INT, saldo FLOAT)')
#conexao.execute('INSERT INTO clientes (id, nome, idade, saldo) VALUES (1, "Sonia", 50, 190.4)')
# conexao.execute('INSERT INTO clientes (id, nome, idade, saldo) VALUES (2, "Antonio", 30, 200)')
# conexao.execute('INSERT INTO clientes (id, nome, idade, saldo) VALUES (3, "Graciele", 35, 300)')
# conexao.execute('INSERT INTO clientes (id, nome, idade, saldo) VALUES (4, "Junior", 25, 400)')
# conexao.execute('INSERT INTO clientes (id, nome, idade, saldo) VALUES (5, "Madalena", 42, 1500.6)')
# conexao.execute('INSERT INTO clientes (id, nome, idade, saldo) VALUES (6, "Suelen", 42, 456.8)')
# conexao.execute('INSERT INTO clientes (id, nome, idade, saldo) VALUES (7, "Samira", 36, 98.56)')
# conexao.execute('INSERT INTO clientes (id, nome, idade, saldo) VALUES (8, "Tiago", 50, 789.10)')
# conexao.execute('INSERT INTO clientes (id, nome, idade, saldo) VALUES (9, "Luan", 36, 471.98)')
# conexao.execute('INSERT INTO clientes (id, nome, idade, saldo) VALUES (10, "Yuri", 63, 963.8)')


# 6. Consultas e Funções Agregadas
# Escreva consultas SQL para realizar as seguintes tarefas:
# a) Selecione o nome e a idade dos clientes com idade superior a 30 anos.

# dados_clientes = conexao.execute('SELECT nome, idade FROM clientes WHERE idade > 30')
# for clientes in dados_clientes:
#          print(clientes)


# b) Calcule o saldo médio dos clientes.

# dados_clientes = cursor.execute('SELECT AVG(saldo) FROM clientes')
# for media in dados_clientes:
#     print(media[0])



# c) Encontre o cliente com o saldo máximo.

# dados_clientes = cursor.execute('SELECT nome, saldo FROM clientes ORDER BY saldo DESC LIMIT 1')
# for cliente in dados_clientes:
#     print(cliente)


# d) Conte quantos clientes têm saldo acima de 1000.

# saldo_acima_1000 = cursor.execute('SELECT COUNT(*) FROM clientes WHERE saldo > 1000')
# for saldo_acima in saldo_acima_1000:
#     print(saldo_acima[0])

# 7. Atualização e Remoção com Condições
# a) Atualize o saldo de um cliente específico.


# b) Remova um cliente pelo seu ID.


# 8. Junção de Tabelas
# Crie uma segunda tabela chamada "compras" com os campos: id
# (chave primária), cliente_id (chave estrangeira referenciando o id
# da tabela "clientes"), produto (texto) e valor (real). Insira algumas
# compras associadas a clientes existentes na tabela "clientes".
# Escreva uma consulta para exibir o nome do cliente, o produto e o
# valor de cada compra.


conexao.commit()
conexao.close()
