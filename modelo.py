import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report

# Lendo a base de dados
df = pd.read_csv("dados/emprestimos.csv")

# Separando a base de dados
X = df.drop(columns=["aprovado"])
y = df["aprovado"]

# Instanciando os dados de treino e teste
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

# Selecionando colunas para escalonar
num_cols = ["idade","renda_mensal","dividas","anos_trabalhados","dependentes","score",
            "emprestimos_pendentes","pagamentos_atrasados"]

# Escalonando colunas selecionadas
scaler = StandardScaler()
X_train[num_cols] = scaler.fit_transform(X_train[num_cols])
X_test[num_cols] = scaler.transform(X_test[num_cols])

# Instanciando e treinando o modelo preditivo
model = RandomForestClassifier(n_estimators=40, criterion='entropy', random_state=42)
model.fit(X_train, y_train)

# Realizando as previsões
y_pred = model.predict(X_test)

# Avaliando a acuráricia do modelo
print(accuracy_score(y_test, y_pred))