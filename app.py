import streamlit as st

# 1. Setup de Interface "Black-Gold"
st.set_page_config(page_title="Rei dos Cartões | VIP", layout="wide")

st.markdown("""
    <style>
    body { background-color: #050505; color: white; font-family: 'Inter', sans-serif; }
    .stApp { background-color: #050505; }
    
    /* Grid de Jogos */
    .game-grid { display: grid; grid-template-columns: repeat(auto-fit, minmax(300px, 1fr)); gap: 15px; }
    
    /* Card de Jogo Quente */
    .card-hot {
        background: linear-gradient(145deg, #1a1a1a, #000);
        border: 1px solid #333;
        border-top: 4px solid #FFD700;
        padding: 15px;
        border-radius: 12px;
        position: relative;
    }
    
    .badge-live { background: #FF0000; color: white; padding: 2px 8px; border-radius: 4px; font-size: 10px; font-weight: bold; }
    .badge-value { background: #00FF41; color: black; padding: 2px 8px; border-radius: 4px; font-size: 10px; font-weight: bold; }
    
    .odd-mini { background: #222; border: 1px solid #444; padding: 5px; border-radius: 6px; text-align: center; width: 48%; }
    .player-name { color: #FFD700; font-weight: bold; font-size: 16px; margin: 5px 0; }
    .label { color: #888; font-size: 10px; text-transform: uppercase; }
    </style>
    """, unsafe_allow_html=True)

st.title("👑 REI DOS CARTÕES | SCANNER PRO")
st.markdown("#### 📡 Radar de Valor - Sinais em Tempo Real")

# --- DATABASE SIMULADA DE VOLUME (Para não ficar vazio) ---
jogos = [
    {"time": "VASCO x FLAMENGO", "juiz": "R. Claus", "v": "+22%", "o_site": 2.50, "o_rei": 2.05, "p": "MEDEL", "p_odd": 4.33},
    {"time": "PALMEIRAS x SPFC", "juiz": "Daronco", "v": "+18%", "o_site": 1.90, "o_rei": 1.65, "p": "LUCIANO", "p_odd": 3.40},
    {"time": "CRUZEIRO x GALO", "juiz": "W. Sampaio", "v": "+15%", "o_site": 2.15, "o_rei": 1.85, "p": "HULK", "p_odd": 3.75},
    {"time": "GRÊMIO x INTER", "juiz": "F. Rodrigues", "v": "+30%", "o_site": 2.80, "o_rei": 2.10, "p": "KANNEMANN", "p_odd": 2.90},
]

# --- GRID DE EXIBIÇÃO ---
col1, col2 = st.columns(2)

for i, jogo in enumerate(jogos):
    with col1 if i % 2 == 0 else col2:
        st.markdown(f"""
            <div class="card-hot">
                <div style='display: flex; justify-content: space-between;'>
                    <span class="badge-live">● LIVE</span>
                    <span class="badge-value">{jogo['v']} VALUE</span>
                </div>
                <h3 style='margin:10px 0 0 0; color:white;'>{jogo['time']}</h3>
                <p style='color:#666; font-size:12px;'>Árbitro: {jogo['juiz']}</p>
                
                <div style='display: flex; justify-content: space-between; margin-top:10px;'>
                    <div class="odd-mini">
                        <span class="label">Over 5.5 (Site)</span><br>
                        <b style='color:#FF4B4B;'>{jogo['o_site']:.2f}</b>
                    </div>
                    <div class="odd-mini">
                        <span class="label">Over 5.5 (Rei)</span><br>
                        <b style='color:#00FF41;'>{jogo['o_rei']:.2f}</b>
                    </div>
                </div>
                
                <hr style='border: 0.1px solid #222; margin: 15px 0;'>
                
                <div style='display: flex; justify-content: space-between; align-items: center;'>
                    <div>
                        <span class="label">Destaque Jogador</span><br>
                        <span class="player-name">{jogo['p']}</span>
                    </div>
                    <div class="odd-mini" style="width: 30%;">
                        <span class="label">Odd Cartão</span><br>
                        <b style='color:#FFD700;'>{jogo['p_odd']:.2f}</b>
                    </div>
                </div>
            </div>
        """, unsafe_allow_html=True)

st.sidebar.title("MENU VIP")
st.sidebar.checkbox("Filtrar apenas +20% Value", value=True)
st.sidebar.checkbox("Alertas Sonoros", value=True)
if st.sidebar.button("📲 DISPARAR TODOS OS SINAIS"):
    st.sidebar.success("Canal do Telegram Atualizado!")

st.divider()
st.markdown("#### 📑 Histórico de Greens Recentes")
# Tabela de prova social rápida
hist_data = {"Partida": ["Corinthians x Santos", "Bahia x Vitória"], "Mercado": ["Fagner (Cartão)", "Over 6.5"], "Odd": [3.20, 2.45], "Status": ["✅ GREEN", "✅ GREEN"]}
st.table(hist_data)
