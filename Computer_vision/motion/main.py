import numpy as np
import matplotlib.pyplot as plt
from skimage.measure import label, regionprops
import os

def load_data(index):
    return np.load(f"out/h_{index}.npy")

file_indices = [int(filename.split('_')[1].split('.')[0]) for filename in os.listdir("out") if filename.endswith('.npy')]

if file_indices:
    first_image = load_data(file_indices[0])
    image_shape = first_image.shape  # Получение размеров изображения

    plt.figure()

    for index in file_indices[1:]:
        current_image = load_data(index)

        labeled_prev = label(first_image)
        labeled_curr = label(current_image)

        regions_prev = regionprops(labeled_prev)
        regions_curr = regionprops(labeled_curr)

        # Отображение траекторий объектов на графике
        for region_prev in regions_prev:
            plt.plot([region_prev.centroid[1]], [region_prev.centroid[0]], 'bo')  # Текущая позиция объектов

        for region_curr in regions_curr:
            plt.plot([region_curr.centroid[1]], [region_curr.centroid[0]], 'ro')  # Новая позиция объектов
        first_image = current_image

    plt.xlabel('X')
    plt.ylabel('Y')
    plt.show()
    