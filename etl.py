import pandas as pd
import sqlite3

# Extração: Ler o arquivo CSV
df = pd.read_csv('train.csv')

# Transformação: Limpar e selecionar colunas úteis
df = df[['Order Date', 'Region', 'Product Name', 'Sales']].dropna()
df['Order Date'] = pd.to_datetime(df['Order Date'], dayfirst=True)  # Converter data com dia primeiro
df['Sales'] = df['Sales'].round(2)  # Arredondar valores

# Carga: Salvar em um banco SQLite
conn = sqlite3.connect('sales_database.db')
df.to_sql('sales', conn, if_exists='replace', index=False)
conn.close()

print("ETL concluído! Dados salvos em sales_database.db")