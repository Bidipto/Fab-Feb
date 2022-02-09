mat= [
[3, 0, 6, 5, 0, 8, 4, 0, 0],
[5, 2, 0, 0, 0, 0, 0, 0, 0],
[2, 8, 7, 0, 0, 0, 0, 3, 1],
[0, 0, 3, 0, 1, 0, 0, 8, 0],
[9, 0, 0, 8, 6, 3, 0, 0, 5],
[0, 5, 0, 0, 9, 0, 6, 0, 0],
[1, 3, 0, 0, 0, 0, 2, 5, 0],
[0, 0, 0, 0, 0, 0, 0, 7, 4],
[0, 0, 5, 2, 0, 6, 3, 0, 0]]


def isValid(mat):
    N = 9
    for m in range(N):
        arr = set()
        for n in range(N):
            if mat[m][n] != 0:
                if mat[m][n] in arr:
                    return 0
                else:
                    arr.add(mat[m][n])
    for n in range(N):
        arr = set()
        for m in range(N):
            if mat[m][n] != 0:
                if mat[m][n] in arr:
                    return 0
                else:
                    arr.add(mat[m][n])
    for i in range(0, N, 3):
        for j in range(0, N, 3):
            arr = set()
            for m in range(i, i + 3):
                for n in range(j, j + 3):
                    if mat[m][n] != 0:
                        if mat[m][n] in arr:
                            return 0
                        else:
                            arr.add(mat[m][n])
    return 1

print(isValid(mat))