def unique_in_order(sequence) -> list:
    array = list(sequence)
    i = 0
    while i < len(array) - 1:
        if array[i] == array[i+1]:
            array.pop(i+1)
        else:
            i += 1
    return array

print(unique_in_order("AAAABBBCCDAABBB"))
