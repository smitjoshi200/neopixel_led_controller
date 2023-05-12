import config as cfg
import neopixel

pixels = neopixel.NeoPixel(cfg.GPIO_BOARD, cfg.TOTAL_LEDS, brightness=cfg.BRIGHTNESS)
pixels.fill((99,66,23))
pixels.show()