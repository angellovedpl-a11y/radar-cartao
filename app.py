import streamlit as st
import pandas as pd
import time

# Configuração Visual Profissional
st.set_page_config(page_title="THE CARD KING PRO", layout="wide")

st.markdown("""
    <style>
    .stApp { background-color: #050505; color: #FFFFFF; }
    .status-box { background-color: #111; border: 1px solid #333; padding: 15px; border-radius: 10px; }
    .calor-alto { color: #FF4B4B; font-weight: bold; font-size: 24px; }
    </style>
    """, unsafe_allow_html=True)

st.title("👑 THE CARD KING PRO")
st.subheader("🔥 Monitor de Temperatura de Jogo (LIVE)")

# Simulando a leitura de um jogo ao vivo (Ex: Vasco x Flamengo)
col1, col2, col3 = st.columns(3)

with col1:
    st.markdown("<div class='status-box'>", unsafe_allow_html=True)
    minuto = st.slider("Minuto do Jogo", 0, 90, 25)
    st.markdown("</div>", unsafe_allow_html=True)

with col2:
    st.markdown("<div class='status-box'>", unsafe_allow_html=True)
    faltas = st.number_input("Total de Faltas Atual", value=12)
    st.markdown("</div>", unsafe_allow_html=True)

# CÁLCULO DA TEMPERATURA (A Lógica que você pediu)
# Se o jogo tem mais de 0.5 faltas por minuto, a chapa está esquentando.
freq_faltas = faltas / minuto if minuto > 0 else 0

with col3:
    st.markdown("<div class='status-box'>", unsafe_allow_html=True)
    st.write("Frequência de Faltas")
    if freq_faltas > 0.6:
        st.markdown(f"<p class='calor-alto'>{freq_faltas:.2f} faltas/min</p>", unsafe_allow_html=True)
        st.error("JOGO INCENDIÁRIO: Juiz sob pressão!")
    else:
        st.success(f"{freq_faltas:.2f} faltas/min")
        st.write("Jogo controlado.")
    st.markdown("</div>", unsafe_allow_html=True)

st.divider()

# TABELA DE CRUIZAMENTO (O que você quer ver)
st.markdown("### 📊 Inteligência de Mercado")
dados_live = {
    "Critério": ["Média do Juiz", "Importância", "Jogadores 'Brabos' em Campo", "Ritmo de Faltas"],
    "Status": ["Claus (Alta)", "Clássico", "3 Titulares Visados", f"{freq_faltas:.2f}/min"],
    "Peso (0-10)": [9, 10, 8, int(freq_faltas * 10)]
}
df_analise = pd.DataFrame(dados_live)
st.table(df_analise)

# BOTÃO DE ALERTA TELEGRAM
if st.button("🚀 Gerar Relatório de Valor para Telegram"):
    score_final = df_analise["Peso (0-10)"].mean()
    if score_final > 7:
        st.warning(f"Sinal Gerado! Score de Confiança: {score_final:.1f}/10. Enviando para o celular...")
    else:
        st.info("Ainda não atingiu o critério de entrada. Aguarde a temperatura subir.")
