import pandas as pd
import sqlite3


# ler nome da tabela
name = 'api_codigo_insumo'

# Ler a planilha
df = pd.read_excel("planilha.xlsx")
print(df.head())

# Selecionar apenas a coluna 'codigo do insumo'
codigo_insumo = df[['Código do Insumo']]
#
# Conectar ao banco de dados MySQL
conn = sqlite3.connect('../db.sqlite3')
#
with conn:
    cursor = conn.cursor()

   # Criar a tabela
    cursor.execute(f"CREATE TABLE IF NOT EXISTS {name} (id INTEGER PRIMARY KEY, codigo_insumo TEXT)")

    # Inserir os dados
    for i in range(len(codigo_insumo)):
        cursor.execute(f"INSERT INTO {name} (codigo_insumo) VALUES ('{codigo_insumo.iloc[i][0]}')")
    conn.commit()
    print(f'Tabela {name} criada com sucesso!')
    print(f'{len(codigo_insumo)} registros inseridos com sucesso!')