import streamlit as st

# 1. Setup de Interface (Fonte Orbitron para Odds e Inter para Textos)
st.set_page_config(page_title="Rei dos Cartões | VIP", layout="wide", initial_sidebar_state="collapsed")

st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Orbitron:wght@400;700&family=Inter:wght@400;700&display=swap');
    
    .stApp { background-color: #050505; font-family: 'Inter', sans-serif; }
    
    /* Grid de Oportunidades */
    .grid-container {
        display: grid;
        grid-template-columns: repeat(auto-fit, minmax(350px, 1fr));
        gap: 20px;
        padding: 10px;
    }
    
    .card-vip {
        background: linear-gradient(145deg, #111 0%, #050505 100%);
        border: 1px solid #333;
        border-top: 4px solid #FFD700;
        border-radius: 15px;
        padding: 20px;
        transition: 0.3s;
    }
    .card-vip:hover { border-color: #FFD700; transform: translateY(-5px); }
    
    .badge-live { background: #FF0000; color: white; padding: 3px 8px; border-radius: 4px; font-size: 10px; font-weight: bold; animation: pulse 2s infinite; }
    .badge-value { background: #00FF41; color: black; padding: 3px 8px; border-radius: 4px; font-size: 10px; font-weight: bold; }
    
    .odd-box {
        background: #1a1a1a;
        border: 1px solid #333;
        padding: 12px;
        border-radius: 10px;
        text-align: center;
        width: 48%;
    }
    
    .odd-num { font-family: 'Orbitron', sans-serif; font-size: 22px; font-weight: bold; }
    .label-mini { color: #666; font-size: 10px; text-transform: uppercase; letter-spacing: 1px; }
    
    @keyframes pulse {
        0% { opacity: 1; }
        50% { opacity: 0.5; }
        100% { opacity: 1; }
    }
    </style>
    """, unsafe_allow_html=True)

st.markdown("<h1 style='text-align: center; color: #FFD700;'>👑 REI DOS CARTÕES <span style='color:white; font-size:20px;'>| SCANNER PRO</span></h1>", unsafe_allow_html=True)

# 2. Dados dos Jogos (Simulando o Scanner Real)
jogos_hoje = [
    {"time": "VASCO x FLAMENGO", "juiz": "Raphael Claus", "v": "+22%", "os": "2.62", "or": "2.10", "p": "MEDEL", "po": "4.33"},
    {"time": "PALMEIRAS x SPFC", "juiz": "A. Daronco", "v": "+18%", "os": "1.95", "or": "1.70", "p": "LUCIANO", "po": "3.50"},
    {"time": "CRUZEIRO x ATLETICO-MG", "juiz": "W. Sampaio", "v": "+25%", "os": "2.30", "or": "1.90", "p": "HULK", "po": "3.80"},
    {"time": "GREMIO x INTER", "juiz": "F. Rodrigues", "v": "+30%", "os": "2.85", "or": "2.15", "p": "KANNEMANN", "po": "2.90"},
    {"time": "CORINTHIANS x SANTOS", "juiz": "Edina Alves", "v": "+15%", "os": "2.10", "or": "1.85", "p": "FAGNER", "po": "3.20"},
    {"time": "BAHIA x VITORIA", "juiz": "Braulio Machado", "v": "+28%", "os": "2.55", "or": "2.05", "p": "BAIXOLA", "po": "4.10"}
]

# 3. Renderização dos Cards (Usando colunas para o Grid)
col1, col2 = st.columns(2)

for i, j in enumerate(jogos_hoje):
    alvo_col = col1 if i % 2 == 0 else col2
    with alvo_col:
        st.markdown(f"""
            <div class="card-vip">
                <div style='display: flex; justify-content: space-between;'>
                    <span class="badge-live">● LIVE</span>
                    <span class="badge-value">{j['v']} VALUE</span>
                </div>
                
                <h3 style='color:white; margin: 15px 0 5px 0;'>{j['time']}</h3>
                <p style='color:#555; font-size:12px;'>Árbitro: <b>{j['juiz']}</b></p>
                
                <div style='display: flex; justify-content: space-between; margin-top:20px;'>
                    <div class="odd-box">
                        <span class="label-mini">Odd Site</span><br>
                        <span class="odd-num" style="color:#FF4B4B;">{j['os']}</span>
                    </div>
                    <div class="odd-box">
                        <span class="label-mini">Odd Rei</span><br>
                        <span class="odd-num" style="color:#00FF41;">{j['or']}</span>
                    </div>
                </div>
                
                <div style='background:#111; padding:15px; border-radius:10px; margin-top:15px; border:1px solid #222; display:flex; justify-content:space-between; align-items:center;'>
                    <div>
                        <span class="label-mini">Alvo de Cartão</span><br>
                        <b style='color:#FFD700; font-size:18px;'>{j['p']}</b>
                    </div>
                    <div style='text-align:right;'>
                        <span class="label-mini">Odd Prop</span><br>
                        <span class="odd-num" style="font-size:18px;">{j['po']}</span>
                    </div>
                </div>
            </div>
        """, unsafe_allow_html=True)
        st.button(f"📲 Notificar {j['p']}", key=f"btn_{i}", use_container_width=True)

# Sidebar
with st.sidebar:
    st.markdown("### 🛠️ FILTROS")
    st.slider("Mínimo Value (%)", 5, 50, 20)
    st.button("🚀 ATUALIZAR SCANNER", use_container_width=True)
