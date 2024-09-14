def count(lst):
    num = []
    cnt = []
    for i in lst:
        if i not in num:
            num.append(i)
            cnt.append(1)
        else:
            cnt[num.index(i)] += 1
    return num, cnt
lst = [int(x) for x in input().split()]
num, cnt = count(lst)
print(tuple(num),end=' ')
print(tuple(cnt))


