import json
import pandas as pd # type: ignore

# Carregar o arquivo JSON
with open("C:\\Users\\alxdr\\Downloads\\teste.json", encoding="utf-8") as f:
    data = json.load(f)

# Extrair os monstros da chave "results"
monsters = data["results"]

# Criar um DataFrame a partir da lista de monstros
df = pd.DataFrame(monsters)

# Salvar no Excel
df.to_excel("monstros.xlsx", index=False)

print("Arquivo monstros.xlsx criado com sucesso!")
