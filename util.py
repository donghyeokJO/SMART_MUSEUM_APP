import requests
import netifaces as nif

def get_token():
    id = 'admin'
    pw = '1234'

    URL = 'http://59.19.102.174:8888/api/v1/token-auth/'

    response = requests.post(URL, data={'username': id, 'password': pw})

    # print(response)
    res = response.json()

    token = res['access']

    # print('JWT ' + token)
    return 'JWT ' + token

def get_fsm_token():
    id = "test"
    pw = '12345'

    URL = 'http://59.19.102.174:8888/api/v1/token-auth/'

    response = requests.post(URL, data={'username': id, 'password': pw})

    # print(response)
    res = response.json()

    token = res['access']

    # print('JWT ' + token)
    return 'JWT ' + token

def mac_for_ip(ip):
    'Returns a list of MACs for interfaces that have given IP, returns None if not found'
    for i in nif.interfaces():
        addrs = nif.ifaddresses(i)

        if_mac = addrs[nif.AF_LINK][0]['addr']

    
        return if_mac


if __name__ == "__main__":
    get_token()