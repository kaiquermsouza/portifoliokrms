import streamlit as st

st.title("📊 Projeto: DRE AMBEV + Simulador Financeiro")

st.subheader("🎯 Objetivo")
st.write("""
Desenvolver um dashboard gerencial baseado na DRE da AMBEV, permitindo análise de desempenho financeiro
e simulação de cenários através de um fluxo de caixa projetado.
""")

st.subheader("📊 Sobre o Dashboard")
st.write("""
O projeto foi desenvolvido no Power BI com dois principais focos:

🔹 Análise da DRE:
- Receita, custos e despesas
- Margens e indicadores financeiros
- Evolução temporal dos resultados

🔹 Simulador Financeiro:
- Projeção de fluxo de caixa
- Simulação de cenários futuros
- Apoio à tomada de decisão estratégica
""")

st.subheader("💡 Principais Insights")
st.write("""
- Identificação dos principais drivers de resultado (receita vs custos)
- Impacto de variações financeiras no resultado final
- Capacidade de simular decisões antes de aplicá-las na prática
""")

st.subheader("⚙️ Diferencial do Projeto")
st.write("""
Este projeto vai além de um dashboard tradicional, incorporando um simulador financeiro
que permite testar cenários e prever impactos no fluxo de caixa, aproximando a análise
de dados da tomada de decisão real.
""")

st.divider()

# 🔗 LINK DO POWER BI
url = "https://app.fabric.microsoft.com/view?r=eyJrIjoiMjk4MTI0ZGYtYzAyYy00YTQ1LWE4YTItMjY2ZTZmNGFkZmI1IiwidCI6ImE4Y2Y0YWYwLTc5NzctNGQ4Zi1iNjQzLTJjNWJhYTNlZjQxZCJ9"

st.link_button("🔗 Abrir Dashboard no Power BI", url)

st.divider()

# 📺 EMBED
st.subheader("📺 Visualização do Dashboard")

st.components.v1.iframe(url, height=700, scrolling=True)
