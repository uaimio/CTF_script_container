import pytesseract
import requests
from bs4 import BeautifulSoup

URL = "http://captcha.challs.olicyber.it/"

def recognize_text():
    text = pytesseract.image_to_string('test.png')
    return text.strip()

def GET_request():
    response = requests.get(URL)
    response.raise_for_status()

    GET_response = response.text
    soup = BeautifulSoup(GET_response, 'html.parser')
    relative_image_link = str(soup.find('img'))[25:89]
    print(f'DEBUG: Relative image link={relative_image_link}')
    response_img = requests.get(URL + relative_image_link)
    fb = open("test.png", "wb")
    fb.write(response_img.content)
    fb.close()

    print(f'DEBUG: {recognize_text()}')
    return recognize_text(), response.cookies

def POST_request(rec_text, cookie, i):
    response = requests.post(URL + "next", data={'risposta': rec_text}, cookies=cookie)
    response.raise_for_status()

    print(f'DEBUG: Status code={response.status_code}')

    POST_response = response.text
    soup = BeautifulSoup(POST_response, 'html.parser')
    if i >= 99:
        print(soup)
        
    relative_image_link = str(soup.find('img'))[25:89]
    print(f'DEBUG: Relative image link={relative_image_link}')
    response_img = requests.get(URL + relative_image_link)
    fb = open("test.png", "wb")
    fb.write(response_img.content)
    fb.close()
    
    POST_index = str(soup.find('i'))
    print(POST_index)

    return recognize_text(), response.cookies


def main():
    recognized_text, cookie = GET_request()
    for i in range(100):
        print(i)
        recognized_text, cookie = POST_request(recognized_text, cookie, i)
    

if __name__ == '__main__':
    main()
