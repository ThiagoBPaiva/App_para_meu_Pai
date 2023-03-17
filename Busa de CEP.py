import requests

cep = str(input('Digite seu CEP: '))

cep = cep.replace('-', '').replace('.', '').replace(' ', '')

if len(cep) == 8:
    link = f'https://viacep.com.br/ws/{cep}/json/'

    requisicao = requests.get(link)

    dic_requisicao = requisicao.json()

    uf = dic_requisicao['uf']
    naturalidade = dic_requisicao['localidade']
    rua = dic_requisicao['logradouro']
    bairro = dic_requisicao['bairro']
    print(f'UF: {uf}\n'
          f'Naturalidade: {naturalidade}\n'
          f'Rua: {rua}\n'
          f'Bairro: {bairro}')
else:
    print('CPF invalido')