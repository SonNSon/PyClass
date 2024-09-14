def swap(n):
    str = ''
    if n[0] == '-':
        n = n[1:]
        str = '-' + n[-1] + n[1:-1] + n[0]
    else:
        str = n[-1] + n[1:-1] + n[0]
    return str
n = input()
print(swap(n), end = '')