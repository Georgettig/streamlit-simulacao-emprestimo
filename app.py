import streamlit as st
import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.ensemble import RandomForestClassifier

st.set_page_config(page_title="Simulador de Empréstimos", layout="wide")
st.title("💰 Simulador de Aprovação de Empréstimos")

df = pd.read_csv("dados/emprestimos.csv")

# Treinar modelo
X = df.drop("aprovado", axis=1)
y = df["aprovado"]

num_cols = ["idade","renda_mensal","dividas","anos_trabalhados","dependentes","score","emprestimos_pendentes","pagamentos_atrasados"]

scaler = StandardScaler()

X[num_cols] = scaler.fit_transform(X[num_cols])

model = RandomForestClassifier(n_estimators=40, criterion='entropy', random_state=42)
model.fit(X, y)

# Layout da página
col1, col2, col3 = st.columns([1,2,1])

with col2:
    st.markdown("Preencha os dados abaixo para simular um resultado:")
    input_data = {
        "idade": st.number_input("Idade", min_value=18, max_value=70, value=30),
        "renda_mensal": st.number_input("Renda Mensal", min_value=1000, max_value=20000, value=5000),
        "dividas": st.number_input("Dívidas", min_value=0, max_value=50000, value=10000),
        "historico": st.selectbox("Histórico de Crédito (0: Ruim, 1: Bom)", [0,1]),
        "anos_trabalhados": st.number_input("Anos de Emprego", min_value=0, max_value=40, value=5),
        "dependentes": st.number_input("Dependentes", min_value=0, max_value=5, value=0),
        "propriedades": st.selectbox("Possui Casa? (0: Não, 1: Sim)", [0,1]),
        "score": st.number_input("Score Bancário", min_value=300, max_value=850, value=650),
        "emprestimos_pendentes": st.number_input("Empréstimos Pendentes", min_value=0, max_value=5, value=0),
        "pagamentos_atrasados": st.number_input("Pagamentos Atrasados", min_value=0, max_value=10, value=0)
    }

    input_df = pd.DataFrame([input_data])
    input_df[num_cols] = scaler.transform(input_df[num_cols])

    previsao = model.predict(input_df)[0]

    st.subheader("📊 Resultado da Simulação")
    if st.button("Realizar Previsão"):
        if previsao == 1:
            st.success("Empréstimo aprovado ✅")
        else:
            st.error("Empréstimo negado ❌")
