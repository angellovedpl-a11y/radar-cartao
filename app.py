import streamlit as st
import streamlit.components.v1 as components

# 1. Configuração de Página
st.set_page_config(page_title="Rei dos Cartões | VIP", layout="wide", initial_sidebar_state="collapsed")

# 2. Estilos CSS e Estrutura do Card (Tudo em uma variável limpa)
def gerar_html_card(t, j, v, os, orj, ov, un, p, po, prob):
    return f"""
    <div style="background: #111; border: 1px solid #333; border-top: 4px solid #FFD700; border-radius: 12px; padding: 20px; font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif; color: white; margin-bottom: 10px;">
        <div style="display: flex; justify-content: space-between; align-items: center;">
            <span style="color:red; font-weight:bold; font-size:10px;">● AO VIVO</span>
            <span style="background: #00FF41; color: black; padding: 2px 8px; border-radius: 4px; font-size: 10px; font-weight: bold;">{v} DE VALOR</span>
        </div>
        <h3 style="margin: 15px 0 5px 0; color:white; font-size: 22px;">{t}</h3>
        <p style="color:#666; font-size:12px; margin: 0 0 15px 0;">👤 Juiz: {j}</p>
        
        <div style="display: flex; justify-content: space-between;">
            <div style="background: #1a1a1a; padding: 10px; border-radius: 8px; text-align: center; border: 1px solid #333; width: 45%;">
                <span style="color: #888; font-size: 10px; text-transform: uppercase;">Site pagando</span><br>
                <span style="font-size: 18px; color: #FF4B4B; font-weight: bold;">{os}</span>
            </div>
            <div style="background: #1a1a1a; padding: 10px; border-radius: 8px; text-align: center; border: 1px solid #333; width: 45%;">
                <span style="color: #888; font-size: 10px; text-transform: uppercase;">Preço Justo</span><br>
                <span style="font-size: 18px; color: #00FF41; font-weight: bold;">{orj}</span>
            </div>
        </div>

        <div style="display: flex; justify-content: space-between; margin-top: 10px; padding: 8px 10px; background: #0c0c0c; border-radius: 5px; border: 1px solid #222;">
            <div style="font-size: 12px;"><span style="color: #666; text-transform: uppercase;">Over 4.5:</span> <b style="color:#00FF41;">{ov}</b></div>
            <div style="font-size: 12px;"><span style="color: #666; text-transform: uppercase;">Under 4.5:</span> <b style="color:#FF4B4B;">{un}</b></div>
        </div>

        <div style="background: linear-gradient(90deg, #1a1a1a 0%, #222 100%); padding:15px; border-radius:8px; margin-top:15px; display:flex; justify-content:space-between; align-items:center; border: 1px solid #FFD70066;">
            <div>
                <span style="color: #FFD700; font-size: 10px; text-transform: uppercase; font-weight: bold;">🔥 PAPA CARTÃO</span> 
                <span style="background: rgba(0, 255, 65, 0.1); color: #00FF41; border: 1px solid #00FF41; padding: 2px 6px; border-radius: 4px; font-size: 11px; font-weight: bold;">{prob}% CHANCE</span><br>
                <b style="color:white; font-size:18px;">{p}</b>
            </div>
            <div style="text-align:right;">
                <span style="color: #888; font-size: 10px; text-transform: uppercase;">PAGAMENTO</span><br>
                <b style="font-size:20px; color:#FFD700;">{po}</b>
            </div>
        </div>
    </div>
    """

st.markdown("<h1 style='text-align: center; color: #FFD700; font-family: sans-serif;'>👑 REI DOS CARTÕES</h1>", unsafe_allow_html=True)

# 4. Grid de Oportunidades
c1, c2 = st.columns(2)

# Lista de dados para facilitar
jogos = [
    ["VASCO x FLAMENGO", "Raphael Claus", "22%", "2.62", "2.10", "1.85", "1.95", "MEDEL", "4.33", "88"],
    ["PALMEIRAS x SPFC", "A. Daronco", "18%", "1.95", "1.70", "1.65", "2.25", "LUCIANO", "3.50", "81"],
    ["CRUZEIRO x ATLETICO-MG", "W. Sampaio", "25%", "2.30", "1.90", "1.72", "2.10", "HULK", "3.80", "74"],
    ["GREMIO x INTER", "F. Rodrigues", "30%", "2.85", "2.15", "1.90", "1.80", "KANNEMANN", "2.90", "92"]
]

for i, dado in enumerate(jogos):
    col = c1 if i % 2 == 0 else c2
    with col:
        html = gerar_html_card(*dado)
        components.html(html, height=350) # Aqui está a blindagem!
        st.button(f"📲 Copiar Sinal: {dado[7]}", key=f"btn_{i}", use_container_width=True)

st.sidebar.button("🔄 ATUALIZAR RADAR", use_container_width=True)
