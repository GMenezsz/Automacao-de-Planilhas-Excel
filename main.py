import utils
import os
import inserir_registros
from database import criar_banco, CRIAR_ESTOQUE

def main():
    criar_banco(CRIAR_ESTOQUE)

    arquivo = "estoque_supermercado.xlsx"
    if not os.path.exists(arquivo):
        raise FileNotFoundError(f"O arquivo {arquivo} não foi encontrado")
    else:
        print(f"O arquivo {arquivo} foi encontrado.")

    inserir_registros.inserir_excel_bd(arquivo)

    utils.estoque_baixo()
    utils.valor_total_estoque()

if __name__ == "__main__":
    main()
