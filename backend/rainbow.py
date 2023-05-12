import config as cfg
import neopixel
import time
pixels = neopixel.NeoPixel(cfg.GPIO_BOARD, cfg.TOTAL_LEDS, brightness=cfg.BRIGHTNESS)
def wheel(pos):
    # Input a value 0 to 255 to get a color value.
    # The colours are a transition r - g - b - back to r.
    if pos < 0 or pos > 255:
        r = g = b = 0
    elif pos < 85:
        r = int(pos * 3)
        g = int(255 - pos * 3)
        b = 0
    elif pos < 170:
        pos -= 85
        r = int(255 - pos * 3)
        g = 0
        b = int(pos * 3)
    else:
        pos -= 170
        r = 0
        g = int(pos * 3)
        b = int(255 - pos * 3)
    return (r, g, b) if cfg.ORDER in (neopixel.RGB, neopixel.GRB) else (r, g, b, 0)

def rainbow_cycle(wait, speed=0.001):
    for j in range(255):
        for i in range(cfg.TOTAL_LEDS):
            pixel_index = (i * 256 // cfg.TOTAL_LEDS) + j
            pixels[i] = wheel(pixel_index & 255)
            time.sleep(speed)
        pixels.show()
        time.sleep(wait)
        return

        
while True:
    rainbow_cycle(0.01)
    pixels.fill((0,0,0))
    pixels.show()
    