import streamlit as st

# 1. Configuração de Página
st.set_page_config(page_title="Rei dos Cartões | PRO", layout="wide", initial_sidebar_state="collapsed")

# 2. Estilos CSS (Visual Sniper)
estilo = """
<style>
    @import url('https://fonts.googleapis.com/css2?family=Orbitron:wght@400;700&family=Inter:wght@400;700&display=swap');
    body { background-color: #050505; color: white; font-family: 'Inter', sans-serif; }
    .stApp { background-color: #050505; }
    .card-vip {
        background: #111;
        border: 1px solid #333;
        border-top: 4px solid #FFD700;
        border-radius: 12px;
        padding: 20px;
        margin-bottom: 15px;
    }
    .badge-v { background: #00FF41; color: black; padding: 2px 8px; border-radius: 4px; font-size: 10px; font-weight: bold; }
    .odd-box { background: #1a1a1a; padding: 10px; border-radius: 8px; text-align: center; border: 1px solid #333; width: 48%; }
    .odd-num { font-family: 'Orbitron', sans-serif; font-size: 18px; color: #00FF41; }
    .label-m { color: #666; font-size: 10px; text-transform: uppercase; letter-spacing: 1px; }
    .over-under-row { display: flex; justify-content: space-between; margin-top: 10px; padding: 5px 10px; background: #0c0c0c; border-radius: 5px; border: 1px solid #222; }
</style>
"""
st.markdown(estilo, unsafe_allow_html=True)

st.markdown("<h1 style='text-align: center; color: #FFD700;'>👑 REI DOS CARTÕES</h1>", unsafe_allow_html=True)

# 3. Função para desenhar o Card (Com Over/Under integrado)
def criar_card(time, juiz, valor, odd_s, odd_r, over_val, under_val, jogador, odd_p):
    html_card = f"""
    <div class="card-vip">
        <div style="display: flex; justify-content: space-between;">
            <span style="color:red; font-weight:bold; font-size:10px;">● AO VIVO</span>
            <span class="badge-v">{valor} VALUE</span>
        </div>
        <h3 style="margin: 10px 0 0 0; color:white;">{time}</h3>
        <p style="color:#555; font-size:12px; margin-bottom: 15px;">Árbitro: {juiz}</p>
        
        <div style="display: flex; justify-content: space-between;">
            <div class="odd-box">
                <span class="label-m">Site Paga (O 5.5)</span><br>
                <span class="odd-num" style="color:#FF4B4B;">{odd_s}</span>
            </div>
            <div class="odd-box">
                <span class="label-m">Preço Rei</span><br>
                <span class="odd-num">{odd_r}</span>
            </div>
        </div>

        <div class="over-under-row">
            <div><span class="label-m">Over 4.5:</span> <b style="font-family:Orbitron; font-size:14px; color:#00FF41;">{over_val}</b></div>
            <div><span class="label-m">Under 4.5:</span> <b style="font-family:Orbitron; font-size:14px; color:#FF4B4B;">{under_val}</b></div>
        </div>

        <div style="background:#0a0a0a; padding:12px; border-radius:8px; margin-top:15px; display:flex; justify-content:space-between; align-items:center; border: 1px solid #222;">
            <div><span class="label-m">Alvo Cartão</span><br><b style="color:#FFD700; font-size:16px;">{jogador}</b></div>
            <div style="text-align:right;"><span class="label-m">Odd Prop</span><br><b style="font-family:Orbitron; font-size:18px; color:white;">{odd_p}</b></div>
        </div>
    </div>
    """
    return st.markdown(html_card, unsafe_allow_html=True)

# 4. Grid de Oportunidades (Dados atualizados)
col1, col2 = st.columns(2)

with col1:
    criar_card("VASCO x FLAMENGO", "Raphael Claus", "+22%", "2.62", "2.10", "1.85", "1.95", "MEDEL", "4.33")
    criar_card("CRUZEIRO x ATLETICO-MG", "W. Sampaio", "+25%", "2.30", "1.90", "1.72", "2.10", "HULK", "3.80")

with col2:
    criar_card("PALMEIRAS x SPFC", "A. Daronco", "+18%", "1.95", "1.70", "1.65", "2.25", "LUCIANO", "3.50")
    criar_card("GREMIO x INTER", "F. Rodrigues", "+30%", "2.85", "2.15", "1.90", "1.80", "KANNEMANN", "2.90")

# Sidebar
with st.sidebar:
    st.header("⚙️ FILTROS")
    st.button("🔄 ATUALIZAR RADAR", use_container_width=True)
