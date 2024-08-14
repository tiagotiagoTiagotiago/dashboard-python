import streamlit as st #criação de dashboard
import pandas as pd #manipulação de dados
import plotly.express as px #construção de gráficos
# Com uma visão mensal
#faturamento por unidade… 
# tipo de produto mais vendido, contribuição por filial,
#Desempenho das forma de pagamento…
#Como estão as avaliações das filiais?
st.set_page_config(layout="wide")#ocupa todo espaço horizontal

df = pd.read_csv("vendas.csv", sep=";", decimal=",")#separação dele está com ; e as casas decimais com ,    
df["Date"] = pd.to_datetime(df["Date"])#converter a data que está como string no csv para data de verdade
df=df.sort_values("Date")#seria como ordenando as datas

df["Month"] = df["Date"].apply(lambda x: str(x.year) + "-" + str(x.month))#função de uma linha que transforma ano e mês em string
month = st.sidebar.selectbox("Mês", df["Month"].unique())#criando uma selectbox com os valores do df

df_filtered = df[df["Month"] == month]#criando filtro por mês
df_filtered


#criando colunas com streamlit
col1, col2 = st.columns(2)
col3, col4, col5 = st.columns(3)


#grafico de faturamento diario
fig_date = px.bar(df_filtered, x="Date", y="Total", color="City", title="Faturamento por dia")
col1.plotly_chart(fig_date, use_container_width=True)

#grafico de faturamento de tipo de produto
fig_prod = px.bar(df_filtered, x="Date", y="Product line", 
                  color="City", title="Faturamento por tipo de produto",
                  orientation="h")
col2.plotly_chart(fig_prod, use_container_width=True)

#contribuição por filial
city_total = df_filtered.groupby("City")[["Total"]].sum().reset_index()#soma o total de valores
fig_city = px.bar(city_total, x="City", y="Total",
                   title="Faturamento por filial")
col3.plotly_chart(fig_city, use_container_width=True)

#grafico de tipo de pagamento
fig_kind = px.pie(df_filtered, values="Total", names="Payment",
                   title="Faturamento por tipo de pagamento")
col4.plotly_chart(fig_kind, use_container_width=True)


city_total = df_filtered.groupby("City")[["Rating"]].mean().reset_index()
fig_rating = px.bar(df_filtered, y="Rating", x="City",
                   title="Avaliação")
col5.plotly_chart(fig_rating, use_container_width=True)


