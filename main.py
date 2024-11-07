def rot90(matrix):
    return [list(reversed(col)) for col in zip(*matrix)]