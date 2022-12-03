from pwn import remote
import json
import base64

if __name__ == '__main__':
    r = remote('based.challs.olicyber.it', 10600)
    r.recvlines(4)

    level = r.recvline().decode().removesuffix('\n')
    data = r.recvline().decode().removesuffix('\n')
    r.recvline()

    while True:
        x = json.loads(data)

        print(f'Level = {level}')
        print(f'Data = {data}')
        
        if level == 'Converti questo da binario!':
            s = ''

            #for c in x['message']:
            #    temp += c
            #    cont += 1
            #    if cont == 8:
            #        l.append(temp)
            #        temp = ''
            #        cont = 0
            i = 0
            while i < len(x['message']):
                temp = chr(int(x['message'][i:i+7], 2))
                if not temp.isalpha():
                    temp = chr(int(x['message'][i:i+8], 2))
                    i += 1

                s += temp
                i += 7


            #s = ''.join([chr(int(byt, 2)) for byt in l])
            #x = json.dumps({'answer': s})
            #r.sendline(x)

        elif level == 'Converti questo a binario (Senza lo 0b iniziale)!':
            l = [bin(ord(i)) for i in x['message']]
            s = ''
            for i in range(len(l)):
                temp = str(l[i])[2:]
                if i != 0: # and i != len(l) - 1:
                   temp = '0' + temp # '0' * (8 - len(temp))
                s += temp
            #s = ''.join([str(i)[2:] + '0' for i in l])
            #x = json.dumps({'answer': s})
            #r.sendline()

        elif level == 'Converti questo da esadecimale!':
            l = []
            for i in range(0, len(x['message']), 2):
                l.append(x['message'][i] + x['message'][i+1])

            s = ''.join([chr(int(i, 16)) for i in l])
            #x = json.dumps({'answer': s})
            #r.sendline()

        elif level == 'Converti questo a esadecimale! (Senza lo 0x iniziale)':
            l = [hex(ord(i)) for i in x['message']]
            s = ''.join(str(i)[2:] for i in l)
            

        elif level == 'Converti questo a base64!':
            s = base64.b64encode(x['message'].encode()).decode()

        elif level == 'Converti questo da base64!':
            s = base64.b64decode(x['message'].encode()).decode()

        else:
            exit(1)

        res = json.dumps({'answer': s})
        try:
            r.sendline(res.encode())
            ans = r.recvline()
            a = r.recvline()
            b = r.recvline()
            level = r.recvline().decode().removesuffix('\n')
            data = r.recvline().decode().removesuffix('\n')
            a = r.recvline()
        except EOFError:
            print(f'DEBUG: fine')
            print(a)
            print(b)
            print(level)
            print(data)
            exit(1)
