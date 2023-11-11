import numpy as np
from skimage import measure

coins_image = np.load('coins.npy')

labeled_coins = measure.label(coins_image)

sum_1 = 0
sum_2 = 0
sum_5 = 0
sum_10 = 0

for region in measure.regionprops(labeled_coins):
    area = region.area
    centroid = region.centroid

    if area < 70:
        sum_1 += 1
    elif area < 150:
        sum_2 += 2
    elif area < 310:
        sum_5 += 5
    else:
        sum_10 += 10

print(f"Сумма монет номиналом 1: {sum_1}")
print(f"Сумма монет номиналом 2: {sum_2}")
print(f"Сумма монет номиналом 5: {sum_5}")
print(f"Сумма монет номиналом 10: {sum_10}")
print(f"Всего: {sum_10+sum_1+sum_2+sum_5}")