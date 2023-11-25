import os
from PIL import Image

def count_pencils_in_image(image_path):
    try:
        img = Image.open(image_path)

        green_count = 0
        cyan_count = 0
        orange_count = 0

        pixels = img.load()
        for x in range(img.width):
            for y in range(img.height):
                r, g, b = pixels[x, y]

                if r < 60 and g > 123 and b < 25:  # Зеленый (60, 123, 25)
                    green_count += 1
                elif r < 47 and g > 96 and b > 126:  # Голубой (47, 96, 126)
                    cyan_count += 1
                elif r > 177 and g > 78 and b < 45:  # Оранжевый (177, 78, 45)
                    orange_count += 1

        # Предположим, что каждый цвет карандаша имеет определенное количество пикселей
        pixels_per_pencil = 2550

        # Рассчитываем количество карандашей каждого цвета
        green_pencils = green_count // pixels_per_pencil
        cyan_pencils = cyan_count // pixels_per_pencil
        orange_pencils = orange_count // pixels_per_pencil

        return green_pencils, cyan_pencils, orange_pencils
    except Exception as e:
        print(f"Ошибка при обработке изображения {image_path}: {e}")
        return 0, 0, 0

def count_pencils_in_folder(folder_path):
    total_green = 0
    total_cyan = 0
    total_orange = 0

    image_files = [os.path.join(folder_path, file) for file in os.listdir(folder_path) if file.endswith(('jpg'))]

    for image_path in image_files:
        green, cyan, orange = count_pencils_in_image(image_path)
        total_green += green
        total_cyan += cyan
        total_orange += orange

    return total_green, total_cyan, total_orange

folder_with_images = "./images"

total_green, total_cyan, total_orange = count_pencils_in_folder(folder_with_images)
total_count = total_green + total_cyan + total_orange

print(f"Общее количество карандашей (зеленые): {total_green}")
print(f"Общее количество карандашей (голубые): {total_cyan}")
print(f"Общее количество карандашей (оранжевые): {total_orange}")
print(f"Общее количество карандашей: {total_count}")
