import cv2
from PIL import Image
import os
from time import sleep

cap = cv2.VideoCapture("Rotating Donut Stock Video.mp4")
fps = round(cap.get(cv2.CAP_PROP_FPS))
sec_per_frame = fps/1000
print(f"Milliseconds per frame: {sec_per_frame}")


pics = []
while True:
    success, image = cap.read()
    if not success:
        break

    img = Image.fromarray(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
    img = img.resize((120, 60))

    lines = ""
    width, height = img.size
    for y in range(height):
        for x in range(width):
            r, g, b = img.getpixel((x, y))
            brightness = 0.299 * r + 0.587 * g + 0.114 * b
            if brightness > 200:
                lines += "@"
            elif brightness > 150:
                lines += "#"
            elif brightness > 100:
                lines += "%"
            elif brightness > 50:
                lines += "*"
            else:
                lines += ":"
        lines += "\n"
    pics.append(lines)

for pic in pics:
    print(pic)
    sleep(sec_per_frame)
    os.system("cls")


cap.release()
