n = int(input())
lst = {}
i = 0
while i < n:
    key = int(input())
    if key not in lst:
        lst[key] = key#f(key)
    print(lst[key])
    i += 1