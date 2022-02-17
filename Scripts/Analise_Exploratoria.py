# Importando Bibliotecas

import pandas as pd

# Importando base de dados
df = pd.read_csv(r'H:\My Drive\1. ESTUDO\Desafio de BI - Semana 01 - Alura Filmes\Dados Brutos\Filmes.csv')

# Primeiras informações
df.head()
df.info()

# Colunas com campos nulos
gross_null = df.Gross.isnull().sum()
print(f'Nossa base de dados possui {gross_null} entradas com a coluna Gross nula')
metascore_null = df.Meta_score.isnull().sum()
print(f'Nossa base de dados possui {metascore_null} entradas com a coluna Meta_score nula')
# Ajustando a coluna Gross para valores numéricos
df.Gross
df['Gross'] = pd.to_numeric(df.Gross.str.replace(',',''),downcast='float')
df.info()
