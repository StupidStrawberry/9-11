def rot90(matrix):
    return [list(reversed(col)) for col in zip(*matrix)]


def rot270(matrix):
    return [list(row) for row in list(zip(*matrix))[::-1]]


def big_sum(mas_a, mas_b):
    int_mas_a = int(''.join(map(str, mas_a)))
    int_mas_b = int(''.join(map(str, mas_b)))
    z = int_mas_a + int_mas_b
    mas_x = []
    while z > 0:
        mas_x.append(z % 10)
        z //= 10
    mas_x.reverse()
    return mas_x


def big_diff(mas_a, mas_b):
    int_mas_a = int(''.join(map(str, mas_a)))
    int_mas_b = int(''.join(map(str, mas_b)))
    z = int_mas_a - int_mas_b
    mas_x = []
    while z > 0:
        mas_x.append(z % 10)
        z //= 10
    mas_x.reverse()
    return mas_x


if __name__ == "__main__":
    a = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    print(rot90(a))
    print(rot270(a))
    x = [1, 2, 3]
    y = [3, 2, 1]
    print(big_sum(x, y))
    print(321+123)
    print(big_diff(y, x))
    print(321 - 123)
