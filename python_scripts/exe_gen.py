with open('hexdump.txt', 'r') as f_dump:
    f_exe = open('hexdump.dat', 'wb')
    for line in f_dump:
        #line = line.replace(' ', '')[40:]
        #line = line.strip()
        #line = line.replace('|', '')
        nl = line[:8] + ': ' + line[10:12] + line[13:15] + ' ' + line[16:18] + line[19:21] + \
            ' ' + line[22:24] + line [25:27] + ' ' + line[28:30] + line[31:33] + ' ' + \
            line[35:37] + line[38:40] + ' ' + line[41:43] + line[44:46] + ' ' + \
            line[47:49] + line[50:52] + ' ' + line[53:55] + line[56:58] + '  ' + \
            line[61:77] + '\n'

        print(nl)
        f_exe.write(nl.encode())

    f_exe.close()