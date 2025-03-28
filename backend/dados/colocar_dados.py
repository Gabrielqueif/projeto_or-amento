import pandas as pd
import sqlite3

# Conexão com o banco de dados SQLite
conexao = sqlite3.connect('../db.sqlite3')  # Nome do arquivo do banco de dados SQLite
NAME = 'api_insumos'

# Leitura do arquivo Excel
db = pd.read_excel('planilha.xlsx')

# Inserção de dados no banco de dados
with conexao:
    cursor = conexao.cursor()
    
    # Comando para deletar os dados da tabela (opcional, descomente se necessário)
    # cursor.execute(f'DELETE FROM {NAME}')
    
    # Comando para adicionar os dados na tabela
    for i in range(len(db)):
        cursor.execute(
            f'INSERT INTO {NAME} (Classificação, descrição_insumo, unidade, origem_preço) VALUES (?, ?, ?, ?)',
            (db['Classificação'][i], db['Descrição do Insumo'][i], db['Unidade'][i], db['Origem de Preço'][i])
        )
    conexao.commit()

print("dados inseridos com sucesso")
