import streamlit as st
import pandas as pd
import plotly.graph_objects as go

# Configuração de App de Elite
st.set_page_config(page_title="Rei dos Cartões - Terminal", layout="wide", initial_sidebar_state="collapsed")

# CSS de Terminal Profissional (Estilo Bloomberg/V0)
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=JetBrains+Mono:wght@400;700&display=swap');
    
    html, body, [class*="st-"] { font-family: 'JetBrains Mono', monospace; background-color: #050505; color: #00FF41; }
    
    /* Card de SINAL DE OURO */
    .signal-card {
        background: rgba(255, 75, 75, 0.1);
        border: 2px solid #FF4B4B;
        padding: 20px;
        border-radius: 15px;
        text-align: center;
        margin-bottom: 20px;
        animation: pulse 2s infinite;
    }
    
    @keyframes pulse {
        0% { box-shadow: 0 0 0 0 rgba(255, 75, 75, 0.4); }
        70% { box-shadow: 0 0 0 15px rgba(255, 75, 75, 0); }
        100% { box-shadow: 0 0 0 0 rgba(255, 75, 75, 0); }
    }

    .stat-value { font-size: 30px; font-weight: bold; color: #FFFFFF; }
    .label { color: #888; font-size: 12px; text-transform: uppercase; }
    
    /* Botão de Compra/Sinal */
    .stButton>button {
        background-color: #00FF41; color: black; border: none;
        font-weight: bold; width: 100%; border-radius: 10px; height: 50px;
    }
    </style>
    """, unsafe_allow_html=True)

# Top Bar
st.markdown("### 🛰️ REI DOS CARTÕES <span style='color:#555'>| TERMINAL DE ALTA FREQUÊNCIA v4.0</span>", unsafe_allow_html=True)

# --- NÍVEL 1: SCANNER DE OPORTUNIDADES (O QUE VENDE) ---
st.markdown("""
    <div class="signal-card">
        <p style='color: #FF4B4B; margin:0;'>🔥 ALERTA DE VALOR DETECTADO (EV+)</p>
        <h2 style='margin:10px 0; color:white;'>VASCO vs FLAMENGO</h2>
        <div style='display: flex; justify-content: space-around;'>
            <div><p class="label">Prob. Casa</p><p style='color:white;'>45% (Odd 2.20)</p></div>
            <div><p class="label">Prob. REI</p><p style='color:#00FF41; font-size:20px;'>78%</p></div>
            <div><p class="label">Margem de Lucro</p><p style='color:#00FF41;'>+33.5%</p></div>
        </div>
    </div>
""", unsafe_allow_html=True)

# --- NÍVEL 2: TERMÔMETRO LIVE ---
col1, col2 = st.columns([1, 2])

with col1:
    st.markdown("#### 🌡️ TERMÔMETRO LIVE")
    minuto = st.select_slider("Tempo de Jogo", options=range(0, 91), value=28)
    faltas = st.number_input("Faltas Totais", value=14)
    
    temp = faltas / minuto if minuto > 0 else 0
    
    st.markdown(f"""
        <div style='background:#111; padding:20px; border-radius:10px; border-left: 5px solid {"#FF4B4B" if temp > 0.6 else "#00FF41"}'>
            <p class="label">Pressão de Cartão/Min</p>
            <p class="stat-value">{temp:.2f}</p>
            <p style='color: {"#FF4B4B" if temp > 0.6 else "#888"}'>
                {"⚠️ RITMO ACIMA DA MÉDIA" if temp > 0.6 else "Ritmo Normal"}
            </p>
        </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("#### 📈 ÍNDICE DE EXPLOSÃO (Últimos 10 min)")
    # Gráfico de linha mostrando a subida das faltas
    fig = go.Figure()
    fig.add_trace(go.Scatter(x=[10, 15, 20, 25, 28], y=[2, 4, 5, 10, 14], 
                             mode='lines+markers', line=dict(color='#00FF41', width=3)))
    fig.update_layout(height=200, margin=dict(l=0, r=0, t=0, b=0), 
                      paper_bgcolor='rgba(0,0,0,0)', plot_bgcolor='rgba(0,0,0,0)',
                      xaxis=dict(showgrid=False), yaxis=dict(showgrid=False))
    st.plotly_chart(fig, use_container_width=True)

# --- NÍVEL 3: LISTA DE MONITORAMENTO ---
st.markdown("#### 📋 RADAR DA RODADA")
grid_dados = {
    "PARTIDA": ["PAL x COR", "CRU x ATM", "FOR x CEA"],
    "JUIZ": ["R. Claus", "Daronco", "W. Sampaio"],
    "TEMP": ["0.45", "0.82 🔥", "0.55"],
    "STATUS": ["Estudando", "ENTRAR AGORA", "Aguardando"]
}
st.table(pd.DataFrame(grid_dados))

# Barra Lateral Profissional
with st.sidebar:
    st.title("⚙️ CONFIG")
    st.write("Conexão API: 🟢 OK")
    st.write("Filtro: Juízes Rigorosos")
    if st.button("CONFIGURAR ALERTAS TELEGRAM"):
        st.success("BOT ATIVADO!")
