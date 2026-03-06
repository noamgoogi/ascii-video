import cv2
from PIL import Image
import os
from time import sleep
import time
import shutil

video = cv2.VideoCapture("skull.gif")
if not video.isOpened():
    print("Error: Could not open video.")
else:
    frame_count = video.get(cv2.CAP_PROP_FRAME_COUNT)
    fps = video.get(cv2.CAP_PROP_FPS)
    if fps > 0: # Avoid division by zero
        duration_seconds = frame_count / fps
        print(f"Video duration: {duration_seconds:.2f} seconds")
    else:
        print("Error: Could not retrieve FPS.")


def get_terminalSize() -> tuple:
    try:
        terminal_size = shutil.get_terminal_size()
        return terminal_size.columns, terminal_size.lines
    except OSError:

        return 80, 24  # Default values

terminalSize = get_terminalSize()
print(f"Terminal size: {terminalSize[0]} columns x {terminalSize[1]} lines")


pics = []
while True:
    success, image = video.read()
    if not success:
        break

    img = Image.fromarray(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
    img = img.resize(terminalSize)

    lines = ""
    width, height = img.size
    for y in range(height):
        for x in range(width):
            r, g, b = img.getpixel((x, y))
            brightness = 0.299 * r + 0.587 * g + 0.114 * b
            if brightness >= 200:
                lines += "@"
            elif brightness >= 150:
                lines += "#"
            elif brightness >= 100:
                lines += "%"
            elif brightness >= 50:
                lines += "*"
            elif brightness >= 25:
                lines += "+"
            elif brightness >= 10:
                lines += ":"
            elif brightness >= 5:
                lines += "."
            else:
                lines += " "
        lines += "\n"
    pics.append(lines)


duration_seconds /= len(pics)
print(f"Displaying each frame for {duration_seconds:.2f} seconds")
for pic in pics:
    t = time.time()
    print(f"\033[{terminalSize[1]}A", end="")
    print(pic, end="")
    
    t = duration_seconds - (time.time() - t)
    if t > 0:
        sleep(t)
