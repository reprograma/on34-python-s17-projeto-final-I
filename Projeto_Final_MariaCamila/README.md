# 📊 Projeto de Análise de Dados sobre Diversidade de Gênero e Raça

Este projeto faz parte do bootcamp da **Reprograma** sobre **Python para Dados** e tem como objetivo analisar a diversidade de gênero e raça na área de tecnologia e dados no Brasil. Utilizamos uma base de dados contendo informações sobre escolaridade, faixa etária, experiência, nível de atuação e faixa salarial dos participantes.

## 📂 Descrição dos Dados

A base de dados utilizada contém **7.404 registros** e **16 colunas**, com informações como:

- 🆔 **ID**: Identificação única dos participantes.
- 📅 **Ano**: Ano da coleta dos dados.
- 👶👨👵 **Faixa Etária**: Faixa etária dos respondentes.
- 🚻 **Gênero**: Gênero com o qual o respondente se identifica.
- 🧑🏽‍🦱👩🏻‍🦰 **Como você se identifica**: Identificação racial do respondente (e.g., Parda, Branca).
- 🏠 **Estado e Região**: Localização do participante.
- 🎓 **Escolaridade**: Nível de escolaridade atual.
- 💼 **Área de Formação**: Área acadêmica ou profissional do participante.
- 👩‍💻 **Você está trabalhando?**: Indicador se a pessoa está empregada.
- 🏢 **Setor**: Setor onde trabalha (e.g., Finanças, Setor Público).
- 👩‍🏫 **Cargo como Gestor**: Se o participante atua em posição de gestão.
- 📋 **Cargo Atual**: Cargo atual do participante.
- 📊 **Nível**: Nível profissional (e.g., Júnior, Pleno, Sênior).
- 💸 **Faixa Salarial**: Faixa salarial dos participantes, por gênero e raça.
- 🕒 **Tempo de experiência na área de dados**: Tempo de atuação na área de dados.

## 🔗 Fontes de Dados

As bases de dados originais foram obtidas dos seguintes links:

- [State of Data 2022 - Kaggle](https://www.kaggle.com/datasets/datahackers/state-of-data-2022/data)
- [State of Data Brazil 2023 - Kaggle](https://www.kaggle.com/datasets/datahackers/state-of-data-brazil-2023)

## 🛠️ Ferramentas Utilizadas

- **📊 Excel**: Para tratamento inicial e limpeza dos dados.
- **🐍 Python** (Colab): Para análise exploratória dos dados.
- **📉 Pandas**: Para manipulação da base de dados no Colab.
- **📊 Matplotlib/Seaborn**: Para criação de gráficos exploratórios no Colab.

## 📝 Passos Realizados

1. 🔍 **Exploração Inicial dos Dados**: Leitura e tratamento inicial dos dados utilizando **Excel** para identificar inconsistências e valores faltantes.
2. 🧼 **Limpeza de Dados**: Correção e preparação dos dados no Excel para facilitar a análise.
3. 📈 **Análise Exploratória no Colab**: Transferência da base para o Google Colab, onde foram gerados gráficos exploratórios para entender a distribuição dos dados e encontrar padrões sobre a diversidade na área de dados.
4. 📊 **Visualização dos Resultados**: Foram criados gráficos utilizando as bibliotecas **Matplotlib** e **Seaborn** para visualizar informações como:
   - 📊 Distribuição de gênero e raça.
   - 💰 Faixa salarial por grupo.
   - 🎓 Escolaridade e área de formação predominante.
   - 🕒 Tempo de experiência na área de dados por faixa etária.

## 🔗 Links Importantes

- **Tableau**: [Visualização Interativa no Tableau](https://public.tableau.com/app/profile/vera.felix/viz/diversidade-dados/Painel1#1)
- **Apresentação**: [Apresentação no Canva](https://www.canva.com/design/DAGScIVPqyE/X6USiBmqlgwPmYTXadn43A/edit?utm_content=DAGScIVPqyE&utm_campaign=designshare&utm_medium=link2&utm_source=sharebutton)
- **Github**: [Repositório do Projeto](https://github.com/Vera-Felix/on34-python-s17-s18-projeto-final)

## 📁 Estrutura do Repositório

- `📄 base_diversidade.csv`: Base de dados utilizada para a análise.
- `📓 diversidade_dados.ipynb`: Notebook contendo o tratamento e a análise dos dados no Colab. [Link para o Notebook](https://colab.research.google.com/drive/1Q5UMdDgclddF2XW6oiNo2ynvS6HaAuLO?usp=sharing)
- `📜 README.md`: Arquivo de documentação do projeto.

## 📢 Conclusão

Este projeto buscou identificar e entender como **gênero** e **raça** impactam a inserção e a permanência de profissionais na área de dados e tecnologia, contribuindo para um debate mais inclusivo e orientado por dados.
