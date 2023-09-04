def solution(s):
    lists = list(s)
    for i in range(len(lists)):
        if lists[i] == lists[i].upper():
            s.insert(i, ' ')
    return lists
    
print(solution("breakCamelCase"))