import multiprocessing as mp
from hashlib import sha256
from itertools import repeat

value = mp.Value('i', 0, lock=True)

def finder2(initial_i, first_six, event):
    i = initial_i
    while True:
        if i % 10000000 == 0:
            print("!!!")

        hex_i = hex(i)[2:]
        hex_i_adj = hex_i if (len(hex_i) % 2) == 0 else '0' + hex_i
        #print(f'DEBUG TEMPORANEO: i = {i}, hex = {hex_i_adj}')
        if sha256(bytes.fromhex(hex_i_adj)).hexdigest()[:6] == first_six:
            print(f'FOUND! = {hex_i_adj}')
            value.value = i
            event.set()
            return hex_i_adj.encode()

        i += 1

if __name__ == '__main__':
    first_6_hex = '9abf01'
    to_send = b''
    with mp.Pool(processes=4) as pool:
        m = mp.Manager()
        #value = m.Value('i', 0, lock=True)
        event = m.Event()
        value = m.list()
        l2 = [0, 10000000, 100000000, 1000000000]
        res = pool.starmap_async(finder2, zip(l2, repeat(first_6_hex), repeat(event)))
        #to_send = res.get()
        #pool.close()
        event.wait()
        #print(res)
        pool.terminate()
        event.clear()
        print()
        for el in res._value:
            if el is not None:
                v = el
        #print(hex_i_adj)