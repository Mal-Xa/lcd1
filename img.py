import time, glob
from PIL import Image
from luma.core.interface.serial import spi
from luma.lcd.device import ili9341

serial = spi(port=0, device=0, gpio_DC=24, gpio_RST=25)
device = ili9341(serial, width=240, height=320, rotate=0)

for file in glob.glob("gfh.jpg"):
    img = Image.open(file).resize((device.width, device.height)).convert("RGB")
    device.display(img)
    time.sleep(3)
