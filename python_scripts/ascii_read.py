with open('dashed.txt', 'r') as f:
    elems = f.readline().split(',')

    l = list()
    i = 0
    j = 0
    for el in elems:
        try:
            if i == 0:
                l.append(chr(int(el, 16)))
                i += 1
            elif i == 7:
                l[j] += chr(int(el, 16))
                #l.append(chr(int(el, 16)))
                i = 0
                j += 1
            else:
                l[j] += chr(int(el, 16))
                i += 1
        except ValueError:
            print(l)
            print([chr(int(i,2)) for i in l])

        s = str()
        for oo in l:
            s += chr(int(oo, 2))
        print(s)
