n = int(input())
list_n = list(range(n))
matrix = []
for i in range(n):
    row = []
    for j in range(n):
        row.append(1)
    matrix.append(row)


def darts(list_n, start):
    if len(list_n) > 0:
        for i in list_n:
            for j in list_n:
                matrix[i][j] = start
        if len(list_n) > 1:
            del list_n[0]
            del list_n[-1]
        else:
            del list_n[0]
        darts(list_n, start + 1)


darts(list_n, 1)

for i in matrix:
    print(i)
