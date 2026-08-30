import pandas as pd
import database

def estoque_baixo():
    dados = database.buscar_por_status("Baixo Estoque")
    df_estoque_baixo = pd.DataFrame(dados)
    df_estoque_baixo.to_excel("EstoqueBaixo.xlsx", index=False)

def valor_total_estoque():
    total = database.valor_total_doestoque()
    total_formatado = f"RS {total:,.2f}".replace(",", "X").replace("X", ".")
    df = pd.DataFrame({"Valor Total do Estoque": [total_formatado]})
    df.to_excel("ValorTotalEstoque.xlsx", index=False)
    
