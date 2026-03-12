import streamlit as st
import pandas as pd

# Configuração de Interface de Alta Conversão
st.set_page_config(page_title="Rei dos Cartões - Scanner", layout="wide")

st.markdown("""
    <style>
    body { background-color: #000; color: #fff; }
    .opportunity-card {
        background: #111;
        border-left: 5px solid #00FF41;
        padding: 20px;
        border-radius: 10px;
        margin-bottom: 20px;
    }
    .odd-box {
        background: #222;
        padding: 10px;
        border-radius: 5px;
        text-align: center;
        min-width: 80px;
    }
    .profit-text { color: #00FF41; font-weight: bold; font-size: 20px; }
    .house-text { color: #888; font-size: 12px; }
    </style>
    """, unsafe_allow_html=True)

st.title("🎯 SCANNER DE OPPORTUNIDADES")
st.markdown("### Encontrando brechas nas Odds de Cartões")

# --- LÓGICA DE CÁLCULO DE VALOR ---
with st.sidebar:
    st.header("⚙️ Ajuste de Mercado")
    odd_casa = st.number_input("Odd Atual (Bet365/Betano):", value=2.20, step=0.05)
    prob_real = st.slider("Probabilidade do Rei (%):", 0, 100, 65)
    
    # Cálculo: Odd Justa = 100 / Probabilidade
    odd_justa = 100 / prob_real if prob_real > 0 else 0
    # Valor = (Odd Casa / Odd Justa) - 1
    valor = (odd_casa / odd_justa) - 1 if odd_justa > 0 else 0

# --- EXIBIÇÃO DA OPORTUNIDADE ---
st.markdown(f"""
    <div class="opportunity-card">
        <div style='display: flex; justify-content: space-between; align-items: center;'>
            <div>
                <h2 style='margin:0;'>VASCO vs FLAMENGO</h2>
                <p style='color:#888;'>Mercado: Over 5.5 Cartões</p>
            </div>
            <div style='text-align: right;'>
                <span class="profit-text">{valor*100:.1f}% DE VALOR</span><br>
                <small>VALOR ESPERADO POSITIVO (EV+)</small>
            </div>
        </div>
        <hr style='border: 0.1px solid #333;'>
        <div style='display: flex; gap: 20px; justify-content: center; margin-top:15px;'>
            <div class="odd-box">
                <span class="house-text">ODD CASA</span><br>
                <span style='font-size: 24px; color: #FF4B4B;'>{odd_casa:.2f}</span>
            </div>
            <div style='font-size: 30px; align-self: center;'> VS </div>
            <div class="odd-box">
                <span class="house-text">ODD DO REI (JUSTA)</span><br>
                <span style='font-size: 24px; color: #00FF41;'>{odd_justa:.2f}</span>
            </div>
        </div>
    </div>
""", unsafe_allow_html=True)

# --- RECOMENDAÇÃO DE GESTÃO ---
col1, col2 = st.columns(2)
with col1:
    st.info(f"**Análise do Rei:** A casa está subestimando este jogo em {valor*100:.0f}%. O histórico do árbitro e a temperatura live indicam que essa Odd deveria estar em {odd_justa:.2f}.")
with col2:
    st.warning(f"**Sugestão de Entrada:** {min(5.0, valor*20):.1f}% da sua banca (Gestão de Risco Moderada).")

st.divider()

# --- TABELA DE MONITORAMENTO DE ODDS ---
st.markdown("#### 📡 Monitor de Radar - Outros Jogos")
monitor_dados = {
    "Jogo": ["Palmeiras x SPFC", "Cruzeiro x Galo"],
    "Odd Casa": [1.85, 2.10],
    "Odd Rei": [1.90, 1.75],
    "Status": ["Aguardar Subir", "ENTRAR (VALOR)"]
}
st.table(pd.DataFrame(monitor_dados))
