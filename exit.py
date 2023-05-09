import board
import neopixel

pixels = neopixel.NeoPixel(board.D18, 120, brightness=0.05)

pixels.deinit()