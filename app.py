import streamlit as st

st.set_page_config(page_title="The Card King", layout="wide")

st.title("👑 THE CARD KING PRO")
st.subheader("Radar de Arbitragem & Cartões")

st.markdown("### 🔍 Análise de Confronto")

col1, col2 = st.columns(2)

with col1:
    mandante = st.text_input("Time da Casa", "Vasco")
    visitante = st.text_input("Time Visitante", "Botafogo")

with col2:
    arbitro = st.text_input("Árbitro da Partida", "Raphael Claus")
    media_cartoes = st.number_input("Média de Cartões do Juiz", value=5.8)

if st.button("Gerar Relatório de Risco"):
    st.write("---")
    st.write(f"### 📋 Relatório: {mandante} x {visitante}")
    
    if media_cartoes > 5.5:
        st.error(f"🚨 ALERTA: {arbitro} tem tendência alta de cartões ({media_cartoes}).")
        st.success("✅ Sugestão: Over 4.5 Cartões na partida.")
    else:
        st.warning(f"⚠️ Atenção: {arbitro} tem média moderada ({media_cartoes}).")
        st.info("ℹ️ Sugestão: Aguardar o live ou buscar mercado de faltas.")

st.sidebar.info("Sistema Online via Nuvem")
