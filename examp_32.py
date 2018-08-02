lst = {}
m = 0
ms = ''
with open('dataset_3363_3.txt') as inf:
    for line in inf:
        line = line.strip().lower()

        for w in line.split():
            if w in lst:
                lst[w] += 1
            else:
                lst[w] = 1
            if m < lst[w]:
                m = lst[w]
                ms = w
            elif m == lst[w] and ms > w:
                m = lst[w]
                ms = w
            print(ms, m)
