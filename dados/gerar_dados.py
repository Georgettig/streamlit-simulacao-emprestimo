import pandas as pd
import numpy as np

np.random.seed(42)
n = 2000
df = pd.DataFrame({
    "idade": np.random.randint(18, 80, n),
    "renda_mensal": np.random.randint(1000, 20000, n),
    "dividas": np.random.randint(0, 50000, n),
    "historico": np.random.randint(0, 2, n),
    "anos_trabalhados": np.random.randint(0, 40, n),
    "dependentes": np.random.randint(0, 5, n),
    "propriedades": np.random.randint(0, 3, n),
    "score": np.random.randint(300, 850, n),
    "emprestimos_pendentes": np.random.randint(0, 5, n),
    "pagamentos_atrasados": np.random.randint(0, 10, n)
})

df["aprovado"] = (
    (df["renda_mensal"] > df["dividas"]*0.5) &
    (df["historico"] == 1) &
    (df["pagamentos_atrasados"] <= 2) &
    (df["score"] >= 600)
).astype(int)

df.to_csv("emprestimos.csv", index=False)
print("Dataset criado com sucesso!")