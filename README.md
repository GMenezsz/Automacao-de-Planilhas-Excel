# Processador de Vendas e Gerenciador de Clientes via Excel e SQLite

Sistema desenvolvido em **Python** para automação de leitura, processamento, armazenamento e exportação de dados a partir de planilhas Excel (`.xlsx`), utilizando **Pandas** e **SQLite3**.

## 🚀 Funcionalidades
- **Leitura Dinâmica de Excel:** Importa dados de planilhas identificando as colunas pelos nomes dos cabeçalhos, garantindo flexibilidade caso a ordem mude.
- **Persistência em Banco de Dados:** Armazena e estrutura os dados automaticamente em um banco SQLite3.
- **Exportação Automatizada:** Gera novos relatórios em planilhas Excel separadas diretamente dos dados filtrados no banco.
- **Arquitetura Modular:** Código dividido em camadas de responsabilidade (`main.py`, `utils.py`, `inserir_registros` e `database.py`).

## 🛠️ Tecnologias Utilizadas
- **Python 3**
- **Pandas** (Manipulação e leitura de dados)
- **SQLite3** (Banco de dados relacional local)

## 📂 Estrutura do Projeto
- `main.py`: Arquivo principal de execução do fluxo.
- `utils.py`: Validação de cabeçalhos e lógica de exportação.
- `database.py`: Gerenciamento de conexões, criação da tabela e persistência no SQLite.
- `estoque_supermercado.xlsx`: Planilha de exemplo contendo os dados de entrada.

---
*Projeto desenvolvido para estudos e aplicação prática de manipulação de dados, automação de planilhas e integração com banco de dados relacional.*
