import os
import numpy as np
import matplotlib.pyplot as plt
from skimage.morphology import (binary_erosion, binary_dilation,
                                binary_opening, binary_closing)
from skimage.measure import label

image_folder = "images"

image_files = [f for f in os.listdir(image_folder) if f.endswith('.npy')]

for image_file in image_files:
    image_path = os.path.join(image_folder, image_file)
    wires = np.load(image_path)

    labeled = label(wires)

    breaks = []

    for label_value in range(1, labeled.max() + 1):
        current_wire = np.zeros_like(wires)
        current_wire[labeled == label_value] = 1

        struct = np.ones((3, 1))
        current_wire = binary_erosion(current_wire, struct)

        reduced_labeled = label(current_wire)

        if reduced_labeled.max() > 1:
            num_breaks = reduced_labeled.max()
            breaks.append((label_value, num_breaks))
        else:
            breaks.append((label_value, 0))

    for label_value, num_breaks in breaks:
        if num_breaks == 0:
            print(f"Провод с меткой {label_value} не порван.")
        else:
            print(f"Провод с меткой {label_value} порван на {num_breaks} части(ей).")

    plt.subplot(121)
    plt.imshow(labeled)
    plt.subplot(122)
    plt.imshow(wires)
    plt.show()
