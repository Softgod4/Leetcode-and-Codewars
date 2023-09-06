def count_smileys(arr) -> int:
    countsmile = 0
    for smiles in range(len(arr)):
        if arr[smiles][0] == ';' or arr[smiles][0] == ':':
            if arr[smiles][1] == '~' or arr[smiles][1] == '-':
                if arr[smiles][2] == 'D' or arr[smiles][2] == ')':
                    countsmile += 1
            elif arr[smiles][1] == 'D' or arr[smiles][1] == ')':
                countsmile += 1
    return countsmile

print(count_smileys([':D',':~)',';~D',':)']))