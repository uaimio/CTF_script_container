import requests

header = {'Accept': 'text/html; charset=UTF-8', 'Accept-Encoding': 'gzip, deflate', 'user-agent': 'chrome'}

resp = requests.get('http://confuse-me.challs.olicyber.it', params=f'input={0x0}', headers=header)
print(resp)
print(resp.headers)
print(resp.content)

