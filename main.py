def rot90(matrix):
    return [list(reversed(col)) for col in zip(*matrix)]


def rot270(matrix):
    return [list(row) for row in list(zip(*matrix))[::-1]]


def big_sum(mas_a, mas_b):
    int_mas_a = int(''.join(map(str, mas_a)))
    int_mas_b = int(''.join(map(str, mas_b)))
    x = int_mas_a + int_mas_b
    mas_x = []
    while x > 0:
        mas_x.append(x % 10)
        x //= 10
    return mas_x


if __name__ == "__main__":
    a = [[1, 2], [3, 4]]
    print(rot90(a))
    print(rot270(a))
    x = [1, 2, 3]
    y = [3, 2, 1]
    print(big_sum(x,y))
    print(321+123)
