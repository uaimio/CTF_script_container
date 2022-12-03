def timeConversion(s):
    h = s[:2]
    meridian = s[8]

    if h == '12':
        h = '00'

    if meridian == 'A':
        return h + s[2:8]
    else:
        return str(int(h) + 12) + s[2:8]
        
if __name__ == '__main__':
    result = timeConversion('07:05:45PM')
    print(result)