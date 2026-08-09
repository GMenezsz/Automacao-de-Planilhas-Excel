import os
import pandas as pd
import database

def ler_excel(caminho_arquivo):
    if not os.path.exists(caminho_arquivo):
        raise FileNotFoundError(f"O arquivo '{caminho_arquivo}' não foi encontrado.")
    
    df = pd.read_excel(caminho_arquivo)
    
    colunas_necessarias = ["ID do Pedido", "Cliente", "Valor", "Status"]
    for coluna in colunas_necessarias:
        if coluna not in df.columns:
            raise ValueError(f"A coluna obrigatória '{coluna}' não foi encontrada no cabeçalho do Excel.")
    
    registros = []
    for _, row in df.iterrows():
        registro = {
            "id_produto": str(row["ID do Pedido"]),
            "cliente": str(row["Cliente"]),
            "valor": float(row["Valor"]),
            "status": str(row["Status"]).strip()
        }
        registros.append(registro)
        
    return registros

def processar_importacao(caminho_arquivo):
    database.criar_banco()
    dados_excel = ler_excel(caminho_arquivo)
    database.inserir_clientes(dados_excel)

def obter_clientes_por_status(status):
    return database.buscar_por_status_db(status)

def exportar_pendentes():
    df_pendentes = obter_clientes_por_status("Pendente")
    df_pendentes.to_excel("clientes_pendentes.xlsx", index=False)

def exportar_pagos():
    df_pagos = obter_clientes_por_status("Pago")
    df_pagos.to_excel("clientes_pagos.xlsx", index=False)