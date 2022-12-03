from pwn import remote
from hashlib import sha256
from itertools import repeat
import multiprocessing as mp


def finder(initial_i, first_six, event, rl, dl):
    i = initial_i
    while True:
        if i % 10000000 == 0:
            print("!!!")

        hex_i = hex(i)[2:]
        hex_i_adj = hex_i if (len(hex_i) % 2) == 0 else '0' + hex_i
        sha6 = sha256(bytes.fromhex(hex_i_adj)).hexdigest()[:6]
        if sha6 not in dl:
            dl[sha6] = hex_i_adj.encode()
        #print(f'DEBUG TEMPORANEO: i = {i}, hex = {hex_i_adj}')
        if sha6 == first_six:
            print('FOUND')
            event.set()
            rl.append(hex_i_adj.encode())
            return hex_i_adj.encode()

        i += 1        

if __name__ == '__main__':
    with remote('pow.challs.olicyber.it', 12209) as r:
            m = mp.Manager()
            event = m.Event()
            rl = m.list()
            dl = m.dict()
            li = [0, 10000000, 100000000, 1000000000 ]#, 10000000000, 100000000000, 1000000000000, 1000000000000]

            line = r.recvline().decode().removesuffix('\n')
            while line[0] == 'G':
                print(line)
                first_6_hex = line[len(line)-6:]
                
                if first_6_hex in dl:
                    to_send = dl[first_6_hex]
                else:
                    with mp.Pool(processes=4) as pool:
                        res = pool.starmap_async(finder, zip(li, repeat(first_6_hex), repeat(event), repeat(rl), repeat(dl)))
                        event.wait()
                        event.clear()
                        pool.terminate()

                        #for el in res._value:
                        #    if el is not None:
                        #        to_send = el

                        if len(rl) > 0:
                            to_send = rl[0]
                            del rl[:]

                print(to_send)
                r.sendline(to_send)
                line = r.recvline().decode().removesuffix('\n')

            print(line)

    
