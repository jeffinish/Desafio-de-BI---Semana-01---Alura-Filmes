# Importando Bibliotecas

import pandas as pd
pd.set_option('display.float_format', '{:.2f}'.format)

import matplotlib.pyplot as plt
plt.rc('figure', figsize = (15, 7))

import numpy as np

# Importando base de dados
# df = pd.read_csv(r'H:\My Drive\1. ESTUDO\Desafio de BI - Semana 01 - Alura Filmes\Dados Brutos\Filmes.csv')
df = pd.read_csv(r'G:\My Drive\1. ESTUDO\Desafio de BI - Semana 01 - Alura Filmes\Dados Tratados\Filmes_Tratados.csv')

# Primeiras informações
df.info()

# Scaterplot : Faturamento x IMDB

plt.scatter(df.IMDB_Rating,df.Gross)

# Scatterplot : Faturamento x Ano

plt.scatter(df.Released_Year,df.Gross)

# Scatterplot : Faturamento x Duração

plt.scatter(df.Runtime,df.Gross)

# BoxPlot : Por Ano
grupo_ano = df.groupby('Released_Year')['Gross']
grupo_ano

Q1 = grupo_ano.quantile(.25)
Q1

### Terceiro Quartil (75%)
Q3 = grupo_ano.quantile(.75)
Q3

### Intervalo interquaril
IIQ = Q3- Q1

### Limite inferior
limite_inferior = Q1 - 1.5*IIQ
limite_superior = Q3 + 1.5*IIQ


dados_new = pd.DataFrame()
for tipo in grupo_ano.groups.keys():
    eh_tipo = df['Released_Year'] == tipo
    eh_dentro_limite = (df.Gross >= limite_inferior[tipo]) & (df.Gross <= limite_superior[tipo])
    selecao = eh_tipo & eh_dentro_limite
    dados_selecao = df[selecao]
    dados_new = pd.concat([dados_new,dados_selecao])
dados_new_recent = dados_new[dados_new.Released_Year >= 1980]
dados_new.describe()
dados_new_recent
dados_new_recent.boxplot(['Gross'],by=['Released_Year'])

df_recent = df[df.Released_Year >= 1980]
pic_gross_year = df_recent.boxplot(['Gross'],by=['Released_Year'])
pic_gross_year.set_xlabel('Ano de Lançamento')
pic_gross_year.set_ylabel('Faturamento em Dólares')
pic_gross_year.set_title('Boxplot de Faturamento agrupado por Ano')
plt.suptitle('')
plt.xticks(rotation=45)
plt.ticklabel_format(axis='y',useOffset=False,style='plain')
plt.savefig(r'G:\My Drive\1. ESTUDO\Desafio de BI - Semana 01 - Alura Filmes\Imagens\gross_by_year.png',dpi=300,bbox_inches='tight')

df.groupby('')


df[df.Released_Year == 1990].sort_values(by=['Gross'],ascending=False)


# Gráficos de evolução por ano

from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import StandardScaler


df_new = df.dropna(subset=['Gross'])
df_new = df_new[df_new.Released_Year >= 1980]
group_year = df_new.groupby(['Released_Year'])['Gross']
ml_df = pd.DataFrame(group_year.sum()).reset_index()

### Gross Linear
Y_sum = ml_df[['Gross']]
X_sum = ml_df[['Released_Year']]
reg = LinearRegression()
reg.fit(X,Y)
reg.coef_
gross_linear = reg.predict(X)
gross_linear
plt.plot(X,Y)
plt.plot(X,gross_linear)

### Count Linear
ml_count =  pd.DataFrame(group_year.count()).reset_index()
ml_count.rename(columns={'Gross':'Count'},inplace=True)
Y_count = ml_count[['Count']]
X_count = ml_count[['Released_Year']]

reg_count = LinearRegression()
reg_count.fit(X_count,Y_count)
count_linear = reg_count.predict(X_count)
plt.plot(X_count,Y_count)
plt.plot(X_count,count_linear)

### Mean Linear
ml_avg = pd.DataFrame(group_year.mean()).reset_index()
ml_avg.rename(columns={'Gross':'Mean'},inplace=True)
Y_avg = ml_avg[['Mean']]
X_avg = ml_avg[['Released_Year']]

reg_avg = LinearRegression()
reg_avg.fit(X_avg,Y_avg)
avg_linear = reg_avg.predict(X_avg)
plt.plot(X_avg,Y_avg)
plt.plot(X_avg,avg_linear)

## Teste Normalizando os valores
###Avg
avg_scaler = StandardScaler()
avg_scaler.fit(Y_avg)
Y_avg_scaled = avg_scaler.transform(Y_avg)
reg_avg = LinearRegression()
reg_avg.fit(X_avg,Y_avg_scaled)
reg_avg.coef_
avg_linear = reg_avg.predict(X_avg)
plt.plot(X_avg,Y_avg_scaled)
plt.plot(X_avg,avg_linear)

##Count
count_scaler = StandardScaler()
count_scaler.fit(Y_count)
Y_count_scaled = count_scaler.transform(Y_count)
reg_count = LinearRegression()
reg_count.fit(X_count,Y_count_scaled)
reg_avg.coef_
count_linear = reg_count.predict(X_count)
plt.plot(X_count,Y_count_scaled)
plt.plot(X_count,count_linear)

##Sum
sum_scaler = StandardScaler()
sum_scaler.fit(Y_sum)
Y_sum_scaled = sum_scaler.transform(Y_sum)
reg_sum = LinearRegression()
reg_sum.fit(X_sum,Y_sum_scaled)
reg_sum.coef_
sum_linear = reg_sum.predict(X_sum)
plt.plot(X_sum,Y_sum_scaled)
plt.plot(X_sum,sum_linear)

##Max
ml_max = pd.DataFrame(group_year.max()).reset_index()
ml_max.rename(columns={'Gross':'Max'},inplace=True)
Y_max = ml_max[['Max']]
X_max = ml_max[['Released_Year']]
max_scaler = StandardScaler()
max_scaler.fit(Y_max)
Y_max_scaled = max_scaler.transform(Y_max)
reg_max = LinearRegression()
reg_max.fit(X_max,Y_max_scaled)
reg_max.coef_
max_linear = reg_max.predict(X_max)
plt.plot(X_max,Y_max_scaled)
plt.plot(X_max,max_linear)

##Min
df_new.sort_values(by=['Gross'])
ml_min = pd.DataFrame(group_year.min()).reset_index()
ml_min.rename(columns={'Gross':'min'},inplace=True)
Y_min = ml_min[['min']]
X_min = ml_min[['Released_Year']]
min_scaler = StandardScaler()
min_scaler.fit(Y_min)
Y_min_scaled = min_scaler.transform(Y_min)
reg_min = LinearRegression()
reg_min.fit(X_min,Y_min_scaled)
reg_min.coef_
min_linear = reg_min.predict(X_min)
plt.plot(X_min,Y_min_scaled)
plt.plot(X_min,min_linear)


plt.plot(X_avg,avg_linear,label='Avg Gross')
plt.plot(X_count,count_linear,label='Count')
plt.plot(X_sum,sum_linear,label='Total Gross')
plt.plot(X_max,max_linear,label='Max Gross')
plt.plot(X_min,min_linear,label='Min Gross')
plt.legend()
plt.savefig(r'G:\My Drive\1. ESTUDO\Desafio de BI - Semana 01 - Alura Filmes\Imagens\gross_normal.png',dpi=300,bbox_inches='tight',transparent=False)

plt.plot(X_max,Y_max_scaled)







## Total de Receita por ano
grupo_ano.sum().plot()
##Quantidade de Filmes por Ano
grupo_ano.count().plot()

## Média de Receita por ano
grupo_ano.mean().plot()
