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
    cursor.execute('CREATE TABLE alunos (id INT, nome varchar(100), idade INT, curso varchar(100));')
    
    # Inserir 5 registros ou mais na tabela alunos
    cursor.execute('INSERT INTO alunos(id,nome,idade,curso) VALUES (1,"Isadora",8, "financas pessoais")')
    cursor.execute('INSERT INTO alunos(id,nome,idade,curso) VALUES (2,"Maria",9, "ingles para adolescentes")')
    cursor.execute('INSERT INTO alunos(id,nome,idade,curso) VALUES (3,"Joao",10, "design grafico")')
    cursor.execute('INSERT INTO alunos(id,nome,idade,curso) VALUES (4,"Pedro",11, "programação para iniciantes")')
    cursor.execute('INSERT INTO alunos(id,nome,idade,curso) VALUES (5,"Ana",12, "programação para iniciantes")')
    cursor.execute('INSERT INTO alunos(id,nome,idade,curso) VALUES (6,"Tereza",13, "programação para iniciantes")')
    cursor.execute('INSERT INTO alunos(id,nome,idade,curso) VALUES (7,"Bento",14, "financas pessoais")')
    cursor.execute('INSERT INTO alunos(id,nome,idade,curso) VALUES (8,"Luan",15, "redação e comunicação")')
    cursor.execute('INSERT INTO alunos(id,nome,idade,curso) VALUES (9,"Camila",14, "ingles para adolescentes")')
    cursor.execute('INSERT INTO alunos(id,nome,idade,curso) VALUES (10,"Patricia",15, "programação para iniciantes")')
    cursor.execute('INSERT INTO alunos(id,nome,idade,curso) VALUES (11,"Bento",23, "engenharia")')
    cursor.execute('INSERT INTO alunos(id,nome,idade,curso) VALUES (12,"Luan",27, "engenharia")')
    cursor.execute('INSERT INTO alunos(id,nome,idade,curso) VALUES (13,"Camila",20, "nutricao")')
    cursor.execute('INSERT INTO alunos(id,nome,idade,curso) VALUES (14,"Patricia",22, "programação para iniciantes")')
    
#Consultas Básicas
#Escreva consultas SQL para realizar as seguintes tarefas:
#a) Selecionar todos os registros da tabela "alunos".

    dados = cursor.execute('SELECT * from alunos')
    for alunos in dados:
         print(alunos)

#b) Selecionar o nome e a idade dos alunos com mais de 20 anos.

    dados = cursor.execute('SELECT nome, idade FROM alunos WHERE idade>20')
    for alunos in dados:
         print(alunos)



#c) Selecionar os alunos do curso de "Engenharia" em ordem alfabética.

dados = cursor.execute('SELECT nome FROM alunos WHERE curso="engenharia" ORDER BY nome DESC')
for alunos in dados:
        print(alunos)


#d) Contar o número total de alunos na tabela

dados = cursor.execute('SELECT COUNT(DISTINCT id) FROM alunos')
for total in dados:
    print(total[0])

conexao.commit()
conexao.close()