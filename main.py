import streamlit as st
from streamlit_option_menu import option_menu
from streamlit_lottie import st_lottie
import json


# Configuração da página principal
st.set_page_config(page_title="IA products", page_icon="💰")

st.markdown(
    f"""
    <style>
    {open("static/styles.css").read()}
    </style>
    """,
    unsafe_allow_html=True
)



# animações
with open("animaçoes/animation4.json") as source:
    animacao_1 = json.load(source)

# Menu de navegação
with st.sidebar:

       #exibir animação
    st_lottie(animacao_1, height=200, width=270)


    

    selected = option_menu("Menu", ["Home", "Recomendações de Produto", "Sobre o Projeto"],
                           icons=['house', 'box', 'info-circle'], 
                           menu_icon="cast", default_index=0)
    
      # badges
    st.markdown(
        """
    <div style="display: flex; justify-content: space-between;">
        <div>
            <a href="https://github.com/thaleson" target="_blank">
                <img src="https://img.shields.io/badge/GitHub-100000?style=for-the-badge&logo=github&logoColor=white" width="100" />
            </a>
        </div>
        <div>
            <a href="https://www.linkedin.com/in/thaleson-silva-9298a0296/" target="_blank">
                <img src="https://img.shields.io/badge/LinkedIn-0077B5?style=for-the-badge&logo=linkedin&logoColor=white" width="100" />
            </a>
        </div>
        <div>
            <a href="mailto:thaleson177@gmail.com" target="_blank">
                <img src="https://img.shields.io/badge/Gmail-D14836?style=for-the-badge&logo=gmail&logoColor=white" width="90" />
            </a>
        </div>
    </div>
    """,
        unsafe_allow_html=True,
    )
# Navegação para as páginas
if selected == "Home":
    from pages.nav import home
    home.show()
elif selected == "Recomendações de Produto":
    from pages.nav import recommendations
    recommendations.show()
elif selected == "Sobre o Projeto":
    from pages.nav import about
    about.show()
