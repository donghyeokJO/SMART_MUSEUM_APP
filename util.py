import requests

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

if __name__ == "__main__":
    get_token()