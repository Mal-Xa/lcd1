from luma.core.interface.serial import spi
from luma.lcd.device import ili9341
from PIL import Image
import time

# SPI interface
serial = spi(port=0, device=0, gpio_DC=24, gpio_RST=25)

# Initialize display
device = ili9341(serial, width=240, height=320, rotate=0)

# Fill colors one by one
colors = ["red", "green", "blue", "white", "black"]
for c in colors:
    img = Image.new("RGB", (240, 320), c)
    device.display(img)
    time.sleep(1)
