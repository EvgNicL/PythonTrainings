def getPass(start, end):
    dict_ = {}
    for i in range(start, end):
        v = ''
        for j in range(1, i):
            for c in range(j, i):
                if i % (c + j) == 0 and c != j:
                   v = v + str(j) + str(c)
        dict_[i] = v
    return dict_

def printPass(start, end):
    if isinstance(start, int) and isinstance(end, int):
        for key, value in getPass(start, end).items():
            print(f'{key}: {value}')

printPass(3, 21)