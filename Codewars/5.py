def find_uniq(arr):
    for i in range(len(arr)):
        if arr.index(arr[i]) > 0:
            
            if arr[0] != arr[1] and arr[0] != arr[2]:
                return arr[0]
            else:
                return arr[i]

# print(find_uniq([ 1, 1, 1, 2, 1, 1 ]))
# print(find_uniq([ 0, 0, 0.55, 0, 0 ]))
print(find_uniq([ 1, 3, 3, 3, 3 ]))