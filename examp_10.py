a = int(input())
thaus = a // 100000 + (a // 10000) %10 + (a // 1000) %10
once = (a // 100) %10 + (a // 10) %10 + a % 10
if thaus == once:
    print('Счастливый')
else:
    print('Обычный')