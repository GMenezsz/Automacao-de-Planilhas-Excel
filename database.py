import sqlite3
import pandas as pd

DB_NAME = "clientes_sistema.db"
TABELA_NOME = "pedidos_clientes"

def criar_banco():
    conexao = sqlite3.connect(DB_NAME)
    cursor = conexao.cursor()
    cursor.execute(f"""
        CREATE TABLE IF NOT EXISTS {TABELA_NOME} (
            id_produto TEXT PRIMARY KEY,
            cliente TEXT NOT NULL,
            valor REAL NOT NULL,
            status TEXT NOT NULL
        )
    """)
    conexao.commit()
    conexao.close()

def inserir_clientes(registros):
    conexao = sqlite3.connect(DB_NAME)
    cursor = conexao.cursor()
    for reg in registros:
        cursor.execute(f"""
            INSERT OR REPLACE INTO {TABELA_NOME} (id_produto, cliente, valor, status)
            VALUES (?, ?, ?, ?)
        """, (reg["id_produto"], reg["cliente"], reg["valor"], reg["status"]))
    conexao.commit()
    conexao.close()

def buscar_por_status_db(status_Desejado):
    conexao = sqlite3.connect(DB_NAME)
    query = f"SELECT id_produto AS ID, cliente AS Cliente, valor AS Valor, status AS Status FROM {TABELA_NOME} WHERE status = ?"
    df_resultado = pd.read_sql(query, conexao, params=(status_Desejado,))
    conexao.close()
    return df_resultado