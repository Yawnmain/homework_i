import numpy as np
import matplotlib.pyplot as plt

def load(filename):
    with open(filename) as file:
        _ = file.readline()
        img = np.loadtxt(file)
    return img

def offset(img1, img2):
    cord = np.correlate(img1.ravel(), img2.ravel(), mode='full')
    y, x = divmod(np.argmax(cord), img2.shape[1])
    return y - img1.shape[0] + 1, x - img1.shape[1] + 1

def save_image_with_offset(img, offset, filename):
    shifted_img = np.roll(img, offset, axis=(0, 1))
    with open(filename, 'w') as file:
        file.write(f"Сдвиг (y, x): {offset}\n")
        np.savetxt(file, shifted_img, fmt='%d')

img1 = load("images/img1.txt")
img2 = load("images/img2.txt")

offset = offset(img1, img2)
print(f"Offset is (y, x): {offset}")

# Сохранение изображения с отмеченным сдвигом
save_image_with_offset(img2, offset, "images/img2_shifted.txt")

# Отображение изображения с сдвигом
plt.imshow(img2)
plt.title(f"Сдвиг (y, x): {offset}")
plt.show()
