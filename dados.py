# importanto bibliotecas necessarioas
import requests
import json

# link contendo a api
api_link = "https://dicio-api-ten.vercel.app/v2/comer"

# requests
r = requests.get(api_link)

# convertendo os dados do request em dicionario
dados = r.json()

print(dados)