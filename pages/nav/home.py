import json
import streamlit as st
from streamlit_lottie import st_lottie

def load_lottie_animation(file_path):
    """Carregar a animação Lottie a partir do arquivo JSON"""
    try:
        with open(file_path, "r") as f:
            return json.load(f)
    except FileNotFoundError:
        st.error(f"Arquivo não encontrado: {file_path}")
        return None
    except json.JSONDecodeError:
        st.error(f"Erro ao decodificar o arquivo JSON: {file_path}")
        return None

def show():
    # Configurar o título da página
    st.title("Bem-vindo ao Sistema de Recomendação de Produtos! 🎉")

    # Adicionar subtítulo
    st.subheader("Olá! Descubra as melhores recomendações de produtos 👋")

    # Carregar animações
    animation_1 = load_lottie_animation("animaçoes/animationproduct.json")
    animation_2 = load_lottie_animation("animaçoes/animation3.json")  # Substitua por um arquivo diferente, se necessário

    if animation_1 and animation_2:
        # Configurar layout em colunas
        col1, col2 = st.columns(2)

        # Conteúdo da coluna 1
        with col1:
            st_lottie(animation_1, height=350, width=350, key="animation1")
            st.markdown(
                """
                <div style='margin-top: 10px;'>
                    <h5 style='text-align: justify;'>Este site oferece recomendações personalizadas de produtos com base na sua pesquisa. Utilizamos técnicas avançadas de processamento de linguagem natural e aprendizado de máquina para fornecer recomendações precisas.</h5>
                </div>
                """,
                unsafe_allow_html=True
            )

        # Conteúdo da coluna 2
        with col2:
            st.markdown(
                """
                <div style='margin-top: 10px;'>
                    <h5 style='text-align: justify;'>Aqui você pode procurar por produtos e receber recomendações similares, além de explorar informações detalhadas sobre o projeto e as tecnologias utilizadas.</h5>
                </div>
                """,
                unsafe_allow_html=True
            )
            st_lottie(animation_2, height=350, width=350, key="animation2")

        # Adicionar um aviso
        st.markdown(
            """
            <div style='background-color: #d4edda; padding: 15px; border-radius: 8px;'>
                <h4 style='color: #155724;'>Aviso:</h4>
                <p style='color: #155724;'>Este projeto é uma demonstração das capacidades de recomendação de produtos. A precisão das recomendações pode variar e deve ser usada como uma referência adicional.</p>
            </div>
            """,
            unsafe_allow_html=True
        )
    else:
        st.warning("Não foi possível carregar as animações.")

if __name__ == "__main__":
    show()
