import streamlit as st
import pandas as pd
import plotly.graph_objects as go

# 1. Configuração Master (Nome e Favicon)
st.set_page_config(page_title="Rei dos Cartões", layout="wide", initial_sidebar_state="collapsed")

# 2. CSS de Elite (Aparência v0 / Glassmorphism)
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;700&display=swap');
    html, body, [class*="st-"] { font-family: 'Inter', sans-serif; background-color: #050505; color: white; }
    
    .main-card {
        background: linear-gradient(145deg, #111 0%, #000 100%);
        border: 1px solid #333;
        padding: 25px;
        border-radius: 20px;
        text-align: center;
        box-shadow: 0 10px 30px rgba(0,0,0,0.5);
    }
    
    .live-badge {
        background-color: #FF4B4B;
        color: white;
        padding: 2px 10px;
        border-radius: 50px;
        font-size: 10px;
        font-weight: bold;
        animation: pulse 1.5s infinite;
    }
    
    @keyframes pulse { 0% { opacity: 1; } 50% { opacity: 0.3; } 100% { opacity: 1; } }
    
    .probabilidade { font-size: 48px; font-weight: bold; color: #00FF41; margin: 10px 0; }
    .label-mini { color: #888; font-size: 12px; text-transform: uppercase; letter-spacing: 1px; }
    </style>
    """, unsafe_allow_html=True)

# 3. Cabeçalho
st.markdown("### 👑 REI DOS CARTÕES <span style='color:#444'>| TERMINAL DE INTELIGÊNCIA</span>", unsafe_allow_html=True)

# 4. Inteligência de Dados (O Cérebro)
DB_ARBITROS = {
    "Raphael Claus": 6.2, "Wilton Sampaio": 5.8, "Anderson Daronco": 4.5, "Flavio Rodrigues": 5.5
}

# --- BARRA LATERAL (ENTRADA DE DADOS) ---
with st.sidebar:
    st.header("🎮 Controle do Jogo")
    arbitro = st.selectbox("Árbitro:", list(DB_ARBITROS.keys()))
    minuto = st.number_input("Minuto Atual:", value=25)
    faltas = st.number_input("Faltas Totais:", value=15)
    st.divider()
    if st.button("📲 DISPARAR PRO TELEGRAM"):
        st.success("Sinal enviado!")

# --- CÁLCULO DE CRUZAMENTO ---
media_juiz = DB_ARBITROS[arbitro]
temp_live = faltas / minuto if minuto > 0 else 0
# O Score Final cruza os dois dados (Lógica Lucrativa)
score_final = int((media_juiz * 8) + (temp_live * 40))
if score_final > 100: score_final = 100

# --- INTERFACE VISUAL (O QUE VOCÊ GOSTOU) ---
col1, col2 = st.columns([1.5, 1])

with col1:
    st.markdown(f"""
        <div class="main-card">
            <span class="live-badge">● LIVE ANALYTICS</span>
            <p style='margin-top:20px;' class="label-mini">Probabilidade de Cartão</p>
            <div class="probabilidade">{score_final}%</div>
            <div style='display: flex; justify-content: space-around; margin-top:20px;'>
                <div><p class="label-mini">Juiz</p><p>{arbitro} ({media_juiz})</p></div>
                <div><p class="label-mini">Ritmo</p><p>{temp_live:.2f} faltas/min</p></div>
            </div>
        </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("#### 🌡️ PRESSÃO DE JOGO")
    # Gráfico de Pressão
    fig = go.Figure(go.Indicator(
        mode = "gauge+number",
        value = temp_live,
        domain = {'x': [0, 1], 'y': [0, 1]},
        title = {'text': "Faltas p/ Min", 'font': {'size': 14, 'color': "#888"}},
        gauge = {
            'axis': {'range': [None, 1.5], 'tickwidth': 1, 'tickcolor': "white"},
            'bar': {'color': "#00FF41" if temp_live < 0.7 else "#FF4B4B"},
            'bgcolor': "#111",
            'borderwidth': 2,
            'bordercolor': "#333",
            'steps': [
                {'range': [0, 0.6], 'color': '#111'},
                {'range': [0.6, 1.5], 'color': '#220000'}],
        }))
    fig.update_layout(paper_bgcolor='rgba(0,0,0,0)', plot_bgcolor='rgba(0,0,0,0)', 
                      font={'color': "white", 'family': "Inter"}, height=250, margin=dict(l=20, r=20, t=50, b=20))
    st.plotly_chart(fig, use_container_width=True)

st.divider()

# --- TABELA DE MONITORAMENTO ---
st.markdown("#### 📋 MONITOR DE SCANNER")
st.markdown("""
    <div style='background-color:#111; padding:15px; border-radius:10px; border:1px solid #222;'>
        <div style='display:flex; justify-content:space-between; color:#888; font-size:12px;'>
            <span>PARTIDA</span><span>STATUS</span><span>SCORE</span>
        </div>
        <hr style='border:0.5px solid #222;'>
        <div style='display:flex; justify-content:space-between;'>
            <span><b>Vasco x Flamengo</b></span><span style='color:#FF4B4B;'>🔥 QUENTE</span><span style='color:#00FF41;'>88%</span>
        </div>
    </div>
""", unsafe_allow_html=True)
