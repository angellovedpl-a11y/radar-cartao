import streamlit as st
import pandas as pd

# Nome do Projeto
st.set_page_config(page_title="Rei dos Cartões", layout="wide")

# Inteligência de Árbitros (Onde o cruzamento começa)
# Isso aqui vira o seu "ouro" - quanto mais dados aqui, mais lucro.
DB_ARBITROS = {
    "Raphael Claus": {"media": 6.2, "perfil": "Rigoroso", "tendencia": "Over"},
    "Wilton Sampaio": {"media": 5.8, "perfil": "Técnico", "tendencia": "Médio"},
    "Anderson Daronco": {"media": 4.5, "perfil": "Deixa Jogar", "tendencia": "Under"},
    "Flavio Rodrigues": {"media": 5.5, "perfil": "Rigoroso", "tendencia": "Over"}
}

st.title("👑 REI DOS CARTÕES")

# Seleção do Juiz (Cruzamento 1)
arbitro_selecionado = st.selectbox("Selecione o Árbitro do Jogo:", list(DB_ARBITROS.keys()))
dados_juiz = DB_ARBITROS[arbitro_selecionado]

# Entrada do Live (Cruzamento 2)
col1, col2 = st.columns(2)
with col1:
    minuto = st.number_input("Minuto Atual", value=20)
with col2:
    faltas = st.number_input("Faltas Totais", value=12)

# O CÁLCULO DE CRUZAMENTO (A Mágica)
temp_live = faltas / minuto if minuto > 0 else 0
# Score de 0 a 100
score_final = (dados_juiz['media'] * 10) + (temp_live * 40)

# INTERFACE DE DECISÃO
st.divider()
st.subheader(f"Análise: {arbitro_selecionado}")

c1, c2, c3 = st.columns(3)
c1.metric("Média Histórica", dados_juiz['media'])
c2.metric("Temperatura Live", f"{temp_live:.2f}")
c3.metric("SCORE DE VALOR", f"{score_final:.1f}%")

if score_final > 75:
    st.error("🚨 SINAL CONFIRMADO: Entrada Forte em Over Cartões!")
elif score_final > 60:
    st.warning("⚠️ OBSERVAR: Jogo esquentando, aguarde valor na Odd.")
else:
    st.info("❄️ SEM VALOR: Jogo muito calmo para o perfil do juiz.")
