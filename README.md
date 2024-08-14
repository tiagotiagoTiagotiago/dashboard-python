Dashboard de Vendas com Streamlit
Este projeto é um dashboard interativo desenvolvido em Python utilizando a biblioteca Streamlit. O objetivo é fornecer uma visualização detalhada dos dados de vendas, permitindo a análise mensal de diferentes métricas, como faturamento por unidade, tipos de produtos mais vendidos, contribuição por filial, desempenho das formas de pagamento e avaliações das filiais.

Funcionalidades
Seleção Mensal: Escolha o mês para visualizar os dados correspondentes.
Faturamento Diário: Gráfico de barras mostrando o faturamento diário por cidade.
Faturamento por Tipo de Produto: Gráfico de barras horizontal indicando o faturamento por linha de produto em cada cidade.
Contribuição por Filial: Gráfico de barras que mostra o total de faturamento de cada filial.
Desempenho das Formas de Pagamento: Gráfico de pizza mostrando a contribuição de cada forma de pagamento para o faturamento total.
Avaliações das Filiais: Gráfico de barras com a média de avaliação de cada filial.
Como Executar
Clone o repositório:
bash
Copiar código
git clone https://github.com/seu-usuario/seu-repositorio.git
Instale as dependências:
bash
Copiar código
pip install -r requirements.txt
Execute o aplicativo Streamlit:
bash
Copiar código
streamlit run app.py
Estrutura do Projeto
app.py: Arquivo principal que contém o código para a criação do dashboard.
vendas.csv: Arquivo CSV contendo os dados de vendas.
requirements.txt: Lista de dependências do projeto.
Bibliotecas Utilizadas
Streamlit: Para a criação do dashboard.
Pandas: Para a manipulação e análise dos dados.
Plotly Express: Para a construção de gráficos interativos.
