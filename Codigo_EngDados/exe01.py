

from requests import requests
from flask import Flask

print('Digite o número do CEP - Apenas os números \n')
cep_client = input(str())

#Remover espaço no começo e fim da string e substituir '-' por espaço branco.
cep_client = cep_client.strip()
if len(cep_client) == 9:
    cep_client = cep_client.replace('-', "")

r = requests.get(f'https://viacep.com.br/ws/{cep_client}/json/')
r = r.json()

app = Flask(__name__)
# $ set FLASK_APP=exe01.py
# $ run flask
@app.get('/')

def return_cep():
    return r
print(r)