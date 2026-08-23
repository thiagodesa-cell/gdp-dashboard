import streamlit as st
import streamlit.components.v1 as components

# Configuração da página
st.set_page_config(
    page_title="StreamFinder - Assistir Filmes",
    page_icon="🍿",
    layout="wide"
)

# Estilização visual estilo Netflix
st.markdown("""
    <style>
    .main { background-color: #111; color: #fff; }
    .stTextInput > div > div > input { background-color: #222; color: #fff; border-radius: 5px; }
    h1, h2, h3 { color: #E50914; font-family: sans-serif; }
    .stButton>button { background-color: #E50914; color: white; border-radius: 5px; font-weight: bold; border: none; }
    </style>
""", unsafe_allow_html=True)

st.markdown("<h1 style='text-align: center; color: #E50914;'>🍿 StreamFinder - Cinema Online</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center; color: #aaa;'>Escolha um filme abaixo ou digite o ID do TMDB para assistir diretamente no player, sem chaves ou cadastros!</p>", unsafe_allow_html=True)
st.markdown("---")

# Filmes populares pré-configurados com IDs reais do TMDB
filmes_populares = {
    "Selecione um filme popular...": "",
    "Interestelar (2014)": "157336",
    "Batman: O Cavaleiro das Trevas (2008)": "155",
    "Vingadores: Ultimato (2019)": "299534",
    "O Poderoso Chefão (1972)": "238",
    "Titanic (1997)": "597",
    "A Origem (2010)": "27205",
    "Matrix (1999)": "603",
    "Homem-Aranha: Através do Aranhaverso (2023)": "569094"
}

col1, col2 = st.columns([2, 1])

with col1:
    escolha = st.selectbox("Escolha rápida de Filmes Populares:", list(filmes_populares.keys()))
    tmdb_selecionado = filmes_populares[escolha]

with col2:
    st.markdown("<br>", unsafe_allow_html=True)
    input_manual = st.text_input("Ou digite o ID do TMDB:", value=tmdb_selecionado if tmdb_selecionado else "")

# Define o ID final
tmdb_id = input_manual.strip() if input_manual else tmdb_selecionado

st.markdown("---")

if tmdb_id:
    st.subheader(f"🎬 Reproduzindo (TMDB ID: {tmdb_id})")
    
    # Player embutido integrado (VidSrc)
    embed_url = f"https://vidsrc.xyz/embed/movie?tmdb={tmdb_id}"
    
    player_html = f"""
    <div style="width: 100%; height: 520px; background: #000; border-radius: 10px; overflow: hidden; box-shadow: 0 4px 15px rgba(0,0,0,0.8);">
        <iframe src="{embed_url}" style="width: 100%; height: 100%; border: none;" allowfullscreen="true" webkitallowfullscreen="true" mozallowfullscreen="true"></iframe>
    </div>
    """
    components.html(player_html, height=550)
    
    st.success("Player carregado com sucesso! Divirta-se assistindo.")
else:
    st.info("💡 Selecione um filme na lista acima ou digite o ID do TMDB (por exemplo, `597` para Titanic) para começar a reprodução.")

st.markdown("---")
st.markdown("<p style='text-align: center; color: #666; font-size: 12px;'>StreamFinder - Entretenimento direto e sem complicações.</p>", unsafe_allow_html=True)
