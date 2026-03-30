#BIBLIOTECAS USADAS( REQUESTS.GET / JSON.JSON )
import requests
import json

print("==BUSCA POR INFORMAÇÕES PELO CEP==")

cep = input("Escreva seu CEP ")

api = f"https://viacep.com.br/ws/{cep}/json/" #API CONSUMIDA

result = requests.get(api)  #CONSUMO DA API

if result.status_code == 200:
    infos = result.json()   #TRANSFORMAÇÃO DOS DADOS PARA JSON

    if 'erro' in infos:
        print('CEP NÃO ENCONTRADO!')

    else:
                 
    #FORMATAÇÃO
        print(f"CEP: {infos.get('cep', 'N/A')}")
        print(f"RUA: {infos.get('logradouro', 'N/A')}")
        print(f"BAIRRO: {infos.get('bairro', 'N/A')}")
        print(f"CIDADE: {infos.get('localidade', 'N/A')}")
        print(f"ESTADO: {infos.get('estado', 'N/A')}")
        print(f"DDD: {infos.get('ddd', 'N/A')}")

else:
    print(f"ERRO NA REQUISIÇÃO: {result.status_code}")
    
#DESENVOLVIDO POR JOÃO PEDRO PERLE