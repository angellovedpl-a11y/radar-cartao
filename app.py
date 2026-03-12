import streamlit as st

# 1. Configuração e Estilo (Visual Sniper)
st.set_page_config(page_title="Rei dos Cartões", layout="wide")

st.markdown("""
    <style>
    body { background-color: #050505; color: #00FF41; font-family: 'JetBrains Mono', monospace; }
    .stApp { background-color: #050505; }
    .card-principal { background: #111; border: 1px solid #333; padding: 20px; border-radius: 15px; margin-bottom: 20px; border-left: 5px solid #FFD700; }
    .card-jogador { background: #0a0a0a; border: 1px solid #222; padding: 15px; border-radius: 10px; border-top: 3px solid #FFD700; }
    .odd-box { background: #1a1a1a; padding: 10px; border-radius: 8px; text-align: center; border: 1px solid #444; }
    .label { color: #888; font-size: 11px; text-transform: uppercase; }
    </style>
    """, unsafe_allow_html=True)

# 2. Sistema de Abas (Operação vs Cadastro)
aba1, aba2 = st.tabs(["🎯 RADAR DE ODDS", "⚙️ ADMINISTRADOR"])

with aba2:
    st.subheader("Cadastrar Oportunidade do Dia")
    with st.form("cadastro_jogo"):
        jogo_nome = st.text_input("Partida (Ex: Vasco x Fla)")
        mercado_jogo = st.text_input("Mercado Jogo (Ex: Over 5.5)")
        odd_site_jogo = st.number_input("Odd Site Jogo", value=2.50)
        odd_rei_jogo = st.number_input("Odd Rei Jogo", value=2.00)
        
        st.divider()
        jogador_nome = st.text_input("Jogador Alvo")
        odd_site_player = st.number_input("Odd Site Jogador", value=4.50)
        odd_rei_player = st.number_input("Odd Rei Jogador", value=2.50)
        
        btn_salvar = st.form_submit_button("PUBLICAR NO DASHBOARD")
        if btn_salvar:
            st.session_state['dados_viva'] = {
                "jogo": jogo_nome, "mercado": mercado_jogo, "osj": odd_site_jogo, "orj": odd_rei_jogo,
                "player": jogador_nome, "osp": odd_site_player, "orp": odd_rei_player
            }

# 3. Dashboard de Operação
with aba1:
    dados = st.session_state.get('dados_viva', {
        "jogo": "VASCO vs FLAMENGO", "mercado": "Over 5.5 Cartões", "osj": 2.62, "orj": 2.10,
        "player": "MEDEL (Vasco)", "osp": 4.33, "orp": 2.20
    })

    st.markdown(f"""
        <div class="card-principal">
            <div style='display: flex; justify-content: space-between;'>
                <h2 style='margin:0; color:white;'>{dados['jogo']}</h2>
                <span style='color:#00FF41; font-weight:bold;'>VALOR DETECTADO</span>
            </div>
            <p style='color:#888;'>Mercado: {dados['mercado']}</p>
            <div style='display: flex; gap: 20px; margin-top:15px;'>
                <div class="odd-box"> <span class="label">SITE PAGA</span><br><b style='font-size: 22px; color: #FF4B4B;'>{dados['osj']:.2f}</b> </div>
                <div class="odd-box"> <span class="label">REI DIZ</span><br><b style='font-size: 22px; color: #00FF41;'>{dados['orj']:.2f}</b> </div>
            </div>
        </div>
    """, unsafe_allow_html=True)

    col1, col2 = st.columns(2)
    with col1:
        st.markdown(f"""
            <div class="card-jogador">
                <h4 style='margin:0; color:#FFD700;'>{dados['player']}</h4>
                <div style='display: flex; justify-content: space-between; margin-top:15px;'>
                    <div class="odd-box" style='width:45%;'> <small class="label">SITE PAGA</small><br><b>{dados['osp']:.2f}</b> </div>
                    <div class="odd-box" style='width:45%;'> <small class="label">REI DIZ</small><br><b style='color:#00FF41;'>{dados['orp']:.2f}</b> </div>
                </div>
            </div>
        """, unsafe_allow_html=True)

st.sidebar.title("REI DOS CARTÕES")
if st.sidebar.button("📲 NOTIFICAR TELEGRAM"):
    st.sidebar.success("Sinal enviado!")
