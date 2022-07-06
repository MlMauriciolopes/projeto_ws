import requests
import json
from enderecos import Endereco

cep = input("Digite um cep: ")

r = requests.get("https://viacep.com.br/ws/%s/json/" % cep)

if r.status_code == requests.codes.ok:
	j = json.loads(r.text)

	endereco = Endereco()
	endereco.cep = j['cep']
	endereco.logradouro = j['logradouro'] 
	endereco.complemento = j['complemento']
	endereco.bairro = j['bairro']
	endereco.localidade = j['localidade']
	endereco.uf = j['uf']
	endereco.unidade = j['unidade']
	endereco.ibge = j['ibge']
	endereco.gia = j['gia']

	endereco.salvar()

else:
	print("Cep não encontrado!")