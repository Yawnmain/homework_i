import numpy as np
from skimage.measure import label
from skimage.morphology import binary_erosion, binary_opening

img = np.load("psnpy.txt")

obj_1 = np.array([[0,0,0,0,0,0],
                  [0,0,0,0,0,0],
                  [1,1,1,1,1,1],
                  [1,1,1,1,1,1],
                  [1,1,1,1,1,1],
                  [1,1,1,1,1,1]])


obj_2 = np.array([[0,0,0,0,0,0],
                  [0,0,0,0,0,0],
                  [1,1,0,0,1,1],
                  [1,1,0,0,1,1],
                  [1,1,1,1,1,1],
                  [1,1,1,1,1,1]])


obj_3 = np.array([[0,0,0,0,0,0],
                  [0,0,0,0,0,0],
                  [1,1,1,1,1,1],
                  [1,1,1,1,1,1],
                  [1,1,0,0,1,1],
                  [1,1,0,0,1,1]])


obj_4 = np.array([[0,0,1,1,1,1],
                  [0,0,1,1,1,1],
                  [0,0,0,0,1,1],
                  [0,0,0,0,1,1],
                  [0,0,1,1,1,1],
                  [0,0,1,1,1,1]])


obj_5 = np.array([[0,0,1,1,1,1],
                  [0,0,1,1,1,1],
                  [0,0,1,1,0,0],
                  [0,0,1,1,0,0],
                  [0,0,1,1,1,1],
                  [0,0,1,1,1,1]])

img = label(img)

print(f"Zero: {label(binary_opening(img, obj_1)).max()}")
print(f"Left: {label(binary_opening(img, obj_4)).max()}")
print(f"Right: {label(binary_opening(img, obj_5)).max()}")
print(f"Up: {label(binary_opening(img, obj_2)).max() - label(binary_opening(img, obj_1)).max()}")
print(f"Down: {label(binary_opening(img, obj_3)).max() - label(binary_opening(img, obj_1)).max()}")
print(f"Total: {np.max(img)}")