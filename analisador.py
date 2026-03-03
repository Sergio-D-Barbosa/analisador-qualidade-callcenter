import sqlite3

def classificar_sentimento(transcricao):
    palavras_criticas = ["procon", "cancelar", "absurdo", "indevida", "bravo", "ruim", "péssimo"]
    texto_analise = transcricao.lower()

    for palavra in palavras_criticas:
        if palavra in texto_analise:
            return "crítico"
    
    return "bom"

try:
    conexao = sqlite3.connect("database_01.db")
    cursor = conexao.cursor()
    
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS atendimentos (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            operador TEXT,
            data_hora TEXT,
            protocolo INTEGER UNIQUE,
            transcricao TEXT,
            sentimento TEXT
        )
    """)

    print("Iniciando análise de atendimentos...")
    print("-" * 50)

    conexao = sqlite3.connect("database_01.db")
    cursor = conexao.cursor()
    palavras_criticas = ["procon", "cancelar", "absurdo", "indevida", "bravo", "ruim", "péssimo"]

    with open("atendimentos.txt", "r", encoding="utf-8") as arquivo:
        for linha in arquivo:

            try:
                
                dados = linha.strip().split(",")

                operador, data, protocolo, transcricao = dados[0], dados[1], int(dados[2]), dados[3]

                sentimento = classificar_sentimento(transcricao)

                cursor.execute("""
                               INSERT OR IGNORE INTO atendimentos (operador, data_hora, protocolo, transcricao, sentimento)
                                VALUES (?, ?, ?, ?, ?)""", (operador, data, protocolo, transcricao, sentimento))

            except (ValueError, IndexError) as e:
                print(f"Erro ao processar linha: {linha.strip()} - {e}")
                continue

    cursor.execute("SELECT operador, protocolo FROM atendimentos WHERE sentimento = 'crítico'")
    criticos = cursor.fetchall()

    print(f"\nFoi encontrado um total de {len(criticos)} atendimentos críticos:\n")

    for c in criticos:
        print(f"Operador: {c[0]} | Protocolo de Atendimento: {c[1]}")

    print("-" * 50)

    cursor.execute("SELECT * FROM atendimentos")


    dados = cursor.fetchall()
    print(f"\nDados armazenados no banco de dados:\n")
    for dado in dados:
        print(dado)

except sqlite3.Error as e:
    print(f"Erro ao acessar o banco de dados: {e}")

finally:    
    if conexao:
        conexao.commit()
        conexao.close()