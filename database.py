import sqlite3

CRIAR_ESTOQUE = """
            CREATE TABLE IF NOT EXISTS estoque(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            id_produto NOT NULL,
            nome_produto TEXT NOT NULL,
            categoria TEXT NOT NULL,
            estoque INTEGER NOT NULL,
            preco REAL NOT NULL,
            valor_total_estoque REAL NOT NULL,
            data_entrada TEXT NOT NULL,
            status TEXT NOT NULL)
"""

def criar_banco(sql, params=()): 
    conexao = sqlite3.connect("estoque.db") 
    cursor = conexao.cursor() 
    cursor.execute(sql, params) 
    conexao.commit()
    conexao.close()

def inserir_planilha(estoque):
    conexao = sqlite3.connect("estoque.db")
    cursor = conexao.cursor()

    for registros in estoque:
        cursor.execute("INSERT INTO estoque (id_produto, nome_produto, categoria, estoque, preco, valor_total_estoque, data_entrada, status) VALUES (?, ?, ?, ?, ?, ?, ?, ?)", registros)
    conexao.commit()
    conexao.close()

def buscar_por_status(status):
    conexao = sqlite3.connect("estoque.db")
    conexao.row_factory = sqlite3.Row

    cursor = conexao.cursor()
    cursor.execute("SELECT * FROM estoque WHERE status = ?", (status,))
    resultado = cursor.fetchall()
    conexao.close()

    lista_registros = []
    for linha in resultado:
        registro = {
            "ID Produto": linha["id_produto"],
            "Nome do Produto": linha["nome_produto"],
            "Categoria": linha["categoria"],
            "Estoque Disponível": linha["estoque"],
            "Preço Unitário (R$)": linha["preco"],
            "Valor Total em Estoque (R$)": linha["valor_total_estoque"],
            "Última Entrada": linha["data_entrada"],
            "Status": linha["status"],
        }
        lista_registros.append(registro)

    return lista_registros

def valor_total_doestoque():
    conexao = sqlite3.connect("estoque.db")
    cursor = conexao.cursor()
    cursor.execute("SELECT SUM(valor_total_estoque) FROM estoque")
    resultado = cursor.fetchone()
    conexao.close()
    
    if resultado is None or resultado[0] is None:
        raise ValueError("A tabela está vazia ou não há valores para somar.")

    total = resultado[0]
    return total

def trazer_estoque_completo():
    conexao = sqlite3.connect("estoque.db")
    cursor = conexao.cursor()
    cursor.execute("SELECT * FROM estoque")
    resultado = cursor.fetchall()
    conexao.close()
    return resultado
