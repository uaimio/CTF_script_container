def isBadVersion(version) -> bool:
    if version > 3:
        return True
    else:
        return False

def firstBadVersion(n: int) -> int:
    if n == 1:
        return 1

    t = int(n / 2)
    while True:
        if isBadVersion(t) and not isBadVersion(t-1):
            return t
        elif isBadVersion(t) and isBadVersion(t-1):
            t = int(t / 2)
        elif not isBadVersion(t):
            t += int(t / 2)
        else:
            print('Condizione non ammessa')
            raise Exception

def firstBadVersion1(n: int) -> int:
    from random import randrange

    prev_i_inf = 1
    prev_i_sup = n

    while True:
        if prev_i_inf == prev_i_sup:
            return prev_i_sup

        i = randrange(prev_i_inf, prev_i_sup, 1)
        
        if not isBadVersion(i) and isBadVersion(i + 1):
            return i + 1
        elif isBadVersion(i):
            prev_i_sup = i
        elif not isBadVersion(i):
            prev_i_inf = i
        else:
            print('Condizione non ammessa')
            raise Exception

print(firstBadVersion(5))
print(firstBadVersion1(5))

