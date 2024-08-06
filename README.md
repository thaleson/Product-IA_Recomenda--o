# Sistema de Recomendação de Produtos

Bem-vindo ao **Sistema de Recomendação de Produtos**! 🎉 Este projeto oferece uma plataforma para recomendar produtos com base nas suas pesquisas, utilizando técnicas avançadas de processamento de linguagem natural e aprendizado de máquina.

## 🚀 Funcionalidades

- **Recomendações Personalizadas**: Receba recomendações de produtos com base no nome do produto pesquisado.
- **Interface Intuitiva**: Navegue facilmente através das páginas usando o menu de navegação.
- **Animações Atraentes**: Visualize animações interativas para uma experiência de usuário envolvente.

## 🛠️ Instalação

Siga os passos abaixo para configurar o ambiente e executar o projeto:

1. **Clone o Repositório**

   ```bash
   git clone https://github.com/thaleson/Product-IA_Recomenda--o
   cd seu-repositorio
   ```

2. **Criar e Ativar Ambiente Virtual**

   Se estiver usando `conda`:

   ```bash
   conda create --name seu-ambiente python=3.8
   conda activate seu-ambiente
   ```

3. **Instalar Dependências**

   Com o ambiente ativado, instale as dependências do projeto:

   ```bash
   pip install -r requirements.txt
   ```

4. **Executar o Projeto**

   Para iniciar o servidor Streamlit e visualizar a aplicação:

   ```bash
   streamlit run main.py
   ```

## 📂 Estrutura do Projeto

- `main.py`: Arquivo principal para executar a aplicação Streamlit.
- `data/amazon.csv`: Dados de produtos usados para recomendações.
- `models/`: Contém modelos e arquivos necessários para a recomendação.
- `pages/nav/`: Contém as páginas para navegação (Home, Recomendações de Produto, Sobre o Projeto).
- `static/styles.css`: Arquivo de estilos CSS para a interface.
- `animações/`: Contém arquivos JSON de animações Lottie.

## 🤖 Como Funciona

1. **Carregamento de Dados e Modelos**: O sistema carrega os dados dos produtos e os modelos necessários para a recomendação.
2. **Processamento e Recomendação**: Quando o usuário pesquisa um produto, o sistema utiliza técnicas de similaridade para encontrar e recomendar produtos semelhantes.
3. **Exibição das Recomendações**: As recomendações são exibidas em uma tabela com informações relevantes como nome, preço e classificação.


## ⚠️ Respeito e Ética

Nos preocupamos com a privacidade e a ética na utilização de dados. Ao usar este sistema, certifique-se de respeitar as seguintes diretrizes:

- **Respeito aos Dados Pessoais**: Não utilize este sistema para processar dados pessoais sem permissão adequada.
- **Uso Responsável**: Use as recomendações como referência adicional e não como única fonte de decisão.


## 📜 Licença

Este projeto está licenciado sob a [MIT License](LICENSE).
