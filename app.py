import streamlit as st

# 1. Setup de Página
st.set_page_config(page_title="Rei dos Cartões | VIP", layout="wide", initial_sidebar_state="collapsed")

# 2. Estilos CSS (Visual Sniper + Animação de Porcentagem)
st.markdown("""
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
        margin-bottom: 5px;
    }
    .badge-v { background: #00FF41; color: black; padding: 2px 8px; border-radius: 4px; font-size: 10px; font-weight: bold; }
    .prob-badge { background: rgba(0, 255, 65, 0.1); color: #00FF41; border: 1px solid #00FF41; padding: 2px 6px; border-radius: 4px; font-size: 12px; font-weight: bold; }
    .odd-box { background: #1a1a1a; padding: 10px; border-radius: 8px; text-align: center; border: 1px solid #333; width: 48%; }
    .odd-num { font-family: 'Orbitron', sans-serif; font-size: 18px; color: #00FF41; }
    .label-m { color: #888; font-size: 10px; text-transform: uppercase; letter-spacing: 1px; }
    .over-under-row { display: flex; justify-content: space-between; margin-top: 10px; padding: 8px 10px; background: #0c0c0c; border-radius: 5px; border: 1px solid #222; }
    .target-box { 
        background: linear-gradient(90deg, #1a1a1a 0%, #222 100%); 
        padding:15px; border-radius:8px; margin-top:15px; 
        display:flex; justify-content:space-between; align-items:center; 
        border: 1px solid #FFD70066;
    }
</style>
""", unsafe_allow_html=True)

st.markdown("<h1 style='text-align: center; color: #FFD700;'>👑 REI DOS CARTÕES</h1>", unsafe_allow_html=True)

# 3. Função de Renderização com Porcentagem de Chance
def render_card(t, j, v, os, orj, ov, un, p, po, prob, idx):
    card_html = f"""
    <div class="card-vip">
        <div style="display: flex; justify-content: space-between; align-items: center;">
            <span style="color:red; font-weight:bold; font-size:10px;">● AO VIVO</span>
            <span class="badge-v">{v} DE VALOR</span>
        </div>
        <h3 style="margin: 10px 0 0 0; color:white;">{t}</h3>
        <p style="color:#666; font-size:12px; margin-bottom: 15px;">👤 Juiz: {j}</p>
        
        <div style="display: flex; justify-content: space-between;">
            <div class="odd-box">
                <span class="label-m">Site pagando</span><br>
                <span class="odd-num" style="color:#FF4B4B;">{os}</span>
            </div>
            <div class="odd-box">
                <span class="label-m">Preço Justo</span><br>
                <span class="odd-num">{orj}</span>
            </div>
        </div>

        <div class="over-under-row">
            <div><span class="label-m">Over 4.5:</span> <b style="font-family:Orbitron; font-size:13px; color:#00FF41;">{ov}</b></div>
            <div><span class="label-m">Under 4.5:</span> <b style="font-family:Orbitron; font-size:13px; color:#FF4B4B;">{un}</b></div>
        </div>

        <div class="target-box">
            <div>
                <span class="label-m" style="color:#FFD700;">🔥 PAPA CARTÃO</span> 
                <span class="prob-badge">{prob}% CHANCE</span><br>
                <b style="color:white; font-size:18px;">{p}</b>
            </div>
            <div style="text-align:right;">
                <span class="label-m">PAGAMENTO</span><br>
                <b style="font-family:Orbitron; font-size:20px; color:#FFD700;">{po}</b>
            </div>
        </div>
    </div>
    """
    st.markdown(card_html, unsafe_allow_html=True)
    
    texto_sinal = f"🚨 SINAL DO REI: {t} | PAPA CARTÃO: {p} ({prob}% de chance) na odd {po}!"
    st.text_input("Copiar Sinal:", value=texto_sinal, key=f"input_{idx}", label_visibility="collapsed")

# 4. Grid de Oportunidades (Dados com Porcentagem Real)
c1, c2 = st.columns(2)

with c1:
    # render_card(Time, Juiz, Valor, OddSite, OddRei, Over, Under, Jogador, OddProp, Porcentagem, ID)
    render_card("VASCO x FLAMENGO", "Raphael Claus", "22%", "2.62", "2.10", "1.85", "1.95", "MEDEL", "4.33", "88", 1)
    render_card("CRUZEIRO x ATLETICO-MG", "W. Sampaio", "25%", "2.30", "1.90", "1.72", "2.10", "HULK", "3.80", "74", 2)

with c2:
    render_card("PALMEIRAS x SPFC", "A. Daronco", "18%", "1.95", "1.70", "1.65", "2.25", "LUCIANO", "3.50", "81", 3)
    render_card("GREMIO x INTER", "F. Rodrigues", "30%", "2.85", "2.15", "1.90", "1.80", "KANNEMANN", "2.90", "92", 4)

# Sidebar
with st.sidebar:
    st.header("⚙️ CONFIG")
    st.button("🔄 ATUALIZAR RADAR", use_container_width=True)
