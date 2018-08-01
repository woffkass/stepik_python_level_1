def modify_list(lst):
    i = 0
    while i < len(lst):
        #print(lst)
        #print(i)
        if lst[i] % 2 == 0:
            #print(lst[i])
            lst[i] = lst[i] // 2
            #print(lst[i])
            i += 1
        else:
            del lst[i]
lst = [1, 2, 3, 4, 5, 6]
print(modify_list(lst))  # None
print(lst)               # [1, 2, 3]
modify_list(lst)
print(lst)               # [1]

lst = [10, 5, 8, 3]
modify_list(lst)
print(lst)               # [5, 4]