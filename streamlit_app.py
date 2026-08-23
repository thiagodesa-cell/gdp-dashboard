import streamlit as st
import streamlit.components.v1 as components
import requests

# Configuração da página
st.set_page_config(
    page_title="StreamFinder - Cinema Online",
    page_icon="🍿",
    layout="wide"
)

# Estilização visual
st.markdown("""
    <style>
    .main { background-color: #111; color: #fff; }
    .stTextInput > div > div > input { background-color: #222; color: #fff; border-radius: 5px; }
    h1, h2, h3 { color: #E50914; font-family: sans-serif; }
    .stButton>button { background-color: #E50914; color: white; border-radius: 5px; font-weight: bold; border: none; }
    </style>
""", unsafe_allow_html=True)

st.markdown("<h1 style='text-align: center; color: #E50914;'>🍿 StreamFinder - Cinema Online</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center; color: #aaa;'>Digite o nome de qualquer filme para buscar e assistir instantaneamente!</p>", unsafe_allow_html=True)
st.markdown("---")

# Barra de pesquisa por nome
pesquisa = st.text_input("🔍 Digite o nome do filme que deseja assistir:", placeholder="Ex: Avatar, Interestelar, Batman...")

# Chave pública gratuita do TMDB para buscas básicas
TMDB_API_KEY = "3c59325f57f12e84d1bc978ae1b03362"

if pesquisa:
    with st.spinner("Buscando filme..."):
        url = f"https://api.themoviedb.org/3/search/movie?api_key={TMDB_API_KEY}&language=pt-BR&query={pesquisa}"
        response = requests.get(url)
        dados = response.json()
        resultados = dados.get("results", [])

    if resultados:
        st.success(f"Encontramos {len(resultados)} filme(s)!")
        
        # Cria um seletor com os filmes encontrados na busca
        filmes_opcoes = {f"{f['title']} ({f.get('release_date', 'Data desconhecida')[:4]})": f['id'] for f in resultados}
        filme_escolhido_nome = st.selectbox("Selecione o filme correto:", list(filmes_opcoes.keys()))
        tmdb_id = filmes_opcoes[filme_escolhido_nome]
        
        st.markdown("---")
        st.subheader(f"🎬 Reproduzindo: {filme_escolhido_nome}")
        
        # Player de streaming integrado
        embed_url = f"https://vidsrc.xyz/embed/movie?tmdb={tmdb_id}"
        
        player_html = f"""
        <div style="width: 100%; height: 520px; background: #000; border-radius: 10px; overflow: hidden; box-shadow: 0 4px 15px rgba(0,0,0,0.8);">
            <iframe src="{embed_url}" style="width: 100%; height: 100%; border: none;" allowfullscreen="true" webkitallowfullscreen="true" mozallowfullscreen="true"></iframe>
        </div>
        """
        components.html(player_html, height=550)
        
    else:
        st.warning("Nenhum filme encontrado com esse nome. Tente digitar de outra forma.")
else:
    st.info("💡 Dica: Digite o nome de um filme na caixa acima para pesquisar em um catálogo com milhares de opções.")

st.markdown("---")
st.markdown("<p style='text-align: center; color: #666; font-size: 12px;'>StreamFinder - Entretenimento direto e sem complicações.</p>", unsafe_allow_html=True)
