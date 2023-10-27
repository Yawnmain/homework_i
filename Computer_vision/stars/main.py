import numpy as np
from skimage.measure import label
from skimage.morphology import binary_erosion

img = np.load("stars.npy")

def count(image, mask):
    # маркировка
    labelled_data = label(image)
    #бинарная эрозия
    result = label(binary_erosion(labelled_data, mask))

    # -1(фон)
    return len(np.unique(result)) - 1

plus = np.array([[0, 0, 1, 0, 0],
                 [0, 0, 1, 0, 0],
                 [1, 1, 1, 1, 1],
                 [0, 0, 1, 0, 0],
                 [0, 0, 1, 0, 0]])

cross = np.array([[1, 0, 0, 0, 1],
                  [0, 1, 0, 1, 0],
                  [0, 0, 1, 0, 0],
                  [0, 1, 0, 1, 0],
                  [1, 0, 0, 0, 1]])

stars_plus = count(img, plus)
stars_cross = count(img, cross)

ans = stars_plus + stars_cross
print(ans)
