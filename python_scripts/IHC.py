from pwn import remote

flag = ''

with remote('ihc.challs.olicyber.it', 34008) as r:
    line = r.recvline().decode().removesuffix('\n')
    print(line)
    line = r.recvline().decode().removesuffix('\n')
    print(line)
    line = r.recvline().decode().removesuffix('\n')
    print(line)
    line = r.recvline().decode().removesuffix('\n')
    print(line)
    r.sendline()
    line = r.recvline().decode().removesuffix('\n')

    while '}' not in flag:
        print(line)

        if 'risultato' in line and 'troncato' in line:
            res = int(eval(line.split('(troncato) ')[1].removesuffix('?')))
            print(res)
            r.sendline(str(res).encode())

        elif 'risultato' in line:
            res = eval(line.split(': ')[1].removesuffix('?'))
            print(res)
            r.sendline(str(res).encode())

        elif 'contrario' in line:
            res = line.split(': ')[1][::-1]
            print(res)
            r.sendline(res.encode())

        elif 'posizioni' in line:
            posi = eval(line.split('posizioni ')[1].split(' nella')[0])
            stringa = line.split('stringa ')[1].split('?')[0]

            res = ''.join([stringa[i-1] for i in posi])
            r.sendline(res.encode())

        elif 'compare' in line:
            lettera = line.split('lettera ')[1][0]
            stringa = line.split('stringa ')[1].split('?')[0]
            
            res = stringa.count(lettera)
            r.sendline(str(res).encode())

        line = r.recvline().decode().removesuffix('\n')
        flag += line[len(line) - 1]
        line = r.recvline().decode().removesuffix('\n')

    print(flag)
    