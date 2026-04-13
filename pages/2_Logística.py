import streamlit as st

st.title("📦 Projeto: Dashboard de Logística")

st.subheader("🎯 Objetivo")
st.write("""
Desenvolver um dashboard logístico para monitoramento de entregas, pedidos e devoluções,
permitindo análise operacional e identificação de gargalos no processo.
""")

st.subheader("📊 Sobre o Dashboard")
st.write("""
O dashboard foi desenvolvido no Power BI com foco em indicadores operacionais:

🔹 Performance de Entregas:
- Entregas no prazo vs atrasadas
- Análise por status
- Evolução trimestral

🔹 Gestão de Pedidos:
- Volume total de pedidos
- Acompanhamento por período
- Distribuição por tipo de veículo

🔹 Controle de Devoluções:
- Devoluções por tipo (resfriado, refrigerado, seco)
- Principais motivos de devolução
- Análise geográfica (UF e cidade)
""")

st.subheader("💡 Principais Insights")
st.write("""
- Alto volume de entregas atrasadas impactando a operação
- Identificação dos principais motivos de devolução (ex: desistência do cliente)
- Diferença de performance entre tipos de transporte
- Possibilidade de atuação preventiva em regiões específicas
""")

st.subheader("⚙️ Diferencial do Projeto")
st.write("""
Este dashboard permite uma visão completa da operação logística, integrando indicadores
de desempenho, devoluções e distribuição geográfica, facilitando a tomada de decisão
e otimização de processos.
""")

st.divider()

# 🔗 LINK DO POWER BI
url = "https://app.fabric.microsoft.com/view?r=eyJrIjoiMmYyMTZkNDItOWRkYS00MTMxLWIzOGEtNmE0MmI1ZmI5M2ZlIiwidCI6ImE4Y2Y0YWYwLTc5NzctNGQ4Zi1iNjQzLTJjNWJhYTNlZjQxZCJ9"

st.link_button("🔗 Abrir Dashboard no Power BI", url)

st.divider()

# 📺 EMBED
st.subheader("📺 Visualização do Dashboard")

st.components.v1.iframe(url, height=700, scrolling=True)
