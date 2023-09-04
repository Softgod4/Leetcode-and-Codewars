# def move_zeros(lst):
#     arraynum = 0
#     for nul in lst:
#         if nul == 0:
#             lst.remove(nul)
#             arraynum += 1

#     for i in range(arraynum):
#         lst.append(0)
#     return lst          

# print(move_zeros([1, 0, 1, 0]))

# def move_zeros(lst):
#     arraynum = 0
#     for i in range(len(lst)):
#         if i < len(lst) and lst[i] == 0:
#             lst.pop(i)
#             arraynum += 1

#     for i in range(arraynum):
#         lst.append(0)
#     return lst

# print(move_zeros([9, 0, 9, 1, 2, 1, 1, 3, 1, 9, 0, 0, 9, 0, 0, 0, 0, 0, 0, 0] ))

def move_zeros(lst) -> int:
    arrraynum = []
    nulcout = 0
    for num in lst:
        if num != 0:
            arrraynum.append(num)
        else:
            nulcout += 1

    for i in range(nulcout):
        arrraynum.append(0)
        
    return arrraynum

print(move_zeros([9, 0, 9, 1, 2, 1, 1, 3, 1, 9, 0, 0, 9, 0, 0, 0, 0, 0, 0, 0] ))



