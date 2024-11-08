from concurrent.futures import ThreadPoolExecutor
import funcs

def menu(point):
    """
    Основное меню программы.

    :param point: Пункт меню, выбранный пользователем.
    """
    if point == 1:
        mas_a = funcs.gen_or_get_mas()
        mas_b = funcs.gen_or_get_mas()
        print("Сумма (1) или разность (2)")
        x = int(input())
        if x == 1:
            print(funcs.big_sum(mas_a, mas_b))
        elif x == 2:
            print(funcs.big_diff(mas_a, mas_b))
        else:
            print("Error")
    elif point == 2:
        with ThreadPoolExecutor() as executor:
            a = executor.submit(funcs.gen_or_get_mat)
            mat = a.result()
        print("Повернуть матрицу на право (1) или на лево (2)")
        x = int(input())
        if x == 1:
            print(funcs.rot90(mat))
        elif x == 2:
            print(funcs.rot270(mat))
        else:
            print("Error")
    elif point == 3:
        mas_a = funcs.gen_or_get_mas()
        mas_b = funcs.gen_or_get_mas()
        print(funcs.how_much_same(mas_a, mas_b))
    elif point == 4:
        exit()
    else:
        print("Error")


if __name__ == "__main__":
    while True:
        print(
            "Задачи\n 1. Входные данные: 2 массива с числами одинакового размера. Нужно произвести сумму чисел из массивов, первый массив должен быть отсортирован в порядке убывания, второй в порядке возрастания. Если числа в массивах совпадают, их сумма будет равна нулю. Конечный массив нужно отсортировать в порядке возрастания.\n2. Входные данные: матрица N на M. Требуется повернуть матрицу на 90 градусов против часовой или по часовой.\n 3. Входные данные: 2 массива с цифрами, каждый представляет собой большое число. Нужно произвести сумму или разность массивов.\n4. Закончить работу программы")
        print("Выберите пункт меню")
        menu(int(input()))
