#!/bin/env python3

# pip3 install pwntools
from pwn import remote, context

def access(d, i, j):
    try:
        ret = d[i][j]
    except KeyError:
        ret = 0
    finally:
        return ret

def lista_unica(pulsanti):
    l = []
    for p in pulsanti:
        for o in p:
            l.append(o)

    return l

def solv1(contatori, pulsanti):
    #TODO: da implementare
    pulsanti.sort(key=lambda l:len(l), reverse=True)
    print(f'DEBUG:{pulsanti}')

    lu = lista_unica(pulsanti)
    l_index = {}
    ret = ''

    print(f'DEBUG: lista unica {lu}')

    for i in range(len(pulsanti)):
        for j in range(len(pulsanti[i])):
            try:
                ind = lu.index(pulsanti[i][j], l_index[pulsanti[i][j]])
                l_index[pulsanti[i][j]] = ind
            except (ValueError, KeyError):
                if contatori[pulsanti[i][j]] < 5:
                    ret += f'{str(pulsanti[i][j])} '
                    contatori[pulsanti[i][j]] += 1

    print(f'DEBUG: {ret}')
    return ret.encode()

def solve(contatori, pulsanti):
    s = ''
    for i in range(len(pulsanti)):
        if contatori[pulsanti[i][0]] < 5:
            s += f'{i + 1} ' * (5 - contatori[pulsanti[i][0]])

    s = s[:len(s)-1]
    return s.encode()

if __name__ == '__main__':
    r = remote("test.challs.olicyber.it", 15004)
    context.log_level = 'debug'
    r.recvlines(20)

    livello = r.recvline()
    while livello.startswith(b"Livello"):
        stato = [int(_) for _ in r.recvline(False).decode().split()]
        mosse = []
        while True:
            s = r.recvline(False).decode()
            if s == "":
                break
            mosse.append(["ABCDEFGHIJKLMNOPQRSTUVWXYZ".index(_) for _ in s.split()])
        res = solve(stato, mosse)
        r.sendline(res)
        r.recvlines(2)
        livello = r.recvline()