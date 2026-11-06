def read_int(prompt, min_value=None, max_value=None):
    while True:
        try:
            value = int(input(prompt))

            if min_value is not None and value < min_value:
                print(f"Ошибка ввода данных! Минимальное значение {min_value}.")
                continue
            if max_value is not None and value > max_value:
                print(f"Ошибка ввода данных! Максимальное значение {max_value}.")
                continue

            return value
        except ValueError:
            print("Ошибка! Введите целое число.")



def read_filename():
    while True:
        filename = input("Введите имя выходного файла: ").strip()

        if filename.endswith(".pgm") and filename.count(".") == 1 and filename.split(".")[0].strip() != "":
            return filename
        print("Ошибка! Введите корректное имя файла.")


def valid_user_input_resolution():
    height = read_int("Введите высоту изображения: ", 1)
    width = read_int("Введите ширину изображения: ", 1)

    return height, width

def valid_user_input_center():
    cx = read_int("Введите координату центра cx: ")
    cy = read_int("Введите координату центра cy: ")

    return cx, cy

def read_point(prompt):
    while True:
        try:
            x, y = map(int, input(prompt).split())
            return x, y
        except ValueError:
            print("Ошибка! Введите ровно две целые координаты через пробел.")


def valid_user_input_square():
    height, width = valid_user_input_resolution()
    cx, cy = valid_user_input_center()
    side = read_int("Введите длину стороны: ", 1)
    v_shape = read_int("Введите яркость квадрата: ", 0, 255)
    v_bg = read_int("Введите яркость фона: ", 0, 255)
    filename = read_filename()

    return height, width, cx, cy, side, v_shape, v_bg, filename


def valid_user_input_nested_square():
    height, width = valid_user_input_resolution()
    cx, cy = valid_user_input_center()
    side = read_int("Введите длину стороны: ", 1)
    N = read_int("Введите количество квадратов: ", 1)
    d = read_int("Введите шаг вложенности: ", 1)
    v_start = read_int("Введите начальную яркость: ", 0, 255)
    v_end = read_int("Введите конечную яркость: ", 0, 255)
    v_bg = read_int("Введите яркость фона: ", 0, 255)
    filename = read_filename()

    return height, width, cx, cy, side, N, d, v_start, v_end, v_bg, filename


def valid_user_input_line_segment():
    height, width = valid_user_input_resolution()
    x0, y0 = read_point("Введите координаты начала отрезка (через пробел): ")
    x1, y1 = read_point("Введите координаты конца отрезка (через пробел): ")
    v_line = read_int("Введите яркость линии: ", 0, 255)
    v_bg = read_int("Введите яркость фона: ", 0, 255)
    filename = read_filename()

    return height, width, x0, y0, x1, y1, v_line, v_bg, filename


def valid_user_input_circle():
    height, width = valid_user_input_resolution()
    radius = read_int("Введите радиус: ", 1)
    cx, cy = valid_user_input_center()
    v_center = read_int("Введите центральную яркость: ", 0, 255)
    v_edge = read_int("Введите яркость на границе: ", 0, 255)
    v_bg = read_int("Введите яркость фона: ", 0, 255)
    filename = read_filename()

    return height, width, radius, cx, cy, v_center, v_edge, v_bg, filename

