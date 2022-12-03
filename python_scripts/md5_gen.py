from hashlib import md5
from itertools import repeat
import multiprocessing as mp
#import random
#import pyautogui

#screen = pyautogui.screenshot()
#screen.save(r'C:/Users/mario/Desktop/screen.png')

alphabet = '0123456789abcdef'

#print(hashlib.md5(alphabet).hexdigest())


#n = 1

# while True:
#     s = ''
#     for _ in range(24):
#         s += random.choice(alphabet)
        
#     h = md5(s.encode()).hexdigest()[:24]
#     if s == h:
#         print(s)
#         screen = pyautogui.screenshot()
#         screen.save(r'C:/Users/mario/Desktop/screen1.png')
#         break
#     else:
#         #print(f'Iterazione n. {i} fallita con {s} != {h}')
#         if i == 100000:
#             print(f'Provate {n} * 100000 iterazioni')
#             n += 1
#             i = 0
#         else:
#             i += 1

# i = 0x100000000000000000000000

def finder(i, event):
    while True:
        hex_i = hex(i)[2:]
        md5_24dig = md5(bytes.fromhex(hex_i)).hexdigest()[:24]
        if md5_24dig == hex_i:
            print(f'Trovato! Stringa = {hex_i}')
            event.set()
            break

        i += 1

if __name__ == '__main__':
    li = [0x100000000000000000000000, 0x100000000100000000000000, 0x100002000000000000000000, 0x100000000050000000000000]
    m = mp.Manager()
    event = m.Event()

    with mp.Pool(processes=4) as pool:
        res = pool.starmap_async(finder, zip(li, repeat(event)))
        event.wait()
        event.clear()
        pool.terminate()