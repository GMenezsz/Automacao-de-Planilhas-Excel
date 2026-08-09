import models

def main():
    arquivo_entrada = "vendas.xlsx"
    
    models.processar_importacao(arquivo_entrada)
    
    print("--- CLIENTES PENDENTES ---")
    print(models.obter_clientes_por_status("Pendente").to_string(index=False))
    
    print("\n--- CLIENTES PAGOS ---")
    print(models.obter_clientes_por_status("Pago").to_string(index=False))
    
    models.exportar_pendentes()
    models.exportar_pagos()
    print("\nProcesso concluído e arquivos exportados com sucesso!")

if __name__ == "__main__":
    main()