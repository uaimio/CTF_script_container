import requests

#b'\x69\x6e\x70\x75\x74\x3d
response = requests.get("http://soundofsilence.challs.olicyber.it/")
print(response.text)

response = requests.post("http://soundofsilence.challs.olicyber.it/", data={'input': b'\x00\x74'})
print(response.text)
