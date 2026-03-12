import streamlit as st
import pandas as pd

# Configuração Master
st.set_page_config(page_title="Rei dos Cartões", layout="wide", initial_sidebar_state="collapsed")

# Estilização v0 (Visual Premium)
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;700&display=swap');
    html, body, [class*="st-"] { font-family: 'Inter', sans-serif; background-color: #050505; color: white; }
    
    /* Card de Destaque (Hero Section) */
    .hero-card {
        background: linear-gradient(180deg, #111 0%, #000 100%);
        border: 1px solid #FFD700;
        padding: 30px;
        border-radius: 20px;
        text-align: center;
        margin-bottom: 25px;
        box-shadow: 0 0 20px rgba(255, 215, 0, 0.1);
    }
    
    /* Cards de Jogos */
    .game-card {
        background-color: #111;
        border: 1px solid #222;
        padding: 15px;
        border-radius: 12px;
        margin-bottom: 15px;
    }
    
    .live-indicator { color: #FF4B4B; font-weight: bold; font-size: 12px; animation: blinker 1.5s linear infinite; }
    @keyframes blinker { 50% { opacity: 0; } }
    
    .probabilidade { font-size: 42px; font-weight: bold; color: #FFD700; margin: 10px 0; }
    .badge-rigor { background-color: #441111; color: #FF4B4B; padding: 2px 8px; border-radius: 4px; font-size: 10px; }
    </style>
    """, unsafe_allow_html=True)

# Header
st.markdown("### 👑 REI DOS CARTÕES <span style='font-size:12px; color:#888;'>• O SEU RADAR DE ELITE</span>", unsafe_allow_html=True)

# --- SEÇÃO HERO: APOSTA DO REI ---
st.markdown("""
    <div class="hero-card">
        <p style='color: #FFD700; font-size: 14px; font-weight: bold;'>🏆 APOSTA DO REI</p>
        <div style='display: flex; justify-content: space-around; align-items: center;'>
            <div><p style='margin:0;'>Vasco</p><small style='color:#888;'>3.2 faltas/jogo</small></div>
            <div class="probabilidade">88%</div>
            <div><p style='margin:0;'>Flamengo</p><small style='color:#888;'>3.8 faltas/jogo</small></div>
        </div>
        <p style='margin-top: 15px; font-size: 14px;'>Árbitro: <b>Wilton P. Sampaio</b> <span class="badge-rigor">RIGOROSO</span></p>
    </div>
""", unsafe_allow_html=True)

# --- GRID PRINCIPAL ---
col1, col2 = st.columns(2)

with col1:
    st.markdown("#### 🔥 JOGOS QUENTES (LIVE)")
    # Jogo 1
    st.markdown("""
        <div class="game-card">
            <span class="live-indicator">● AO VIVO 34'</span>
            <div style='display: flex; justify-content: space-between; margin-top:10px;'>
                <span>PAL vs COR</span>
                <span style='color: #FFD700;'>38.5</span>
            </div>
            <progress value="85" max="100" style="width: 100%; height: 5px;"></progress>
            <small style='color: #888;'>Média de faltas combinada: ALTA</small>
        </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("#### ⚖️ SCANNER DE ÁRBITROS")
    st.markdown("""
        <div class="game-card">
            <b>Raphael Claus</b> <span class='badge-rigor' style='background-color:#114411; color:#00FF00;'>MÉDIO</span>
            <p style='font-size: 12px; color: #888; margin: 5px 0;'>Últimos 5 jogos: 28 Amarelos | 2 Vermelhos</p>
            <div style='height: 4px; background: #333; border-radius: 2px;'>
                <div style='width: 65%; height: 100%; background: #00FF00; border-radius: 2px;'></div>
            </div>
        </div>
    """, unsafe_allow_html=True)

# Sidebar para Filtros (igual ao v0)
st.sidebar.title("Filtros do Radar")
st.sidebar.checkbox("Juiz Rigoroso", value=True)
st.sidebar.checkbox("Clássicos", value=True)
st.sidebar.checkbox("Média +5.5 Cartões")

if st.sidebar.button("📲 Notificar no Telegram"):
    st.sidebar.success("Alertas Ativados!")
