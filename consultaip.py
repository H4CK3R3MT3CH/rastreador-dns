import requests
import json

def main():
    print('''
    SEJAM BEM VINDOS A:

    ##############################
    ## ---> Consulta de IP <--- ##
    ##############################

    Desenvolvedor   : MRX
    Apoiadores      : Cyber Stelf

    ''')

    ip_input = input('Digite o IP que deseja consultar:_  ')

    response = requests.get("http://ip-api.com/json/{}".format(ip_input))
    
    address_data = response.json()

    if 'erro' not in address_data:
        print(' ===> IP ENCONTRADO <=== ')

        print('ip: {}'.format(address_data['query']))
        print("status: {}".format(address_data['status']))
        print("country: {}".format(address_data['country']))
        print("countryCode: {}".format(address_data['countryCode']))
        print("region: {}".format(address_data['region']))
        print("cidade: {}".format(address_data['city']))
        print("latitude: {}".format(address_data['lat']))
        print("longitude: {}".format(address_data['lon']))
        exit()
    else:
        print(" ===> IP NÃO ENCONTRADO <=== ")

        aux = input("Deseja realizar uma nova consulta? Y=sim N=não:_")

        if aux == 'Y' or aux == 'y':
            main()

        if aux == 'n' or aux == 'N':
            print("Fechando...")
 
if __name__ == '__main__':
	main()