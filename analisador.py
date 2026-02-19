import sqlite3

conexao = sqlite3.connect("meubanco.db")
cursor = conexao.cursor()

cursor.execute("INSERT INTO operadores (nome, tma) VALUES ('Maria', 370)")


conexao.commit()


cursor.execute("SELECT * FROM operadores")


dados = cursor.fetchall()


for linha in dados:
    print(linha)

conexao.close()