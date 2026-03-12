import streamlit as st
import pandas as pd

st.set_page_config(page_title="Rei dos Cartões - Scanner", layout="wide")

# Estilo focado em Leitura de Odds
st.markdown("""
    <style>
    body { background-color: #000; color: #fff; }
    .market-box {
        background: #111;
        border: 1px solid #333;
        padding: 15px;
        border-radius: 12px;
        margin-bottom: 10px;
    }
    .value-tag {
        color: #00FF41;
        font-weight: bold;
        background: rgba(0, 255, 65, 0.1);
        padding: 2px 8px;
        border-radius: 4px;
    }
    .player-name { color: #FFD700; font-weight: bold; font-size: 18px; }
    </style>
    """, unsafe_allow_html=True)

st.title("👑 REI DOS CARTÕES")
st.markdown("#### Scanner Especialista: Over/Under & Player Prop")

# --- DATABASE DE JOGADORES (A INTELIGÊNCIA) ---
# Aqui você pode alimentar com os "brabos" do campeonato
db_jogadores = {
    "Medel": {"time": "Vasco", "media": 0.45, "odd_real": 2.22},
    "Felipe Melo": {"time": "Fluminense", "media": 0.52, "odd_real": 1.92},
    "Kannemann": {"time": "Grêmio", "media": 0.48, "odd_real": 2.08}
}

# --- SEÇÃO 1: MERCADO DE OVER GERAL ---
st.subheader("🏟️ Over/Under do Jogo")
with st.container():
    st.markdown("""
        <div class="market-box">
            <div style='display: flex; justify-content: space-between;'>
                <span><b>Vasco x Flamengo</b> (Over 5.5 Cartões)</span>
                <span class="value-tag">+14% VALUE</span>
            </div>
            <div style='display: flex; gap: 30px; margin-top:10px;'>
                <div><small>CASA (Bet365)</small><br><b style='font-size:20px;'>2.45</b></div>
                <div><small>ODD JUSTA</small><br><b style='font-size:20px; color:#00FF41;'>2.15</b></div>
            </div>
        </div>
    """, unsafe_allow_html=True)

# --- SEÇÃO 2: MERCADO DE JOGADORES (PLAYER CARDS) ---
st.subheader("👤 Oportunidades em Jogadores")
col1, col2 = st.columns(2)

# O robô varre a lista e encontra onde a odd da casa (ex: 4.00) está maior que a nossa
for nome, dados in list(db_jogadores.items())[:2]:
    with col1 if nome == "Medel" else col2:
        odd_casa_jogador = 4.33 if nome == "Medel" else 3.10 # Simulação de odd da casa
        valor_jogador = (odd_casa_jogador / dados['odd_real']) - 1
        
        st.markdown(f"""
            <div class="market-box" style="border-top: 3px solid #FFD700;">
                <span class="player-name">{nome}</span> <small>({dados['time']})</small>
                <div style='display: flex; justify-content: space-between; margin-top:10px;'>
                    <div><small>ODD CASA</small><br><b>{odd_casa_jogador:.2f}</b></div>
                    <div><small>ODD REI</small><br><b style='color:#00FF41;'>{dados['odd_real']:.2f}</b></div>
                    <div style='text-align:right;'><span class="value-tag">{valor_jogador*100:.1f}%</span></div>
                </div>
            </div>
        """, unsafe_allow_html=True)

# --- CONFIGURAÇÃO DE ALERTA ---
st.sidebar.header("🎯 Filtro de Sinais")
min_value = st.sidebar.slider("Valor Mínimo (%)", 5, 50, 10)
if st.sidebar.button("🚀 Enviar Sugestão de Stake"):
    st.sidebar.info("Calculando Gestão de Banca...")
