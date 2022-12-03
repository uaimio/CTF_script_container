def sign(n):
    if n > 0:
        return True
    elif n < 0:
        return False
    else:
        raise Exception

def divide(dividend, divisor):
    if dividend == 0:
        return 0
    
    minus = sign(dividend) ^ sign(divisor)
    dividend = abs(dividend)
    divisor = abs(divisor)

    res = 0
    while dividend >= divisor:
        dividend -= divisor
        res += 1

    return -res if minus else res

print(divide(3, 2))