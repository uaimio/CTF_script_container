def otp(lines: list):
    for i in range(100):
        try:
            flag = True

            for l in lines:
                if not chr(l[0] - i).isascii():
                    flag = False
                

            if flag:
                print(chr(lines[0][0] - i), chr(lines[1][0] - i), chr(lines[2][0] - i), chr(lines[3][0] - i), chr(lines[4][0] - i), chr(lines[5][0] - i), chr(lines[6][0] - i), chr(lines[7][0] - i), chr(lines[8][0] - i))

        except ValueError:
            print('Situazione non ammessa 1')

    print()

    for i in range(180):
        try:
            flag = True

            for l in lines:
                if not chr(l[1] - i).isascii():
                    flag = False
                

            if flag:
                print(chr(lines[0][1] - i), chr(lines[1][1] - i), chr(lines[2][1] - i), chr(lines[3][1] - i), chr(lines[4][1] - i), chr(lines[5][1] - i), chr(lines[6][1] - i), chr(lines[7][1] - i), chr(lines[8][1] - i))
                

        except ValueError:
            print('Situazione non ammessa 2')

    print()

    for i in range(200):
        try:
            flag = True

            for l in lines:
                if l[2] - i < 32 or l[2] - i > 94:
                    flag = False
                
            if flag:
                for j in range(9):
                    print(chr(lines[j][2] - i), end='')

                print()
                

        except ValueError:
            print('Situazione non ammessa 3')


def otp1(lines: list):
    elements = list()
    for x in range(5):
        for i in range(0xFF):
            chars = [chr((lines[k][x] - i) % 0xFF) for k in range(9)] #if lines[k][x] - i >= 33]
            #for k in range(9)
            
            if len(chars) < 5:
                continue

            if 'f' in chars and x == 0:
                elements.append((chars, f'x={x}, i={i}'))

            elif 'l' in chars and x == 1:
                elements.append((chars, f'x={x}, i={i}'))

            elif 'a' in chars and x == 2:
                elements.append((chars, f'x={x}, i={i}'))

            elif 'g' in chars and x == 3:
                elements.append((chars, f'x={x}, i={i}'))

            elif '{' in chars and x == 4:
                elements.append((chars, f'x={x}, i={i}'))

    return elements


def otp2(lines: list):
    for i in range(255):
        for j in range(9):
            if not chr(lines[j][0] ^ i).isascii():
                break
            if j == 8:
                print(i)
                print(chr(lines[0][0] ^ i))
                print(chr(lines[1][0] ^ i))
                print(chr(lines[2][0] ^ i))
                print(chr(lines[3][0] ^ i))
                print(chr(lines[4][0] ^ i))
                print(chr(lines[5][0] ^ i))
                print(chr(lines[6][0] ^ i))
                print(chr(lines[7][0] ^ i))
                print(chr(lines[8][0] ^ i))
                print("------------------")



if __name__ == '__main__':
    lines = []

    f = open('output.txt', 'r')
    for l in f.readlines():
        lines.append([int(l[i:i+2], 16) for i in range(0, len(l), 2) if l[i:i+2] != '\n'])
    #except FileNotFoundError:
    #    print
    #    exit(1)

        
    #for l in lines:
    #    print(l)
        
        #otp(f)
    #for l in otp1(lines):
    #    print(l)

    otp2(lines)