import streamlit as st
from pathlib import Path

# ===== CONFIG =====
st.set_page_config(
    page_title="Portfólio | Kaique",
    page_icon="📊",
    layout="wide"
)

# ===== CSS (ROBUSTO PRA DEPLOY) =====
def load_css():
    css_path = Path(__file__).parent / "assets" / "style.css"
    
    if css_path.exists():
        with open(css_path) as f:
            st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)
    else:
        st.warning("CSS não encontrado.")

load_css()

# ===== HEADER =====
st.title("📊 Portfólio de Dados")
st.subheader("Kaique Roberto")
st.write("Analista de Dados | Power BI | Python | VBA")

st.divider()

# ===== SOBRE =====
st.markdown("""
### 👋 Sobre mim

Analista de dados com foco em transformar dados em decisões estratégicas.  
Experiência com Power BI no dia a dia e evolução contínua em Python e automações.
""")

st.divider()

# ===== PROJETOS =====
st.markdown("## 🚀 Projetos")

col1, col2, col3 = st.columns(3)

# ===== CARD 1 - FINANCEIRO =====
with col1:
    st.markdown('<div class="card">', unsafe_allow_html=True)

    st.markdown("### 📊 Financeiro")
    st.write("DRE + Simulação de fluxo de caixa")

    if st.button("Ver Projeto", key="fin"):
        st.switch_page("pages/1_financeiroDRE.py")

    st.markdown('</div>', unsafe_allow_html=True)

# ===== CARD 2 - LOGÍSTICA =====
with col2:
    st.markdown('<div class="card">', unsafe_allow_html=True)

    st.markdown("### 📦 Logística")
    st.write("Operação, entregas e devoluções")

    if st.button("Ver Projeto", key="log"):
        st.switch_page("pages/2_logistica.py")

    st.markdown('</div>', unsafe_allow_html=True)

# ===== CARD 3 - VENDAS =====
with col3:
    st.markdown('<div class="card">', unsafe_allow_html=True)

    st.markdown("### 📈 Vendas")
    st.write("Faturamento vs Meta e performance")

    if st.button("Ver Projeto", key="ven"):
        st.switch_page("pages/3_Vendas.py")

    st.markdown('</div>', unsafe_allow_html=True)