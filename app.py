import streamlit as st
import pandas as pd

st.set_page_config(page_title="Rei dos Cartões", layout="wide")

st.markdown("""
    <style>
    body { background-color: #050505; color: white; font-family: 'Inter', sans-serif; }
    .cartao-box {
        background: #111;
        border: 1px solid #333;
        padding: 20px;
        border-radius: 15px;
        margin-bottom: 20px;
    }
    .titulo-mercado { color: #FFD700; font-weight: bold; font-size: 20px; }
    .valor-lucro { color: #00FF41; font-weight: bold; font-size: 24px; }
    .box-preco { background: #222; padding: 10px; border-radius: 8px; text-align: center; border: 1px solid #444; }
    </style>
    """, unsafe_allow_html=True)

st.title("👑 REI DOS CARTÕES")
st.write("Monitorando falhas nos mercados de cartões em tempo real.")

# --- SEÇÃO 1: CARTÕES NO JOGO ---
st.markdown("### 🏟️ Mercado: Total de Cartões (Over)")
st.markdown("""
    <div class="cartao-box" style="border-left: 5px solid #FFD700;">
        <div style='display: flex; justify-content: space-between;'>
            <span class="titulo-mercado">VASCO vs FLAMENGO</span>
            <span class="valor-lucro">+20% DE MARGEM</span>
        </div>
        <p style='color:#888;'>Previsão: Mais de 5.5 cartões na partida</p>
        <div style='display: flex; gap: 20px; margin-top: 15px;'>
            <div class="box-preco">
                <small style='color:#888;'>SITE DE APOSTA PAGA</small><br>
                <b style='font-size: 22px; color: #FF4B4B;'>2.50</b>
            </div>
            <div class="box-preco">
                <small style='color:#888;'>O REI DIZ QUE VALE</small><br>
                <b style='font-size: 22px; color: #00FF41;'>2.00</b>
            </div>
        </div>
    </div>
""", unsafe_allow_html=True)

# --- SEÇÃO 2: CARTÕES PARA JOGADORES ---
st.markdown("### 👤 Mercado: Cartão para Jogador Específico")
col1, col2 = st.columns(2)

with col1:
    st.markdown("""
        <div class="cartao-box" style="border-top: 4px solid #FFD700;">
            <p class="titulo-mercado">MEDEL (Vasco)</p>
            <p style='color:#888; font-size:14px;'>Motivo: 45% de chance de levar amarelo hoje</p>
            <div style='display: flex; justify-content: space-between; margin-top: 15px;'>
                <div class="box-preco" style='width:45%;'>
                    <small style='font-size:10px;'>O SITE PAGA</small><br><b>4.33</b>
                </div>
                <div class="box-preco" style='width:45%;'>
                    <small style='font-size:10px;'>O REI DIZ</small><br><b style='color:#00FF41;'>2.20</b>
                </div>
            </div>
        </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
        <div class="cartao-box" style="border-top: 4px solid #FFD700;">
            <p class="titulo-mercado">F. MELO (Fluminense)</p>
            <p style='color:#888; font-size:14px;'>Motivo: Histórico pesado em clássicos</p>
            <div style='display: flex; justify-content: space-between; margin-top: 15px;'>
                <div class="box-preco" style='width:45%;'>
                    <small style='font-size:10px;'>O SITE PAGA</small><br><b>3.10</b>
                </div>
                <div class="box-preco" style='width:45%;'>
                    <small style='font-size:10px;'>O REI DIZ</small><br><b style='color:#00FF41;'>2.10</b>
                </div>
            </div>
        </div>
    """, unsafe_allow_html=True)

st.sidebar.title("Ajustes do Rei")
st.sidebar.write("Aqui você controla a inteligência do robô.")
if st.sidebar.button("📲 Testar Alerta Telegram"):
    st.sidebar.success("Sinal de teste enviado!")
