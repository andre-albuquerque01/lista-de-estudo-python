import sqlite3

# No parametro passa o nome do banco de dados
conexao = sqlite3.connect('aula.db')

c = conexao.cursor()

# Inserir informações no banco de dados

# c.execute("CREATE TABLE IF NOT EXISTS usuario(id_usuario integer PRIMARY KEY, nome text)")

# c.execute("INSERT INTO usuario VALUES(1, 'Launa')")
# c.execute("INSERT INTO usuario VALUES(2, 'Paulina')")
# c.execute("INSERT INTO usuario VALUES(3, 'Geovanna')")

# conexao.commit()

requisicao = "SELECT * FROM usuario WHERE nome = ?"

for linha in c.execute(requisicao, ('Launa', )):
    print(linha)