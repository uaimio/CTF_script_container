from pwn import remote
from hashlib import sha256


def finder1(init_i, first_six, d):
    i = init_i
    while True:
        if i % 10000000 == 0:
            print("!!!")
        hex_i = hex(i)[2:]
        hex_i_adj = hex_i if (len(hex_i) % 2) == 0 else '0' + hex_i
        sha6 = sha256(bytes.fromhex(hex_i_adj)).hexdigest()[:6]
        if sha6 not in d:
            d[sha6] = hex_i_adj.encode()
        if sha6 == first_six:
            return i, hex_i_adj.encode()

        i += 1

def dict_builder(n, d):
    for i in range(n):
        hex_i = hex(i)[2:]
        hex_i_adj = hex_i if (len(hex_i) % 2) == 0 else '0' + hex_i
        sha6 = sha256(bytes.fromhex(hex_i_adj)).hexdigest()[:6]
        if sha6 not in d:
            d[sha6] = hex_i_adj.encode()

if __name__ == '__main__':
    n = 100000000
    d = dict()
    print(f'Costruzione del dizionario con n={n} elementi.')
    dict_builder(n, d)
    print('Dizionario costruito.')
    print('Proviamo ad accedere con questi elementi, se ne generano altri se necessario.')

    with remote('pow.challs.olicyber.it', 12209) as r:
        line = r.recvline().decode().removesuffix('\n')
        while line[0] == 'G':
            print(line)
            first_6_hex = line[len(line)-6:]
            if first_6_hex in d:
                to_send = d[first_6_hex]
            else:
                n, to_send = finder1(n, first_6_hex, d)
            print(f'TO_SEND:{to_send}, I:{n}')
            r.sendline(to_send)
            line = r.recvline().decode().removesuffix('\n')

        print(line)

    
