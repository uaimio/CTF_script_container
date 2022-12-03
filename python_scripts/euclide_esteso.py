def euclide_esteso(a, b):
    r0 = a
    r1 = b
    s0 = 1
    s1 = 0
    t0 = 0
    t1 = 1


    while True:
        q = r0 // r1
        ri1 = r0 - q * r1

        if ri1 == 0:
            return r1, s1 % b, t1 % a

        si1 = s0 - q * s1
        ti1 = t0 - q * t1

        r0 = r1
        r1 = ri1
        s0 = s1
        s1 = si1
        t0 = t1
        t1 = ti1



if __name__ == '__main__':
    print(euclide_esteso(40, 15))
    print(euclide_esteso(38, 15))
    print(euclide_esteso(149, 256))

