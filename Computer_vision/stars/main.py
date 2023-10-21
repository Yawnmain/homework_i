# import numpy as np
# from matplotlib import pyplot as plt

# img_array = np.load("stars.npy")
# plt.imshow(img_array, cmap="gray")
# plt.show()

import numpy as np
from scipy.signal import convolve2d
from scipy.ndimage import label

img = np.load("stars.npy")

def mask_conv(image, mask):
    convolved = convolve2d(image, mask, mode='same')
    labeled_data, num_features = label(convolved > 0)
    return num_features

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

stars_plus = mask_conv(img, plus)
stars_cross = mask_conv(img, cross)
ans = stars_plus + stars_cross

print(f"кол-во звезд: {ans}")
