import os
import matplotlib.pyplot as plt
import numpy as np

# Функция для вычисления разрешения изображения
def custom_resolution_calculator(filename):
    with open(filename, "r") as file:
        img_size = float(file.readline())  # Чтение размера из файла
        img_data = np.loadtxt(file)  # Загрузка изображения в массив

    obj_rows = [row for row in img_data if 1 in row]  # Поиск объектных строк (содержащих 1)
    obj_width = len(obj_rows)  # Ширина объекта

    if obj_width == 0:
        return 0

    return img_size / obj_width  # Расчет разрешения

# Функция для отображения изображения и разрешения
def custom_image_display(ax, filename, resolution, figure_number):
    with open(filename, "r") as file:
        _ = file.readline()  # Пропустить первую строку
        img_data = np.loadtxt(file)  # Загрузка изображения

    ax.imshow(img_data)
    ax.set_title(f"Фигура {figure_number + 1}")
    ax.set_xlabel(f"Разрешение = {resolution} мм/пиксель")

# Каталог с файлами изображений
input = "input_files"
input_files = os.listdir(input)
fig_res = []  # Список для хранения разрешений
fig, axes = plt.subplots(2, 3, figsize=(8, 6))

# Вычисление разрешений и заполнение списка
for fig in input_files:
    fig_res += [round(custom_resolution_calculator(input + '/' + fig), 3)]

# Отображение изображений на графике
for i, fig in enumerate(input_files):
    j = int(i / 3)
    k = int(i % 3)
    custom_image_display(axes[j, k], f"{input}/{fig}", fig_res[i], i)

plt.subplots_adjust(wspace=1.5)
plt.show()
