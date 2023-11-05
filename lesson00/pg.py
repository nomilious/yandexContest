n, m = map(int, input().split())

field = []
for _ in range(n):
    field.append(list(map(int,  input().split())))
_max = 0
for i in range(1, n):
    _max = max(_max, field[i][0])
    for j in range(1, m):
        if field[i][j] == 1:
            left = field[i-1][j]
            top = field[i][j-1]
            diagonal = field[i-1][j-1]
            field[i][j] +=min(left, top, diagonal)
            _max = max(_max, field[i][j])

print(_max, field)
