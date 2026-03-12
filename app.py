import streamlit as st
import pandas as pd

# Configuração de App de Elite
st.set_page_config(page_title="Rei dos Cartões", layout="wide", initial_sidebar_state="collapsed")

# Estilização CSS Superior (Visual Premium v0)
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;700&display=swap');
    html, body, [class*="st-"] { font-family: 'Inter', sans-serif; background-color: #050505; color: white; }
    
    .main-title { font-size: 32px; font-weight: bold; color: #FFD700; margin-bottom: 20px; }
    
    /* Card Principal de Oportunidade */
    .opportunity-card {
        background: linear-gradient(180deg, #111 0%, #000 100%);
        border: 1px solid #333;
        padding: 25px;
        border-radius: 20px;
        margin-bottom: 25px;
        border-top: 4px solid #FFD700;
    }
    
    .player-card {
        background: #111;
        border: 1px solid #222;
        padding: 15px;
        border-radius: 15px;
        transition: 0.3s;
    }
    .player-card:hover { border-color: #FFD700; }
    
    .odd-tag {
        background: #222;
        padding: 8px 15px;
        border-radius: 8px;
        text-align: center;
        border: 1px solid #444;
    }
    
    .value-green { color: #00FF41; font-weight: bold; font-size: 18px; }
    .label-gray { color: #888; font-size: 11px; text-transform: uppercase; }
    </style>
    """, unsafe_allow_html=True)

# Header
st.markdown("<div class='main-title'>👑 REI DOS CARTÕES</div>", unsafe_allow_html=True)

# --- DESTAQUE DO DIA (OVER/UNDER GERAL) ---
st.markdown("### 🏟️ JOGO EM DESTAQUE (OVER 5.5)")
st.markdown("""
    <div class="opportunity-card">
        <div style='display: flex; justify-content: space-between; align-items: center;'>
            <div>
                <h2 style='margin:0;'>VASCO vs FLAMENGO</h2>
                <p style='color:#888;'>Árbitro: <b>Raphael Claus</b> | Média: 6.2 Cartões</p>
            </div>
            <div style='text-align: right;'>
                <span class="value-green">+18.5% VALUE</span><br>
                <small style='color:#FFD700;'>🔥 ALTA PROBABILIDADE</small>
            </div>
        </div>
        <div style='display: flex; gap: 20px; margin-top: 20px; justify-content: start;'>
            <div class="odd-tag">
                <span class="label-gray">Odd Bet365</span><br>
                <b style='font-size: 22px; color: #FF4B4B;'>2.62</b>
            </div>
            <div class="odd-tag">
                <span class="label-gray">Odd Real (Rei)</span><br>
                <b style='font-size: 22px; color: #00FF41;'>2.10</b>
            </div>
        </div>
    </div>
""", unsafe_allow_html=True)

# --- MERCADO DE JOGADORES (O QUE ATRAI O APOSTADOR) ---
st.markdown("### 👤 SELEÇÃO DE JOGADORES (PROPS)")
col1, col2, col3 = st.columns(3)

# Lista de jogadores "Brabos"
jogadores = [
    {"nome": "MEDEL", "time": "Vasco", "odd": "4.33", "real": "3.10", "valor": "+28%"},
    {"nome": "F. MELO", "time": "Flu", "odd": "2.85", "real": "2.10", "valor": "+26%"},
    {"nome": "KANNEMANN", "time": "Grêmio", "odd": "3.20", "real": "2.50", "valor": "+21%"}
]

for i, jogador in enumerate(jogadores):
    with [col1, col2, col3][i]:
        st.markdown(f"""
            <div class="player-card">
                <p style='margin:0; font-weight:bold;'>{jogador['nome']}</p>
                <p class="label-gray">{jogador['time']}</p>
                <div style='display: flex; justify-content: space-between; margin-top: 15px;'>
                    <div class="odd-tag" style='padding: 5px 10px;'>
                        <small style='font-size:9px;'>ODD CASA</small><br><b>{jogador['odd']}</b>
                    </div>
                    <div style='text-align:right;'>
                        <span class="value-green">{jogador['valor']}</span><br>
                        <small class="label-gray">VALUE</small>
                    </div>
                </div>
            </div>
        """, unsafe_allow_html=True)

st.divider()

# --- AÇÃO E NOTIFICAÇÃO ---
st.markdown("#### ⚙️ CONFIGURAR ALERTAS DE ODD")
c1, c2 = st.columns(2)
with c1:
    st.slider("Notificar se o valor for maior que:", 5, 50, 15, format="%d%%")
with c2:
    if st.button("🚀 ATIVAR RADAR NO TELEGRAM"):
        st.success("Radar Ativo! Você receberá as brechas de odds no celular.")

st.sidebar.image("https://img.icons8.com/ios-filled/50/FFFFFF/poker-cards.png", width=50)
st.sidebar.title("MENU REI")
st.sidebar.info("O Rei dos Cartões analisa 12 ligas em tempo real buscando erros das casas de apostas.")
