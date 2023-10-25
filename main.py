import pandas as pd
import requests
from dotenv import load_dotenv
import os
import json


load_dotenv()


def gerar_seo_produtos(lista_produtos):
    url = "https://api.openai.com/v1/chat/completions"
    headers = {
        "Content-Type": "application/json",
        "Authorization": "Bearer " + os.getenv("OPENAI_API_KEY")
    }
    data = {
        "model": "gpt-3.5-turbo",
        "messages": [{"role": "user", "content": f"Produtos: {', '.join(lista_produtos)}"}],
        "temperature": 0.7
    }

    response = requests.post(url, headers=headers, data=json.dumps(data))
    print (response)
    return response.json()


caminho_pasta = 'sheets/'


caminho_planilha = os.path.join(caminho_pasta, 'sheet.xlsx')
planilha = pd.read_excel(caminho_planilha)


lista_produtos = []
for index, row in planilha.iterrows():
    cod_prod = row['codprod']
    descricao = row['descrprod']
    marca = row['marca']
    lista_produtos.append(f"Produto: {cod_prod}, Descrição: {descricao}, Marca: {marca}")


try:
    seo_produtos = gerar_seo_produtos(lista_produtos)
    planilha['SEO'] = seo_produtos
    caminho_nova_planilha = os.path.join(caminho_pasta, 'new_sheet.xlsx')
    planilha.to_excel(caminho_nova_planilha, index=False)

except Exception as e:
    print(f"Ocorreu um erro: {e}")
