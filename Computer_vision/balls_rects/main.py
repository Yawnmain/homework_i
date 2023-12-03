import numpy as np
import cv2

def count_shapes_by_hue(image_path):
    img = cv2.imread(image_path)
    hsv_img = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    _, thresholded = cv2.threshold(gray_img, 128, 192, cv2.THRESH_OTSU)
    labeled = cv2.connectedComponents(thresholded)[1]

    results = {}
    circles = 0
    rects = 0

    for i in range(1, np.max(labeled) + 1):
        figure = np.where(labeled == i)

        y_min, x_min = figure[0][0], figure[1][0]
        y_max, x_max = figure[0][-1], figure[1][-1]

        hue = hsv_img[y_min][x_min][0]

        if hue not in results:
            results[hue] = {"rects": 0, "circles": 0}

        if (x_max - x_min + 1) * (y_max - y_min + 1) == len(figure[0]):
            results[hue]["rects"] += 1
            rects += 1
        else:
            results[hue]["circles"] += 1
            circles += 1

    print(f"Всего оттенков: {len(results)}")
    print(f"Всего фигур: {np.max(labeled)}")
    print(f"Прямоугольников: {rects}")
    print(f"Кругов: {circles}\n")

    for hue in results:
        print(f"оттенок - {hue}: прямоугольников: {results[hue]['rects']}, кругов: {results[hue]['circles']}")

image_path = "balls_and_rects.png"
count_shapes_by_hue(image_path)
