README

Utilizando o colab notebook, importamos o pandas.

Foi realizada uma análise exploratória de duas bases de dados, que estavam divididas em quatro arquivos. 

Pois o banco de dados só fornecia dados ano a ano. 
Os arquivos de mesma base e anos diferentes foram concatenados em dois novos arquivos CSVs.

Para limpeza dos dados, algumas variáveis tiveram os tipos convertidos. As colunas foram renomeadas. Foram removidas as duplicatas.

Pautada nas variáveis equivalentes entre os dois dataframes foi realizado um merge para junção dos datasets. E criado um novo CSV.

Uma nova limpeza de dados, foi verificado a presença de dados nulos, e retirados. As linhas originais: 390664; Linhas após remoção de nulos: 373055

Para a primeira hipótese:

Os estados foram classificados por região, e com isso essa coluna foi criada. A coluna dataHora foi divida, criando uma coluna para mês e ano.

Realizamos um groupby para obter as queimadas por bioma e estado, e outro para bioma por região, e outros com ambos os dados.

Para visualização dos dados importamos as bibliotecas matplotlib, seaborn e warnings.

Par ao gráfico de biomas por região foi utilizado o sns.barplot e uma função para ignorar valores menores que zero.

Os dados por mês e ano foram agrupados.

Foi realizado um gráfico de linha para os focos de queimadas por mês e bioma.

Foi criada a coluna estação, referente as estações do ano. E salvo um novo dataframe.

foi realizado um outro gráfico de barras com as combinações de Ano, Estação e Bioma

Foi importada a scipy do stats para realizar a análise de variância entre os dados de queimadas e estações do ano.

Para segunda hipótese:

Os períodos de seca foram categorizados Curta (<=5 dias)', 'Moderada (6-10 dias)', 'Longa (11-20 dias)', 'Extensa (>20 dias).

Foi realizado um gráfico de barras para visualização dos focos de queimadas por categoria de seca, entre os dois anos.

Também foi realizado um gráfico de barras para visualização dos focos de queimadas por categoria de seca para cada um dos biomas, por ano.

par aa análise estáticas dos focos de queimadas por categoria de seca,  nos dois anos, foi realizada uma ANOVA: oneway.

Para terceira hipótese:

os dados foram agrupados por mês, ano, e focos de queimadas. E por mês, ano e precipitação.

Para visualização dos dados foi realizado um gráfico de dois eixos, barras e linhas.

Para análise estatística foi realizada a correlação de Pearson.



