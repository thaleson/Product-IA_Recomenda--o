import streamlit as st
import pandas as pd
import pickle
from sklearn.metrics.pairwise import linear_kernel
import re
import time  # Importar time para simular a duração da barra de progresso

@st.cache_data
def load_data():
    """
    Carrega os dados do CSV e os modelos salvos para recomendações de produtos.

    Retorna:
        df (DataFrame): DataFrame contendo os dados dos produtos.
        cosine_sim (ndarray): Matriz de similaridade coseno pré-calculada.
        tfidf_model (TfidfVectorizer): Modelo TF-IDF pré-treinado.
    """
    df = pd.read_csv('data/amazon.csv')
    with open('models/cosine_sim.pkl', 'rb') as file:
        cosine_sim = pickle.load(file)
    with open('models/tfidf_model.pkl', 'rb') as file:
        tfidf_model = pickle.load(file)
    return df, cosine_sim, tfidf_model

# Carrega os dados e os modelos
df, cosine_sim, tfidf_model = load_data()

# Mapeamento de termos em português para inglês
term_mapping = {
  term_mapping = {
    'celular': 'phone',
    'smartphone': 'phone',
    'computador': 'computer',
    'notebook': 'laptop',
    'acessórios': 'accessories',
    'cabo': 'cable',
    'carregador': 'charger',
    'ventilador': 'fan',
    'cozinha': 'kitchen',
    'fritadeira': 'fryer',
    'televisão': 'tv',
    'televisor': 'tv',
    'refrigerador': 'fridge',
    'geladeira': 'fridge',
    'micro-ondas': 'microwave',
    'forno': 'oven',
    'cafeteira': 'coffee maker',
    'liquidificador': 'blender',
    'torradeira': 'toaster',
    'máquina de lavar': 'washing machine',
    'secadora': 'dryer',
    'ar condicionado': 'air conditioner',
    'ventilador de teto': 'ceiling fan',
    'aquecedor': 'heater',
    'aspirador': 'vacuum cleaner',
    'máquina de café': 'coffee machine',
    'panelas': 'pots',
    'frigideira': 'frying pan',
    'tábua de corte': 'cutting board',
    'processador de alimentos': 'food processor',
    'escova de cabelo': 'hairbrush',
    'secador de cabelo': 'hair dryer',
    'chapinha': 'hair straightener',
    'epilador': 'epilator',
    'relógio': 'watch',
    'pulseira': 'bracelet',
    'brinco': 'earring',
    'colar': 'necklace',
    'anel': 'ring',
    'óculos': 'glasses',
    'lupa': 'magnifying glass',
    'câmera': 'camera',
    'tripé': 'tripod',
    'microfone': 'microphone',
    'alto-falante': 'speaker',
    'fone de ouvido': 'headphones',
    'mouse': 'mouse',
    'teclado': 'keyboard',
    'impressora': 'printer',
    'scanner': 'scanner',
    'modem': 'modem',
    'roteador': 'router'


}

def normalize_text(text):
    """
    Normaliza o texto removendo acentos e convertendo para minúsculas.

    Args:
        text (str): Texto a ser normalizado.

    Retorna:
        str: Texto normalizado.
    """
    text = text.lower()
    text = re.sub(r'[áàãâä]', 'a', text)
    text = re.sub(r'[éèêë]', 'e', text)
    text = re.sub(r'[íìîï]', 'i', text)
    text = re.sub(r'[óòõôö]', 'o', text)
    text = re.sub(r'[úùûü]', 'u', text)
    text = re.sub(r'[ç]', 'c', text)
    return text

def format_price(price):
    """
    Formata o preço removendo símbolos de moeda e convertendo para float,
    e então para o formato de Real brasileiro.

    Args:
        price (str): Preço a ser formatado.

    Retorna:
        str: Preço formatado.
    """
    price = price.replace('₹', '').replace(',', '')
    try:
        price_float = float(price)
        return f"R${price_float:,.2f}".replace('.', ',')
    except ValueError:
        return price

def get_recommendations(product_name):
    """
    Retorna recomendações de produtos similares com base no nome do produto fornecido.

    Args:
        product_name (str): Nome do produto para o qual se deseja recomendações.

    Retorna:
        DataFrame/str: DataFrame contendo os produtos recomendados ou mensagem de aviso.
    """
    product_name = normalize_text(product_name)
    product_name_en = term_mapping.get(product_name, product_name)
    
    matching_products = df[df['product_name'].str.contains(product_name_en, case=False, na='')]
    
    if matching_products.empty:
        return "Não temos esse produto em nosso estoque para te recomendar."

    idx = matching_products.index[0]
    sim_scores = list(enumerate(cosine_sim[idx]))
    sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)
    sim_scores = sim_scores[1:6]
    product_indices = [i[0] for i in sim_scores]
    recommended_products = df.iloc[product_indices][['product_name', 'discounted_price', 'rating']]
    recommended_products['discounted_price'] = recommended_products['discounted_price'].apply(format_price)
    
    # Renomear as colunas para português
    recommended_products.columns = ['Nome do Produto', 'Preço', 'Classificação']
    
    return recommended_products

def show():
    """
    Exibe a interface do usuário do sistema de recomendação de produtos usando Streamlit.
    """
    st.header("Recomendações de Produto")
    st.write("Digite o nome de um produto para receber recomendações similares.")

    search_term = st.text_input("Nome do produto")
    search_button = st.button("Buscar")
    
    if search_button:
        if search_term:
            # Simular a duração da barra de progresso
            progress_bar = st.progress(0)
            for i in range(100):
                time.sleep(0.01)  # Simular tempo de carregamento
                progress_bar.progress(i + 1)
            
            recommendations = get_recommendations(search_term)
            if isinstance(recommendations, str):
                st.warning(recommendations)
            else:
                st.success("Recomendações encontradas:")
                
                # Exibir recomendações em uma tabela estilizada
                st.dataframe(recommendations, use_container_width=True)
        else:
            st.warning("Por favor, insira o nome do produto para pesquisar.")

if __name__ == "__main__":
    show()
