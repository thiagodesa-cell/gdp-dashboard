import requests
import streamlit as st

# Configuração da página
st.set_page_config(
    page_title="StreamFinder - Seus Filmes Favoritos",
    page_icon="🍿",
    layout="wide",
)

# Estilização em CSS (Dark Mode)
st.markdown(
    """
    <style>
    .stApp {
        background-color: #0f1015;
        color: #ffffff;
    }
    .hero-container {
        padding: 30px 20px;
        background: linear-gradient(180deg, rgba(229, 9, 20, 0.15) 0%, rgba(15, 16, 21, 0) 100%);
        border-radius: 12px;
        text-align: center;
        margin-bottom: 25px;
    }
    .movie-card {
        background-color: #181b22;
        border-radius: 10px;
        padding: 20px;
        margin-bottom: 20px;
        border: 1px solid #2a2e39;
        box-shadow: 0 4px 10px rgba(0,0,0,0.3);
    }
    .streaming-badge {
        display: inline-block;
        background-color: #e50914;
        color: white !important;
        padding: 6px 14px;
        border-radius: 4px;
        text-decoration: none;
        font-weight: bold;
        font-size: 14px;
        margin: 4px 4px 4px 0;
        transition: background 0.2s;
    }
    .streaming-badge:hover {
        background-color: #f40612;
    }
    </style>
""",
    unsafe_allow_html=True,
)

# Suas credenciais do RapidAPI
RAPIDAPI_KEY = "2981e7e072msh7c1e16f30f788ap1a37e1jsn4424707c8b9e"
RAPIDAPI_HOST = "streaming-availability.p.rapidapi.com"

# Cabeçalho Visual
st.markdown(
    """
    <div class="hero-container">
        <h1>🍿 StreamFinder</h1>
        <p style="color: #94a3b8; font-size: 18px;">Descubra instantaneamente onde assistir aos seus filmes favoritos nos streamings</p>
    </div>
""",
    unsafe_allow_html=True,
)

# Barra lateral
with st.sidebar:
  st.header("⚙️ Preferências")
  country = st.selectbox(
      "Seu País / Região",
      ["br", "us", "gb", "ca", "ar"],
      index=0,
      help="Altera o catálogo base de disponibilidade.",
  )
  st.markdown("---")
  st.info("Dica: Digite o nome do filme em inglês ou português.")

# Caixa de pesquisa centralizada
col_space1, col_center, col_space2 = st.columns([1, 6, 1])
with col_center:
  filme_pesquisa = st.text_input(
      "",
      placeholder="🔍 Digite o nome do filme (ex: The Batman, Interstellar)...",
      label_visibility="collapsed",
  )

if filme_pesquisa:
  with st.spinner("Buscando no catálogo dos streamings..."):
    # Atualizado para a versão V4 da API mostrada no seu painel
    url = f"https://{RAPIDAPI_HOST}/v4/shows/search/title"

    querystring = {
        "title": filme_pesquisa,
        "country": country,
        "show_type": "movie",
        "output_language": "en",
    }

    headers = {
        "x-rapidapi-key": RAPIDAPI_KEY,
        "x-rapidapi-host": RAPIDAPI_HOST,
    }

    try:
      response = requests.get(url, headers=headers, params=querystring)

      if response.status_code == 200:
        dados = response.json()
        # Na V4, o retorno pode vir diretamente como lista ou dentro de uma chave 'result'
        resultados = (
            dados
            if isinstance(dados, list)
            else dados.get("result", dados.get("shows", []))
        )

        if not resultados:
          st.warning(
              "Nenhum filme encontrado com esse nome para a região"
              f" selecionada ({country.upper()})."
          )
        else:
          st.markdown(
              f"<p style='text-align: center; color: #94a3b8;'>Foram encontrados"
              f" <b>{len(resultados)}</b> títulos.</p>",
              unsafe_allow_html=True,
          )

          for item in resultados:
            titulo = item.get("title", "Título desconhecido")
            ano = item.get("releaseYear", "")
            sinopse = item.get("overview", "Sem sinopse disponível.")
            rating = item.get("rating", item.get("voteAverage"))

            # Imagem do pôster
            image_url = item.get("imageSet", {}).get(
                "verticalPoster", {}
            ) or item.get("imageSet", {}).get("horizontalBackdrop", {})
            if isinstance(image_url, dict):
              image_url = image_url.get("url", "")

            streaming_options = item.get("streamingOptions", {}).get(
                country, []
            )

            with st.container():
              st.markdown('<div class="movie-card">', unsafe_allow_html=True)
              col_img, col_info = st.columns([1, 3])

              with col_img:
                if image_url:
                  st.image(image_url, use_container_width=True)
                else:
                  st.markdown("*(Sem imagem)*")

              with col_info:
                st.markdown(f"### {titulo} ({ano})")

                if rating:
                  st.markdown(f"⭐ **Avaliação:** `{rating}`")

                st.write(sinopse)

                st.markdown("---")
                st.markdown("**📺 Onde assistir:**")

                if streaming_options:
                  links_html = ""
                  for opt in streaming_options:
                    servico = opt.get("service", {}).get("name", "Streaming")
                    link = opt.get("link", "#")
                    tipo = opt.get("accessType", "subscription")
                    tipo_txt = (
                        "Assinatura" if tipo == "subscription" else "Aluguel"
                    )

                    links_html += f'<a href="{link}" target="_blank" class="streaming-badge">▶ {servico} ({tipo_txt})</a> '

                  st.markdown(links_html, unsafe_allow_html=True)
                else:
                  st.markdown(
                      "<span style='color: #f87171;'>Indisponível em"
                      f" streamings tradicionais em {country.upper()}.</span>",
                      unsafe_allow_html=True,
                  )

              st.markdown("</div>", unsafe_allow_html=True)

      else:
        st.error(
            f"Erro ao consultar a API. Código: {response.status_code} - Resposta:"
            f" {response.text}"
        )

    except Exception as e:
      st.error(f"Erro de conexão: {e}")
