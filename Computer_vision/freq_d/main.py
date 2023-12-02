import numpy as np
import matplotlib.pyplot as plt
from skimage.measure import label, regionprops

def filling_factor(region):
    return np.mean(region.image)

def recognize(region):
    def check_fill_factor(factor):
        return factor == 1

    def process_euler_1():
        if np.any(region.image.mean(0) == 1):
            if region.eccentricity < 0.5:
                return "*"
            else:
                return "1"
        tmp = region.image.copy()
        tmp[[0, -1], :] = 1
        tmp_label = label(tmp)
        tmp_regions = regionprops(tmp_label)
        euler = tmp_regions[0].euler_number
        if euler == -1:
            return 'X'
        elif euler == -2:
            return "W"
        return '/' if region.eccentricity > 0.5 else '*'

    if check_fill_factor(filling_factor(region)):
        return '-'
    else:
        euler = region.euler_number
        if euler == -1:
            if np.any(region.image.mean(0)[:1] == 1):
                return 'B'
            else:
                return '8'
        elif euler == 0:
            tmp = region.image.copy()
            tmp[-1, :] = 1
            tmp_labeled = label(tmp)
            tmp_regions = regionprops(tmp_labeled)
            if np.any(region.image.mean(0)[:1] == 1):
                tmp[:, -len(tmp[0]) // 2:] = 1
                e = tmp_regions[0].euler_number
                if e == -1:
                    return 'P'
                elif e == 0:
                    return 'D'
            if np.any(region.image.mean(1) == 1):
                return '*'
            if tmp_regions[0].euler_number == -1:
                return 'A'
            else:
                return '0'
        elif euler == 1:
            return process_euler_1()
    return '?'


image = plt.imread('symbols.png').min(2)
image[image > 0] = 1
labeled = label(image)

regions = regionprops(labeled)

counts = {}

for region in regions:
    symbol = recognize(region)
    counts[symbol] = counts.get(symbol, 0) + 1

total_symbols = np.max(labeled)
unknown_symbols = counts.get("?", 0)
percentage_recognized = (1 - unknown_symbols / total_symbols) * 100

print(f"Всего символов: {total_symbols}")
print(f"Процент распознования: {percentage_recognized}%")

for symbol, count in counts.items():
    print(f"{symbol}: {count}")
