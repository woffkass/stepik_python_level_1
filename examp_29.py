s = input().lower()
lst = {}
for w in s.split():
    if w in lst:
        lst[w] += 1
    else:
        lst[w] = 1
for key, value in lst.items():
    print(key, value)