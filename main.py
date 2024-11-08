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
    minus = 0
    if x < 0:
        x = abs(x)
        minus = 1
    while x > 0:
        mas_x.append(x % 10)
        x //= 10
    mas_x.reverse()
    if minus:
        mas_x[0] = mas_x[0]*(-1)
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


def menu(point):
    if point == 1:
        mas_a = gen_or_get_mas()
        mas_b = gen_or_get_mas()
        print("Сумма (1) или разность (2)")
        x = int(input())
        if x == 1:
            print(big_sum(mas_a, mas_b))
        elif x== 2:
            print(big_diff(mas_a, mas_b))
        else:
            print("Error")
    elif point == 2:
        mat = gen_or_get_mat()
        print("Повернуть матрицу на право (1) или на лево (2)")
        x = int(input())
        if x == 1:
            print(rot90(mat))
        elif x == 2:
            print(rot270(mat))
        else:
            print("Error")
    elif point == 3:
        mas_a = gen_or_get_mas()
        mas_b = gen_or_get_mas()
        print(how_much_same(mas_a, mas_b))
    elif point == 4:
        exit()
    else:
        print("Error")


if __name__ == "__main__":
    while True:
        print("Задачи\n 1. Входные данные: 2 массива с числами одинакового размера. Нужно произвести сумму чисел из массивов, первый массив должен быть отсортирован в порядке убывания, второй в порядке возрастания. Если числа в массивах совпадают, их сумма будет равна нулю. Конечный массив нужно отсортировать в порядке возрастания.\n2. Входные данные: матрица N на M. Требуется повернуть матрицу на 90 градусов против часовой или по часовой.\n 3. Входные данные: 2 массива с цифрами, каждый представляет собой большое число. Нужно произвести сумму или разность массивов. 4. Закончить работу программы")
        print("Выберите пункт меню")
        menu(int(input()))
