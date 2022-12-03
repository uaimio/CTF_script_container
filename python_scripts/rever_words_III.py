def reverseWords(s: str) -> str:
    li = s.split(' ')
    return ' '.join(l[::-1] for l in li)

print(reverseWords('cane con la droga'))