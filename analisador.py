import sqlite3

conexao = sqlite3.connect("meubanco.db")
cursor = conexao.cursor()

with open("atendimentos.txt", "r", encoding="utf-8") as arquivo:
    for linha in arquivo:
        dados = linha.strip().split(",")
        
        cursor.execute("""INSERT INTO atendimentos (operador, data_hora, tma, transcricao, sentimento)
               VALUES (?, ?, ?, ?, ?)

               """, (dados[0], dados[1], int(dados[2]), dados[3], "pendente"))


cursor.execute("SELECT * FROM atendimentos")

print(cursor.fetchall())

#conexao.commit()

conexao.close()