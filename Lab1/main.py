"""
Лабораторная работа 
«Генерация растровых изображений в формате PGM P2 на Python»
Корнилов Арсений Сергеевич М30-113БВ-26
"""

from validation_user_input import (
    read_int,
    valid_user_input_square,
    valid_user_input_nested_square,
    valid_user_input_line_segment,
    valid_user_input_circle
)


def print_menu():
    menu_buttons = [
        '=== ГЕНЕРАТОР PGM P2 ===\n'
        '1. Квадрат по центру и стороне\n'
        '2. Вложенные квадраты\n'
        '3. Отрезок по двум точкам\n'
        '4. Круг с радиальным градиентом\n'
        '0. Выход\n'
        '========================'
    ]
    return menu_buttons

def valid_user_input_menu():
    choice = read_int("Выберите пункт меню: ", 0, 4)
    return choice

def save_file(filename, image):
    width = len(image[0])
    height = len(image)

    with open(filename, "w") as file:
        file.write("P2\n")
        file.write(f"{width} {height}\n")
        file.write("255\n")

        for row in image:
            file.write(" ".join(map(str, row)) + "\n")
    print(f"Сохранено: {filename} ({width}x{height})")


def draw_square(image, cx, cy, side, v_shape):
    height = len(image)
    width = len(image[0])

    half = side // 2

    x_min = cx - half
    x_max = x_min + side - 1

    y_min = cy - half
    y_max = y_min + side - 1

    for x in range(x_min, x_max + 1):
        if 0 <= x < width:
            if 0 <= y_min < height:
                image[y_min][x] = v_shape

            if 0 <= y_max < height:
                image[y_max][x] = v_shape

    for y in range(y_min, y_max + 1):
        if 0 <= y < height:
            if 0 <= x_min < width:
                image[y][x_min] = v_shape

            if 0 <= x_max < width:
                image[y][x_max] = v_shape


def filled_image(height, width, v_bg):
    image = []

    for y in range(height):
        row = []
        for x in range(width):
            row.append(v_bg)
        image.append(row)
    return image

def print_image_info(title, width, height, filename):
    print(f"\n--- {title} ---")
    print(f"Ширина изображения: {width}")
    print(f"Высота изображения: {height}")
    print(f"Имя выходного файла: {filename}")

def square_center_side(height, width, cx, cy, side, v_shape, v_bg, filename):
    print("Квадрат по центру и стороне")
    image = filled_image(height, width, v_bg)

    draw_square(image, cx, cy, side, v_shape)

    print_image_info(
        "Квадрат по центру и стороне",
        width, height, filename
    )

    print(f"Центр cx: {cx}")
    print(f"Центр cy: {cy}")
    print(f"Сторона: {side}")
    print(f"Яркость квадрата (0..255): {v_shape}")
    print(f"Яркость фона (0..255): {v_bg}")

    save_file(filename=filename, image=image)
    print()

def nested_squares(height, width, cx, cy, side, N, d, v_start, v_end, v_bg, filename):
    print_image_info(
        "Вложенные квадраты",
        width, height, filename
    )

    print(f"Центр cx: {cx}")
    print(f"Центр cy: {cy}")
    print(f"Начальная сторона: {side}")
    print(f"Количество квадратов: {N}")
    print(f"Шаг уменьшения стороны: {d}")
    print(f"Начальная яркость: {v_start}")
    print(f"Конечная яркость: {v_end}")
    print(f"Яркость фона (0..255): {v_bg}")

    image = filled_image(height, width, v_bg)

    for i in range(N):
        side_i = side - 2 * i * d

        if side_i <= 0:
            break

        if N > 1:
            t = i / (N - 1)

        if N == 1:
            v_i = v_start
        else:
            v_i = round(v_start + (v_end - v_start) * t)
        draw_square(image, cx, cy, side_i, v_i)

    save_file(filename=filename, image=image)
    print()


def line_segment(height, width, x0, y0, x1, y1, v_line, v_bg, filename):
    image = filled_image(height, width, v_bg)

    print_image_info(
        "Отрезок по двум точкам",
        width, height, filename
    )

    print(f"Начальная точка: ({x0}, {y0})")
    print(f"Конечная точка: ({x1}, {y1})")
    print(f"Яркость линии (0..255): {v_line}")
    print(f"Яркость фона (0..255): {v_bg}")

    dx = abs(x1 - x0)
    dy = abs(y1 - y0)

    sx = 1 if x0 < x1 else -1
    sy = 1 if y0 < y1 else -1

    is_steep = dy > dx

    if is_steep:
        dx, dy = dy, dx

    err = dx // 2

    x, y = x0, y0

    for _ in range(dx + 1):
        if is_steep:
            px, py = y, x
        else:
            px, py = x, y
        if 0 <= px < width and 0 <= py < height:
            image[py][px] = v_line

        if err >= 0:
            y += sy
            err -= 2 * dx
        err += 2 * dy
        x += sx

    save_file(filename=filename, image=image)
    print()


def circe_gradient(height, width, r, cx, cy, v_center, v_edge, v_bg, filename):
    image = filled_image(height, width, v_bg)

    print_image_info(
        "Круг с радиальным градиентом",
        width, height, filename
    )

    print(f"Центр cx: {cx}")
    print(f"Центр cy: {cy}")
    print(f"Радиус: {r}")
    print(f"Яркость в центре: {v_center}")
    print(f"Яркость на границе: {v_edge}")
    print(f"Яркость фона (0..255): {v_bg}")

    for y in range(height):
        for x in range(width):
            dist = ((x - cx + 0.5) ** 2 + (y - cy + 0.5) ** 2) ** 0.5

            if dist <= r:
                t = dist / r
                v = round(v_center + (v_edge - v_center) * t)
                image[y][x] = v

    save_file(filename=filename, image=image)
    print()


def main():
    while True:
        print(*print_menu())

        choice = valid_user_input_menu()

        if choice == 0:
            print("Выход.")
            break

        elif choice == 1:
            params = valid_user_input_square()
            square_center_side(*params)

        elif choice == 2:
            params = valid_user_input_nested_square()
            nested_squares(*params)

        elif choice == 3:
            params = valid_user_input_line_segment()
            line_segment(*params)

        elif choice == 4:
            params = valid_user_input_circle()
            circe_gradient(*params)



if __name__ == "__main__":
    main()