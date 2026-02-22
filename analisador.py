import sqlite3

conexao = sqlite3.connect("meubanco.db")
cursor = conexao.cursor()





#cursor.execute("DROP TABLE operadores")

cursor.execute("SELECT * FROM operadores")

print(cursor.fetchall())

#conexao.commit()

conexao.close()