import sqlite3

conexao = sqlite3.connect("meubanco.db")
cursor = conexao.cursor()

palavras_criticas = ["procon", "cancelar", "absurdo", "indevida", "bravo", "ruim", "péssimo"]



print("Iniciando análise de atendimentos...")

print("-" * 50)


with open("atendimentos.txt", "r", encoding="utf-8") as arquivo:
    for linha in arquivo:
        dados = linha.strip().split(",")

        operador, data, protocolo, transcricao = dados[0], dados[1], int(dados[2]), dados[3]

        sentimento = "bom"
        texto_analise = transcricao.lower()

        for palavra in palavras_criticas:
            if palavra in texto_analise:
                sentimento = "crítico"
                break
        
        '''cursor.execute("""INSERT INTO atendimentos (operador, data_hora, protocolo, transcricao, sentimento)
               VALUES (?, ?, ?, ?, ?)

               """, (operador, data, protocolo, transcricao, sentimento))'''


cursor.execute("SELECT operador, protocolo FROM atendimentos WHERE sentimento = 'crítico'")
criticos = cursor.fetchall()

print(f"\nFoi encontrado um total de {len(criticos)} atendimentos críticos:\n")

for c in criticos:
    print(f"Operador: {c[0]} | Protocolo de Atendimento: {c[1]}")

#conexao.commit()

conexao.close()

print("-" * 50)

print("\nAnálise de atendimentos concluída.")