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

O primeiro passo é procurar, de maneira direta e objetiva respostas para as perguntas que foram feitas. Uma vez tendo estas respostas, faz sentido fazer perguntas mais detalhadas e buscar relações entre as variáveis.

1. Quais foram os filmes mais votados?

  Levando em consideração os 273.692.911 de votos registrados, os 5 filmes mais votados são:
  |Título|	Número de Votos	|Receita|	Ano de Lançamento| 	% de Votos|
  |-|-|-|-|-|
  |The Shawshank Redemption	|2.343.110|	$28.341.468,00|	1994|	0.86%|
  |The Dark Knight|	2.303.232|	$534.858.432,00|	2008|	0.84%|
  |Inception|	2.067.042|	$292.576.192,00|	2010|	0.76%|
  |Fight Club|	1.854.740|	$37.030.104,00|	1999|	0.67%|
  |Pulp Fiction|	1.826.188|	$107.928.760,00|	1994|	0.66%|

2. Quais são os gêneros mais rentáveis?

  Primeiramente, notamos que alguns filmes são classificados com mais de um gênero. Para resolver este problema, criamos colunas para cada um dos três possíveis gêneros e assim obter todos os gêneros possíveis.

  Em uma primeira análise, obtemos
  ```
  n_genres = len(pd.concat([df_genres[0],df_genres[1],df_genres[2]]).unique())
  print(f'Existem ao todo (a prinícipio) {n_genres} gêneros de filmes')

  Existem ao todo (a prinícipio) 35 gêneros de filmes
  ```
  Porém, ao olha a lista com mais cuidado, notamos que alguns gêneros aparecem mais de uma vez, como **Action** e **Western**.
  ```
  array(['Drama', 'Crime', 'Action', 'Biography', 'Western', 'Comedy',
       'Adventure', 'Animation', 'Horror', 'Mystery', 'Film-Noir',
       'Fantasy', 'Family', 'Thriller', None, ' Drama', ' Crime',
       ' Adventure', ' Romance', ' Sci-Fi', ' War', ' Family', ' Music',
       ' Comedy', ' Mystery', ' Biography', ' Action', ' Western',
       ' Thriller', ' Horror', ' Musical', ' Film-Noir', ' Fantasy',
       ' Sport', ' History'], dtype=object)
  ```
  Isso se dá por alguns possuem um espaço em branco antes de seus nomes. Para resolver isso, basta utilizar o método `strip` e buscar novamente pelos valores únicos. Com isso, temos 21 gêneros distintos:

  | | | | | | | |
  |-|-|-|-|-|-|-|
  |Action |Adventure  |Animation  |Biography  |Comedy   |Crime  |Drama  |
  |Family |Fantasy    |Film-Noir  |History    |Horror   |Music  |Musical|
  |Mystery|Romance    |Sci-Fi     |Sport      |Thriller |War    |Western|

  Com essas informações, pode-se concluir que os 5 gêneros mais que mais lucraram foram:

  |Gênero |Gross	|%Gross |
  |-  |-  |-  |
  |Adventure   |$28.404.248.576,00 |18,25%  |
  |Drama       |$28.258.189.312,00 |18,16%  |
  |Action      |$22.227.009.536,00 |14,28%  |
  |Comedy      |$12.600.133.632,00 |8,10%   |
  |Sci-Fi      |$9.051.814.912,00  |5,82%   |
  |Animation   |$8.836.903.936,00  |5,68%   |

  e o lucro apenas destes 5 gêneros corresponde à quase 60% de todo lucro gerado pelos filmos em consideração.

3. Estrelas que mais aparecem em filmes

  Considerando os 1000 filmes e as 4 estrelas principais, temos 2709 atores distintos. Podem ser feitas duas análises, a primeira é considerar quantas vezes um ator aparece independente da posição e a outra levando em consideração a ordem. Para cada uma das análises vamos utilizar estratégias distintas.

  Para a primeira, vamos fazer como antes, obter uma lista de todas as atores e buscar quais filmes eles aparecem. Já para a segunda, basta utilizar o método `groupby` e usar como agregador `count` e contar quantos filmes aparecem.


  Ao contar apenas as aparições como estrelas dos filmes considerados, todos os 7 atores que mais aparecem como estrelas de filmes são homens e estes são:

  |Star|	Número de Filmes|
  |-   |  |
  |Robert De Niro |17 |
  |Clint Eastwood |15 |
  |Tom Hanks      |14 |
  |Al Pacino      |13 |
  |Brad Pitt      |12 |
  |Christian Bale |11 |
  |Leonardo DiCaprio|11|

  enquanto a mulher que mais estrlou filmes foi Scarlett Johansson com 9 filmes, empatada em décimo lugar.

  Já quando consideramos a ordem, as ordens mudam um pouco

  |Star | Filmes como Estrela 1|
  |-  |-  |
  |Tom Hanks          |12 |
  |Robert De Niro     |11 |
  |Clint Eastwood     |10 |
  |Al Pacino          |	10 |
  |Leonardo DiCaprio  |	9  |
  |Humphrey Bogart    |	9  |
  |Johnny Depp        |	8  |

  Para Estelas 2, aparecem alguns nomes novos:

  |Star | Filmes como Estrela 2 |
  |-|-|
  |Emma Watson  |7  |
  |Matt Damon   |5 |
  |Diane Keaton |4 |
  |Ian McKellen |4 |
  |Brad Pitt    |4  |
  |Ed Harris    |4  |
  |Julie Delpy  |4  |
