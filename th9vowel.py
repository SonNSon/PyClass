s = input().lower()

cnt = 0
for i in range(len(s)):
    if s[i] == 'a' or s[i] == 'e' or s[i] == 'i' or s[i] == 'o' or s[i] == 'u':
        cnt += 1
print(cnt, end = '')