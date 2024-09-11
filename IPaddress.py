def is_valid_ipv4(ip):
    
    parts = ip.split(".")
    
    if len(parts) != 4:
        return False
    
    for part in parts:
        if not part.isdigit():
            return False
        num = int(part)
        if num < 0 or num > 255:
            return False
        
    return True

# Input number of test cases
t = int(input())


while t > 0:
    ip = input().strip()
    if is_valid_ipv4(ip):
        print("YES")
    else:
        print("NO")
    t -= 1
