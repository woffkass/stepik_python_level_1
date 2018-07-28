genom = input()
genom = genom.upper()
count = 0
for i in genom:
    if i == 'C' or i == 'G':
        count += 1
result = count * 100 / len(genom)
print(result)