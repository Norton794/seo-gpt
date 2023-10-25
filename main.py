import pandas as pd
import requests
from dotenv import load_dotenv
import os

load_dotenv()


def gerar_seo_produtos(lista_produtos):
    url = "https://api.openai.com/v1/chat/completions"
    headers = {
        "Content-Type": "application/json",
        "Authorization": "Bearer " + os.getenv("OPENAI_API_KEY")
    }
    data = {
        "model": "gpt-3.5-turbo",
        "messages": [{"role": "user", "content": f"Gere a descrição SEO da seguinte lista de Produtos: {', '.join(lista_produtos)}"}],
        "temperature": 0.7
    }

    response = requests.post(url, headers=headers, data=json.dumps(data))
    return response.json()

planilha = pd.read_excel('sheet.xlsx')


lista_produtos = []
for index, row in planilha.iterrows():
    cod_prod = row['Codprod']
    descricao = row['Descrição']
    marca = row['Marca']
    lista_produtos.append(f"Produto: {cod_prod}, Descrição: {descricao}, Marca: {marca}")


seo_produtos = gerar_seo_produtos(lista_produtos)

planilha['SEO'] = seo_produtos

planilha.to_excel('new_sheet.xlsx', index=False)
