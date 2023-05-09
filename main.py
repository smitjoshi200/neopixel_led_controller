import board
import neopixel
import time

pixels = neopixel.NeoPixel(board.D18, 120, brightness=0.5)

r = 255
for i in range(120):
    # r = (r - (i * 2)) if (r <= 255) else 255
    pixels[i] = (r, 40, 0)
    time.sleep(0.2)

for i in range((120-1), -1 , -1):
    pixels[i] = (0, 255, 0)
    time.sleep(0.2)
