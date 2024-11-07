def rot90(matrix):
    return [list(reversed(col)) for col in zip(*matrix)]


def rot270(matrix):
    return [list(row) for row in list(zip(*matrix))[::-1]]


if __name__ == "__main__":
    a = [[1, 2], [3, 4]]
    print(rot90(a))
    print(rot270(a))
