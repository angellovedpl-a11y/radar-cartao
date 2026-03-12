import streamlit as st
import pandas as pd
import plotly.express as px

# Configuração da página
st.set_page_config(page_title="THE CARD KING PRO", layout="wide", initial_sidebar_state="collapsed")

# CSS Avançado para imitar o estilo v0.dev / Bloomberg
st.markdown("""
    <style>
    /* Fundo principal */
    .stApp { background-color: #050505; color: #E0E0E0; }
    
    /* Estilo dos Cards */
    .metric-card {
        background-color: #111111;
        border: 1px solid #333333;
        padding: 20px;
        border-radius: 12px;
        box-shadow: 0 4px 6px rgba(0, 0, 0, 0.3);
        margin-bottom: 10px;
    }
    
    /* Títulos e textos */
    h1, h2, h3 { color: #FFFFFF !important; font-family: 'Inter', sans-serif; font-weight: 700; }
    
    /* Botão customizado */
    .stButton>button {
        background: linear-gradient(90deg, #FF4B4B 0%, #8B0000 100%);
        color: white; border: none; border-radius: 8px; font-weight: bold; transition: 0.3s;
    }
    .stButton>button:hover { transform: scale(1.02); box-shadow: 0 0 15px rgba(255, 75, 75, 0.4); }
    </style>
    """, unsafe_allow_html=True)

st.title("👑 THE CARD KING PRO")
st.markdown("<p style='color: #888;'>Painel de Inteligência em Arbitragem</p>", unsafe_allow_html=True)

# Dados (Ainda simulados, preparando para o Scraping)
df = pd.DataFrame({
    'Árbitro': ['R. Claus', 'W. Sampaio', 'A. Daronco', 'F. Rodrigues', 'B. Machado'],
    'Média': [5.2, 6.1, 4.8, 5.5, 6.3],
    'Tendência': ['Alta', 'Crítica', 'Média', 'Alta', 'Crítica']
})

# Layout em colunas
col1, col2 = st.columns([1, 1.5])

with col1:
    st.markdown("### 🔍 Radar de Escala")
    selecao = st.selectbox("Selecione o Juiz", df['Árbitro'])
    dado = df[df['Árbitro'] == selecao].iloc[0]
    
    # Card de Média Estilizado
    st.markdown(f"""
        <div class="metric-card">
            <p style='color: #888; margin: 0;'>Média de Cartões</p>
            <h1 style='color: #FF4B4B; margin: 0;'>{dado['Média']}</h1>
            <p style='color: {"#FF4B4B" if dado['Tendência'] == "Crítica" else "#FFA500"};'>Tendência {dado['Tendência']}</p>
        </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("### 📊 Performance nos Últimos Jogos")
    # Gráfico Plotly (Estilo Profissional)
    fig = px.bar(df, x='Árbitro', y='Média', color='Média', 
                 color_continuous_scale=['#333', '#FF4B4B'],
                 template='plotly_dark')
    fig.update_layout(plot_bgcolor='rgba(0,0,0,0)', paper_bgcolor='rgba(0,0,0,0)', showlegend=False)
    st.plotly_chart(fig, use_container_width=True)

st.divider()

# Veredito
st.markdown("### 🚀 Veredito do King")
if dado['Média'] > 5.5:
    st.warning(f"O Juiz {selecao} é rigoroso. O mercado de **Over 4.5 Amarelos** tem valor aqui.")
else:
    st.info(f"O Juiz {selecao} costuma controlar bem o jogo. Evite mercados de cartões altos.")

st.caption("Engine v2.5 - Design System v0-Alpha")
