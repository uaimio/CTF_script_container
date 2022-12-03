from hashlib import sha256

with open("C:/Users/mario/Desktop/ct.txt", "r") as f:
    lines = f.readlines()
    s = ''
    for line in lines:
        for i in range(33, 247):
            if sha256(chr(i).encode()).hexdigest() == line.removesuffix('\n'):
                s += chr(i)

    print(s)