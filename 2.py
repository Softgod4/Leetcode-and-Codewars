def scramble(s1, s2) -> bool:
    lists2 = list(s2)
    for i in range(len(s1)):
        for a in range(len(lists2)):
            if lists2[a] == s1[i]:
                lists2.pop(a)
                print(lists2)
                if IndexError:
                    return False
    return True

print(scramble('katas', 'steak')) #False
print(scramble('scriptingjava', 'javascript')) #True
