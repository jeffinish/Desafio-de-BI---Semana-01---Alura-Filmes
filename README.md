# Desafio-de-BI-Semana-01-Alura-Filmes

## Etapa 1 : Visão geral dos dados e primeiros ajustes

Começamos olhando os dados de uma maneira mais geral e fazendo os primeiros ajustes caso sejam necessários.

Das 1000 entradas do Dataframe, pode-se notar que 11 possuem a coluna `Gross` nula e 157 com a coluna `Meta_score` nula.

O único ajuste necessário nesta primeira etapa é alterar o tipo dos elementos da coluna `Gross` de `object` para `float`. Isto vai nos permitir fazer operações com essa coluna. Antes de fazer isto, podemos ver que os valores da coluna possuem virgula separando os milhares.

| index |Gross     |
| :------------- | :------------- |
|0    | 28,341,469|
|1    | 134,966,411|
|3    | 57,300,000|
|2    | 534,858,444|
|4    | 4,360,000|
|     | ...     |
|995  |	508,012|
|996  |	5,400,00|
|997  |	30,500,000|
|998  |	1,590,000|
|999  |	51,711|

Para resolver este problema, basta utilizar
```
df['Gross'] = pd.to_numeric(df.Gross.str.replace(',',''),downcast='float')
```

## Etapa 2: Respondendo algumas perguntas básicas
