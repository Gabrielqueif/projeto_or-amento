import sqlite3

# Conexão com o banco de dados
conexao = sqlite3.connect('../db.sqlite')

name = 'api_estados'

# Lista de estados brasileiros com suas siglas
estados = [
    ('Acre', 'AC'),
    ('Alagoas', 'AL'),
    ('Amapá', 'AP'),
    ('Amazonas', 'AM'),
    ('Bahia', 'BA'),
    ('Ceará', 'CE'),
    ('Distrito Federal', 'DF'),
    ('Espírito Santo', 'ES'),
    ('Goiás', 'GO'),
    ('Maranhão', 'MA'),
    ('Mato Grosso', 'MT'),
    ('Mato Grosso do Sul', 'MS'),
    ('Minas Gerais', 'MG'),
    ('Pará', 'PA'),
    ('Paraíba', 'PB'),
    ('Paraná', 'PR'),
    ('Pernambuco', 'PE'),
    ('Piauí', 'PI'),
    ('Rio de Janeiro', 'RJ'),
    ('Rio Grande do Norte', 'RN'),
    ('Rio Grande do Sul', 'RS'),
    ('Rondônia', 'RO'),
    ('Roraima', 'RR'),
    ('Santa Catarina', 'SC'),
    ('São Paulo', 'SP'),
    ('Sergipe', 'SE'),
    ('Tocantins', 'TO')
]

# Criar a tabela se não existir
with conexao:
    cursor = conexao.cursor()
    cursor.execute(f'''
        CREATE TABLE IF NOT EXISTS {name} (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome TEXT NOT NULL,
            sigla TEXT NOT NULL
        )
    ''')
    conexao.commit()

# Inserir dados na tabela estados
with conexao:
    cursor = conexao.cursor()
    
    # Deletar dados existentes na tabela
    cursor.execute(f'DELETE FROM {name}')
    conexao.commit()
    
    # Inserir novos dados
    cursor.executemany(f'INSERT INTO {name} (nome, sigla) VALUES (?, ?)', estados)
    conexao.commit()

print("Dados inseridos com sucesso!")