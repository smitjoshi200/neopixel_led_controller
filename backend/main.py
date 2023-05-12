import config as cfg
import neopixel
import time

pixels = neopixel.NeoPixel(cfg.GPIO_BOARD, cfg.TOTAL_LEDS, brightness=cfg.BRIGHTNESS)
pixels.fill((0, 120, 220))

