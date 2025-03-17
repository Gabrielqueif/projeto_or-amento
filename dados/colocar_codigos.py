import pandas as pd
import pymysql

# Caminho para a planilha
file_path = '../arquivos para enviar para db/ise sinapi.xlsx'

# ler nome da tabela
name = 'api_codigo_insumo'

# Ler a planilha
df = pd.read_excel(file_path)

# Selecionar apenas a coluna 'codigo do insumo'
codigo_insumo = df[['Código do Insumo']]

# Conectar ao banco de dados MySQL
conn = pymysql.connect(
    host='localhost',
    user='root',
    passwd='123456',
    database='orcamento_ifce'
)

# Cursor
cursor = conn.cursor()

# Inserir dados na tabela
with conn:
    with conn.cursor() as cursor:
        # Deletar dados existentes na tabela
        #cursor.execute(f'DELETE FROM {name}')
        #conn.commit()
        
        # Inserir novos dados
        for codigo in codigo_insumo['Código do Insumo']:
            #print(codigo)
            cursor.execute(f'INSERT INTO {name} (codigo_insumo) VALUES (%s)', (codigo))
            conn.commit()