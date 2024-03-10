import requests

def main():
    cepInput = input('Digite o cep que você quer verificar? ')

    if len(cepInput) != 8:
        print('Quantidade de digitos inválidas')
        exit()
        
        #teste commit adede
    request = requests.get('https://viacep.com.br/ws/{}/json/'.format(cepInput))

    addresData = request.json()

    if 'erro' not in addresData:
        print('CEP: {}'.format(addresData['cep']))
        print('Logradouro: {}'.format(addresData['logradouro']))
        print('Bairro: {}'.format(addresData['bairro']))
        
        yesInput = input('Você quer ver todas as informações? (y/n) ')
        
        if yesInput == 'y': print(addresData)
        else: exit()

    else:
        print('{}: CEP inválido.'.format(cepInput))
    
    option = input('Você deseja fazer uma nova consulta? (y/n) ')
    if option == 'y': main()
    else: exit()
    #teste
        
if __name__ == '__main__':
    main()