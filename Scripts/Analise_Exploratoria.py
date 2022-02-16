# Importando Bibliotecas

import pandas as pd

# Importando base de dados
df = pd.read_csv(r'H:\My Drive\1. ESTUDO\Desafio de BI - Semana 01 - Alura Filmes\Dados Brutos\Base de dados\Filmes.csv')

# Primeiras informações
df.head()
df.info()

# Ajustando a coluna Gross para valores numéricos
pd.to_numeric(df[pd.to_numeric(df.Gross.str.replace(',',''),downcast='float').isnull()].Gross)
