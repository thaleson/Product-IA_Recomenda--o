import streamlit as st

def show():
    st.header("Sobre o Projeto")
    st.write(
        """
        Bem-vindo ao nosso projeto de **Recomendação de Produtos**! 🌟

        Este projeto é uma aplicação avançada que utiliza técnicas de processamento de linguagem natural e aprendizado de máquina para fornecer recomendações de produtos personalizadas. Através de modelos de similaridade de texto, nossa aplicação encontra produtos semelhantes com base nas preferências e entradas fornecidas pelo usuário.

        ### Como Funciona
        1. **Entrada do Usuário**: Você insere o nome de um produto que está procurando.
        2. **Processamento**: Nosso sistema utiliza modelos de **TF-IDF** e **similaridade de cosseno** para analisar e entender o texto.
        3. **Recomendações**: A aplicação retorna uma lista de produtos similares com base na sua consulta.

        ### Tecnologias Utilizadas
        - **Python**: Linguagem de programação principal para desenvolvimento e manipulação de dados.
        - **Streamlit**: Framework para criação de aplicações web interativas e fáceis de usar.
        - **Scikit-learn**: Biblioteca para implementação de modelos de aprendizado de máquina e processamento de texto.
        - **Pandas**: Biblioteca essencial para manipulação e análise de dados.
        - **Pickle**: Utilizado para armazenar e carregar modelos treinados de forma eficiente.

        ### Funcionalidades
        - **Busca de Produtos**: Encontre produtos semelhantes com base em suas preferências.
        - **Interface Intuitiva**: Navegue facilmente através de uma interface simples e amigável.
        - **Recomendações Relevantes**: Receba sugestões personalizadas e precisas com base nas entradas fornecidas.

        ### Objetivo
        O objetivo principal deste projeto é aprimorar a experiência de compra dos usuários, oferecendo recomendações precisas e úteis que ajudam a encontrar produtos relacionados de forma rápida e eficiente.

        **Agradecemos por utilizar nossa aplicação e esperamos que ela torne suas buscas de produtos mais fáceis e agradáveis!** 😊
        """
    )
