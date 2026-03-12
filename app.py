import streamlit as st
import pandas as pd

# Configuração da página com o nome oficial
st.set_page_config(page_title="Rei dos Cartões", layout="wide")

# CSS para o Estilo Dark Profissional
st.markdown("""
    <style>
    .stApp { background-color: #0E1117; color: #FFFFFF; }
    .card {
        background-color: #161B22;
        border: 1px solid #30363D;
        padding: 20px;
        border-radius: 10px;
        text-align: center;
    }
    .fogo { color: #FF4B4B; font-weight: bold; font-size: 28px; }
    </style>
    """, unsafe_allow_html=True)

st.title("👑 REI DOS CARTÕES")
st.markdown("<p style='color: #888;'>Inteligência de Arbitragem & Termômetro de Jogo</p>", unsafe_allow_html=True)

# --- ENTRADA DE DADOS AO VIVO (TERMÔMETRO) ---
st.subheader("🌡️ Termômetro da Partida")
col1, col2, col3 = st.columns(3)

with col1:
    minuto = st.number_input("Minuto atual:", min_value=1, max_value=100, value=20)
with col2:
    faltas = st.number_input("Total de faltas no jogo:", min_value=0, value=10)
with col3:
    # Cálculo da Temperatura Real (Faltas por Minuto)
    temp_jogo = faltas / minuto if minuto > 0 else 0
    st.markdown("<div class='card'>", unsafe_allow_html=True)
    st.write("Frequência de Faltas")
    if temp_jogo > 0.6:
        st.markdown(f"<p class='fogo'>{temp_jogo:.2f} faltas/min</p>", unsafe_allow_html=True)
        st.error("JOGO QUENTE! O pau está comendo.")
    else:
        st.success(f"{temp_jogo:.2f} faltas/min")
        st.write("Jogo morno.")
    st.markdown("</div>", unsafe_allow_html=True)

st.divider()

# --- CRUZAMENTO DE DADOS ---
st.subheader("📊 Análise de Risco")
arbitro = st.selectbox("Árbitro da Partida:", ["Raphael Claus", "Wilton Sampaio", "Anderson Daronco", "Outro"])

# Simulando o cruzamento que você pediu
dados_analise = {
    "Fator": ["Média do Juiz", "Importância do Jogo", "Temperatura Live", "Jogadores Visados"],
    "Avaliação": ["Alta", "Clássico/Decisivo", f"{temp_jogo:.2f} f/min", "Sim (2+ jogadores)"],
    "Score (0-10)": [8, 10, int(temp_jogo * 10 if temp_jogo < 1 else 10), 7]
}
df = pd.DataFrame(dados_analise)
st.table(df)

# --- BOTÃO TELEGRAM ---
if st.button("📲 ENVIAR ALERTA PARA O TELEGRAM"):
    media_score = df["Score (0-10)"].mean()
    if media_score >= 7.5:
        st.warning(f"Sinal Gerado! Score: {media_score:.1f}. Enviando para o Rei dos Cartões Bot...")
        # Aqui entra a função enviar_telegram() assim que tivermos o seu TOKEN
    else:
        st.info("Ainda não atingiu o critério. Temperatura insuficiente.")

st.caption("Rei dos Cartões - Sistema de Monitoramento v3.0")
