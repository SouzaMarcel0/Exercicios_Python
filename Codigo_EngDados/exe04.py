
import requests

r = requests.get('http://servicos.cptec.inpe.br/XML/listaCidades?city=sao paulo')

print(r)