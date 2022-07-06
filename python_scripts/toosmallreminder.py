import requests
from bs4 import BeautifulSoup as BS

URL = "http://too-small-reminder.challs.olicyber.it/"
header = {'Content-type': 'application/json'}

def GET_Request():
    response = requests.get(URL)
    response.raise_for_status()

    print(response.text)

def GET_Request_Admin(cookie):
    response = requests.get(URL + 'admin', cookies=cookie)
    response.raise_for_status()

    print(response.text)

def POST_Request_Reg():
    response = requests.post(URL + "register", data={"username": "cane", "password": "gatto"}, headers=header)
    response.raise_for_status()

def POST_Request_Log():
    response = requests.post(URL + 'login', data={"username": "cane", "password": "gatto"}, headers=header)
    response.raise_for_status()

    print(f'DEBUG: Cookie letto=[{response.cookies}]')
    return response.cookies

if __name__ == '__main__':
    GET_Request()
    POST_Request_Reg()
    cookie = POST_Request_Log()
    GET_Request_Admin(cookie)