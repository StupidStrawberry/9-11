def rot90(matrix):
    return [list(reversed(col)) for col in zip(*matrix)]


def rot270(matrix):
    return [list(row) for row in list(zip(*matrix))[::-1]]