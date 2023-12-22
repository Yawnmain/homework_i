import cv2

def find_ru_in_frame(frame, template):
    result = cv2.matchTemplate(frame, template, cv2.TM_CCOEFF_NORMED)

    threshold = 0.7
    match = 0
    for res in result:
        for val in res:
            if val >= threshold:
                match += 1
    return match


def resize_input_image(image_path, target_width, target_height):
    img = cv2.imread(image_path, cv2.IMREAD_COLOR)
    resized_img = cv2.resize(img, (target_width, target_height))
    return resized_img


def count_template_match(video_path, template_image_path):
    template_img = resize_input_image(template_image_path, 640, 480)

    cap = cv2.VideoCapture(video_path)

    count = 0

    while True:
        ret, frame = cap.read()
        if not ret:
            break

        count += find_ru_in_frame(frame, template_img)

    cap.release()
    return count


if __name__ == "__main__":
    video_path = "output.avi"
    template_image_path = "ru.png"

    match = count_template_match(video_path, template_image_path)
    print(f"Кол-во флагов России: {match}")
