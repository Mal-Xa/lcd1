from luma.core.interface.serial import spi
from luma.lcd.device import ili9341
from PIL import Image, ImageDraw, ImageFont
import time

# SPI setup (port=0 CE0, DC=25, RST=24)
serial = spi(port=0, device=0, gpio_DC=25, gpio_RST=24)

# Create device
device = ili9341(serial, width=320, height=240, rotate=90)

# Create a new image
img = Image.new('RGB', (device.width, device.height))
draw = ImageDraw.Draw(img)

# Draw background and text
draw.rectangle((0, 0, device.width, device.height), fill=(0, 0, 100))
font = ImageFont.load_default()
draw.text((40, 100), "Hello ILI9341!", font=font, fill=(255, 255, 0))
draw.text((40, 120), time.strftime("%Y-%m-%d %H:%M:%S"), font=font, fill=(255, 255, 255))

# Display
device.display(img)
time.sleep(10)
