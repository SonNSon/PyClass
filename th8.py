password = input().strip()


cnt = 0
if len(password) < 10:
    print("False",end='')    
else:
    for char in password:
        if char.isdigit() == True:
            cnt += 1
        elif char.isalnum() == False:
            print("False", end = '')
            break

    if cnt < 2:
        print("False", end = '')
    else:
        print("True", end = '')
    
