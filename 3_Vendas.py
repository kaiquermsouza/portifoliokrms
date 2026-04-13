import streamlit as st

st.title("📈 Projeto: Vendas x Meta")

st.subheader("🎯 Objetivo")
st.write("""
Desenvolver um dashboard comercial para acompanhamento de faturamento versus metas,
permitindo análise de desempenho e identificação de oportunidades de crescimento.
""")

st.subheader("📊 Sobre o Dashboard")
st.write("""
O dashboard foi desenvolvido no Power BI com foco em indicadores comerciais:

🔹 Performance de Vendas:
- Faturamento total
- Comparação com metas (% atingido)
- Evolução mensal e anual

🔹 Análise por Categoria:
- Desempenho por subcategoria de produto
- Comparação entre faturamento e meta
- Identificação de áreas com melhor performance

🔹 Gestão Analítica:
- Análise detalhada mês a mês
- Comparação ano contra ano
- Apoio à tomada de decisão comercial
""")

st.subheader("💡 Principais Insights")
st.write("""
- Atingimento de metas acima de 100% em determinados períodos
- Diferença de performance entre categorias de produtos
- Identificação de sazonalidade nas vendas
- Oportunidades de melhoria em categorias com baixo desempenho
""")

st.subheader("⚙️ Diferencial do Projeto")
st.write("""
Este dashboard permite acompanhar o desempenho comercial de forma clara e estratégica,
integrando metas e resultados em uma única visão, facilitando decisões orientadas por dados.
""")

st.divider()

# 🔗 LINK DO POWER BI
url = "https://app.fabric.microsoft.com/view?r=eyJrIjoiYjJkNGUxZjQtZTQwMy00OTk5LTk4M2UtMTlmNjZkODczNmI0IiwidCI6ImE4Y2Y0YWYwLTc5NzctNGQ4Zi1iNjQzLTJjNWJhYTNlZjQxZCJ9"

st.link_button("🔗 Abrir Dashboard no Power BI", url)

st.divider()

# 📺 EMBED
st.subheader("📺 Visualização do Dashboard")

st.components.v1.iframe(url, height=700, scrolling=True)