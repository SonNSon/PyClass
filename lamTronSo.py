def lam_tron_so(N):
    power = 10  
    while N > power:
        
        if (N % power) >= (power // 2):
            N = (N // power) * power + power 
        else:
            N = (N // power) * power 
        power *= 10  
    return N


t = int(input())  
for _ in range(t):
    N = int(input())  
    print(lam_tron_so(N))  
