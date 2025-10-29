# 💡 Sistema Preditivo de Concessão de Empréstimos  

## 🧠 Descrição do Projeto

Este projeto implementa um modelo preditivo de Machine Learning capaz de estimar a probabilidade de um cliente ter um empréstimo aprovado, com base em seu histórico bancário e perfil financeiro.

A aplicação foi desenvolvida em Python e disponibilizada através de uma interface web interativa em Streamlit, permitindo o input de dados e visualização automática dos resultados.

## ⚙️ Tecnologias Utilizadas

Bibliotecas Principais:

- Pandas → Análise e tratamento de dados

- NumPy → Manipulação numérica

- Scikit-learn → Criação e avaliação do modelo preditivo

- Matplotlib / Seaborn → Visualização de dados

- Streamlit → Interface web interativa  



## 🚀 Funcionalidades

- 📊 Importação e tratamento de dados bancários

- 🧮 Treinamento de modelo supervisionado (RandomForestClassifier)

- 📈 Exibição de métricas de performance (acurácia, precisão, recall)

- 💬 Interface interativa para entrada de novos dados

- 🔄 Predição em tempo real de aprovação de empréstimo


## 🧩 Como Executar o Projeto
Clone o repositório:
```bash 
git clone https://github.com/Georgettig/projeto-emprestimos-ml.git
python -m venv venv
.venv.\Scripts\activate
pip install -r requirements.txt
streamlit run app.py
