import streamlit as st
import pandas as pd
import numpy as np

# Configuração estilo Bloomberg/Dark
st.set_page_config(page_title="THE CARD KING PRO", layout="wide")

# CSS para forçar o Dark Mode e estilo profissional
st.markdown("""
    <style>
    .main { background-color: #0E1117; color: #FFFFFF; }
    .stButton>button { width: 100%; border-radius: 5px; height: 3em; background-color: #FF4B4B; color: white; }
    .stMetric { background-color: #161B22; padding: 15px; border-radius: 10px; border: 1px solid #30363D; }
    </style>
    """, unsafe_allow_html=True)

st.title("👑 THE CARD KING PRO")
st.subheader("Análise Estatística de Arbitragem")

# Barra Lateral com Filtros
st.sidebar.header("Configurações do Robô")
site_fonte = st.sidebar.selectbox("Fonte de Dados", ["Transfermarkt", "FBRef", "BetMines (API)"])
st.sidebar.write(f"🟢 Status: Conectado")

# Dados para o Radar (Simulando o início do Scraping)
data = {
    'Árbitro': ['Raphael Claus', 'Wilton Sampaio', 'Anderson Daronco', 'Flavio Rodrigues', 'Bráulio Machado'],
    'Jogos': [12, 15, 10, 14, 11],
    'Média Amarelos': [5.2, 6.1, 4.8, 5.5, 6.3],
    'Vermelhos': [3, 5, 1, 4, 6]
}
df_arbitros = pd.DataFrame(data)

# Interface Principal
col1, col2 = st.columns([1, 2])

with col1:
    st.markdown("### 🔍 Radar de Escala")
    arbitro_selecionado = st.selectbox("Selecione o Árbitro", df_arbitros['Árbitro'])
    
    stats = df_arbitros[df_arbitros['Árbitro'] == arbitro_selecionado].iloc[0]
    
    st.metric("Média de Amarelos", stats['Média Amarelos'])
    st.metric("Total de Vermelhos", int(stats['Vermelhos']))

with col2:
    st.markdown(f"### 📊 Comparativo de Médias")
    st.bar_chart(df_arbitros.set_index('Árbitro')['Média Amarelos'])

st.divider()

# Lógica de Alerta
st.markdown("### ⚡ Veredito do King")
if stats['Média Amarelos'] >= 5.5:
    st.error(f"🔥 JOGO QUENTE: {arbitro_selecionado} tem média de {stats['Média Amarelos']}. Tendência Over Cartões.")
else:
    st.info(f"⚖️ JOGO REGULAR: {arbitro_selecionado} tem média de {stats['Média Amarelos']}. Estudo para Live.")

st.caption("Sistema Online - Engine v2.0")
