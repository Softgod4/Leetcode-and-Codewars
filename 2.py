def scramble(s1, s2):
    sortarray = []
    for i in range(len(s1)):
        for a in range(len(s2)):
            if s2[a] == s1[i]:
                sortarray.append(s2[a])
                break
    return sortarray

print(scramble('katas', 'steak'))