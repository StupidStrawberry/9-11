import random


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
    mas_x.reverse()
    return mas_x


def big_diff(mas_a, mas_b):
    int_mas_a = int(''.join(map(str, mas_a)))
    int_mas_b = int(''.join(map(str, mas_b)))
    x = int_mas_a - int_mas_b
    mas_x = []
    while x > 0:
        mas_x.append(x % 10)
        x //= 10
    mas_x.reverse()
    return mas_x


def how_much_same(mas_a, mas_b):
    k = 0
    for i in range(len(mas_a)):
        a = abs(mas_a[i])
        for j in range(len(mas_b)):
            b = abs(mas_b[j])
            if a == b:
                k += 1
    return k


def get_arr(lenght):
    a = []
    for i in range(lenght):
        a.append(int(input()))
    return a


def gen_arr(lenght):
    a = []
    for i in range(lenght):
        a.append(random.randint(0, 9))
    return a


def get_matrix(lenght, wight):
    a = []
    for i in range(lenght):
        b = []
        for j in range(wight):
            b.append(int(input()))
        a.append(b)
    return a


def gen_matrix(lenght, wight):
    a = []
    for i in range(lenght):
        b = []
        for j in range(wight):
            b.append(random.randint(0, 9))
        a.append(b)
    return a


def gen_or_get_mas():
    print("Желаете ввести массив в ручную? y/n \n В случае отказа массив будет сгенерирован случайно")
    ch = input()
    if ch == 'y':
        print("Введите длинну массива")
        lenght = int(input())
        return get_arr(lenght)
    elif ch == 'n':
        print("Введите длинну массива")
        lenght = int(input())
        return gen_arr(lenght)
    else:
        print("Неверные данные")


def gen_or_get_mat():
    print("Желаете ввести матрицу в ручную? y/n \n В случае отказа матрица будет сгенерирована случайно")
    ch = input()
    if ch == 'y':
        print("Введите длинну матрицы")
        lenght = int(input())
        print("Введите ширину матрицы")
        width = int(input())
        return get_matrix(lenght,width)
    elif ch == 'n':
        print("Введите длинну матрицы")
        lenght = int(input())
        print("Введите ширину матрицы")
        width = int(input())
        return gen_matrix(lenght,width)
    else:
        print("Неверные данные")



if __name__ == "__main__":
    print(gen_or_get_mas())
    print(gen_or_get_mat())
