from hamcrest import none
import requests
from bs4 import BeautifulSoup

URL = "http://infinite.challs.olicyber.it/"

def GET_request():
    response = requests.get(URL)
    response.raise_for_status()

    GET_response = response.text
    soup = BeautifulSoup(GET_response, 'html.parser')
    type_of_test = str(soup.find('title'))
    print(f'DEBUG: type_of_test={type_of_test}')

    if type_of_test == '<title> GRAMMAR TEST </title>':
        test_string = str(soup.find('p'))
        phrases = test_string.split('"')
        res = phrases[3].count(phrases[1])
        print(f'DEBUG: Ci sono n.{res} di {phrases[1]} in {phrases[3]}.')


    elif type_of_test == '<title> MATH TEST </title>':
        test_string = str(soup.find('p'))
        print(f'DEBUG: phrases={test_string}')

        for i in range(len(test_string)):
            if test_string[i].isdigit():
                print(f'DEBUG: da stampare {test_string[i:len(test_string)-6]}')
                res = eval(test_string[i:len(test_string)-6])
                break
        #phrases = test_string.split('"')

        print(f'DEBUG: Il risultato e\' {res}')

    elif type_of_test == '<title> ART TEST </title>':
        test_string = str(soup.find('p'))
        for i in range(6, len(test_string)):
            if test_string[i].isupper():
                res = test_string[i:test_string.find('?')]
                break
        #phrases = test_string.split('"')

        print(f'DEBUG: phrases={test_string}')
        print(f'DEBUG: Il colore da stampare e\' {res}')


    return res, type_of_test, response.cookies

def POST_request(res, type_of_test, cookie):
    if type_of_test == '<title> GRAMMAR TEST </title>':
        response = requests.post(URL, data={'letter': res, 'submit': 'Submit'}, cookies=cookie)
        response.raise_for_status()

    elif type_of_test == '<title> MATH TEST </title>':
        response = requests.post(URL, data={'sum': res}, cookies=cookie)
        response.raise_for_status()

    elif type_of_test == '<title> ART TEST </title>':
        response = requests.post(URL, data={res:''}, cookies=cookie)
        response.raise_for_status()

    print(f'DEBUG: Status code={response.status_code}')

    POST_response = response.text
    cookie = response.cookies
    soup = BeautifulSoup(POST_response, 'html.parser')
    type_of_test = str(soup.find('title'))
    print(f'DEBUG: type_of_test={type_of_test}')
    
    if type_of_test == '<title> GRAMMAR TEST </title>':
        test_string = str(soup.find('p'))
        phrases = test_string.split('"')
        res = phrases[3].count(phrases[1])
        print(f'DEBUG: Ci sono n.{res} di {phrases[1]} in {phrases[3]}.')


    elif type_of_test == '<title> MATH TEST </title>':
        test_string = str(soup.find('p'))
        print(f'DEBUG: phrases={test_string}')

        for i in range(len(test_string)):
            if test_string[i].isdigit():
                print(f'DEBUG: da stampare {test_string[i:len(test_string)-6]}')
                res = eval(test_string[i:len(test_string)-6])
                break
        #phrases = test_string.split('"')

        print(f'DEBUG: Il risultato e\' {res}')

    elif type_of_test == '<title> ART TEST </title>':
        test_string = str(soup.find('p'))
        for i in range(6, len(test_string)):
            if test_string[i].isupper():
                res = test_string[i:test_string.find('?')]
                break
        #phrases = test_string.split('"')

        print(f'DEBUG: phrases={test_string}')
        print(f'DEBUG: Il colore da stampare e\' {res}')

    else:
        print(response.text)
        return None, None, None

    return res, type_of_test, cookie

def main():
    res, type_of_test, cookie = GET_request()
    i = 0
    while(True):
        if not type_of_test in ('<title> GRAMMAR TEST </title>', '<title> MATH TEST </title>', '<title> ART TEST </title>'):
            break

        res, type_of_test, cookie = POST_request(res, type_of_test, cookie)
    

if __name__ == '__main__':
    main()