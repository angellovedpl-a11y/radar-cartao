import streamlit as st

# 1. Configuração e Estilos fixos (dentro do head do app)
st.set_page_config(page_title="Rei dos Cartões | PRO", layout="wide")

st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Orbitron:wght@400;700&display=swap');
    
    .stApp { background-color: #050505; }
    
    .card-hot {
        background: #111;
        border: 1px solid #333;
        border-top: 4px solid #FFD700;
        padding: 20px;
        border-radius: 15px;
        margin-bottom: 20px;
    }
    
    .label-mini { color: #888; font-size: 10px; text-transform: uppercase; letter-spacing: 1px; }
    .odd-val { font-family: 'Orbitron', sans-serif; font-size: 20px; font-weight: bold; }
    .badge-v { background: #00FF41; color: black; padding: 2px 8px; border-radius: 4px; font-size: 10px; font-weight: bold; }
    </style>
    """, unsafe_allow_html=True)

st.title("👑 REI DOS CARTÕES | SCANNER PRO")

# 2. Grid de Jogos corrigido
col1, col2 = st.columns(2)

# Exemplo de como renderizar SEM aparecer o código na tela:
with col1:
    st.markdown("""
        <div class="card-hot">
            <div style='display: flex; justify-content: space-between;'>
                <span style='background:red; color:white; padding:2px 6px; border-radius:4px; font-size:10px;'>● LIVE</span>
                <span class="badge-v">+22% VALUE</span>
            </div>
            
            <h3 style='color:white; margin: 15px 0 5px 0;'>VASCO x FLAMENGO</h3>
            <p style='color:#555; font-size:12px;'>Árbitro: Raphael Claus</p>
            
            <div style='display: flex; justify-content: space-between; margin-top:20px;'>
                <div style='background:#1a1a1a; padding:10px; border-radius:8px; width:48%; text-align:center; border:1px solid #333;'>
                    <span class="label-mini">Odd Site</span><br>
                    <span class="odd-val" style="color:#FF4B4B;">2.50</span>
                </div>
                <div style='background:#1a1a1a; padding:10px; border-radius:8px; width:48%; text-align:center; border:1px solid #333;'>
                    <span class="label-mini">Odd Rei</span><br>
                    <span class="odd-val" style="color:#00FF41;">2.05</span>
                </div>
            </div>
            
            <hr style='border:0.1px solid #222; margin:20px 0;'>
            
            <div style='display: flex; justify-content: space-between; align-items:center;'>
                <div>
                    <span class="label-mini">Alvo de Cartão</span><br>
                    <b style='color:#FFD700; font-size:18px;'>MEDEL</b>
                </div>
                <div style='background:#222; padding:5px 15px; border-radius:5px;'>
                    <span class="odd-val" style="font-size:16px;">4.33</span>
                </div>
            </div>
        </div>
    """, unsafe_allow_html=True)

with col2:
    # Repita a mesma estrutura para o segundo card...
    st.markdown("""<div class="card-hot"><h3 style='color:white;'>PALMEIRAS x SPFC</h3>...</div>""", unsafe_allow_html=True)

# 3. Sidebar (Menu Lateral)
with st.sidebar:
    st.image("https://img.icons8.com/ios-filled/100/FFD700/crown.png", width=80)
    st.header("MENU VIP")
    st.checkbox("Filtrar +20% Value", value=True)
    st.button("🚀 DISPARAR SINAIS", use_container_width=True)
