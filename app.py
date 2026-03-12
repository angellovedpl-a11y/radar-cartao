import streamlit as st
import pandas as pd

# Interface Profissional de Sinais
st.set_page_config(page_title="Rei dos Cartões - Scanner", layout="wide")

st.markdown("""
    <style>
    body { background-color: #000; color: #fff; }
    .card-oportunidade {
        background: linear-gradient(145deg, #1a1a1a 0%, #0a0a0a 100%);
        border: 1px solid #333;
        padding: 20px;
        border-radius: 15px;
        margin-bottom: 20px;
    }
    .badge-valor {
        background-color: #00FF41; color: black;
        padding: 4px 12px; border-radius: 5px; font-weight: bold; font-size: 14px;
    }
    .odd-box {
        background: #222; padding: 10px; border-radius: 8px; text-align: center; border: 1px solid #444;
    }
    </style>
    """, unsafe_allow_html=True)

st.title("🎯 REI DOS CARTÕES - SCANNER EV+")

# --- SEÇÃO 1: OPORTUNIDADE DO JOGO ---
st.markdown("### 🏟️ Mercado: Over Geral")
col1, col2 = st.columns([2, 1])

with col1:
    st.markdown("""
        <div class="card-oportunidade">
            <div style='display: flex; justify-content: space-between;'>
                <h4>VASCO vs FLAMENGO</h4>
                <span class="badge-valor">+22% DE VALOR</span>
            </div>
            <p style='color:#888; font-size:14px;'>Juiz: Raphael Claus | Média: 6.2 | Clima: Clássico Quente</p>
            <div style='display: flex; gap: 15px; margin-top:10px;'>
                <div class="odd-box"> <small>ODD CASA</small><br><b style='color:#FF4B4B;'>2.10</b> </div>
                <div class="odd-box"> <small>ODD REI</small><br><b style='color:#00FF41;'>1.72</b> </div>
            </div>
        </div>
    """, unsafe_allow_html=True)

# --- SEÇÃO 2: OPORTUNIDADE DE JOGADOR (O QUE VOCÊ PEDIU) ---
st.markdown("### 👤 Mercado: Cartão para Jogador")
col3, col4 = st.columns(2)

# Simulação de Oportunidade 1
with col3:
    st.markdown("""
        <div class="card-oportunidade" style="border-left: 4px solid #FFD700;">
            <div style='display: flex; justify-content: space-between;'>
                <h5 style='margin:0;'>MEDEL (Vasco)</h5>
                <span style='color:#FFD700; font-weight:bold;'>TOP PICK</span>
            </div>
            <p style='color:#888; font-size:12px;'>Motivo: Marcação individual em Pedro + Reclamação</p>
            <div style='display: flex; justify-content: space-between; align-items: center; margin-top:10px;'>
                <div class="odd-box"> <small>ODD CASA</small><br><b>3.40</b> </div>
                <div style='text-align:right;'>
                    <span style='color:#00FF41; font-size:18px; font-weight:bold;'>VALOR: High</span><br>
                    <small>Prob. Real: 42%</small>
                </div>
            </div>
        </div>
    """, unsafe_allow_html=True)

# Simulação de Oportunidade 2
with col4:
    st.markdown("""
        <div class="card-oportunidade" style="border-left: 4px solid #FFD700;">
            <div style='display: flex; justify-content: space-between;'>
                <h5 style='margin:0;'>F. MELO (Fluminense)</h5>
                <span style='color:#FFD700; font-weight:bold;'>TOP PICK</span>
            </div>
            <p style='color:#888; font-size:12px;'>Motivo: Histórico em Derbys + Árbitro Rigoroso</p>
            <div style='display: flex; justify-content: space-between; align-items: center; margin-top:10px;'>
                <div class="odd-box"> <small>ODD CASA</small><br><b>2.85</b> </div>
                <div style='text-align:right;'>
                    <span style='color:#00FF41; font-size:18px; font-weight:bold;'>VALOR: Medium</span><br>
                    <small>Prob. Real: 38%</small>
                </div>
            </div>
        </div>
    """, unsafe_allow_html=True)

st.sidebar.title("🛠️ Configurar Filtros")
fator_jogador = st.sidebar.slider("Peso do Histórico do Jogador", 1.0, 5.0, 3.5)
if st.sidebar.button("📲 Notificar Oportunidade via Telegram"):
    st.sidebar.success("Alerta enviado!")
