from luma.core.interface.serial import spi
from luma.oled.device import ssd1309
from luma.core.render import canvas
from PIL import ImageFont
import time

# Pin configuration (using BCM numbering)
# DC: 24, RST: 25 (Standard Waveshare/Pi configurations)
serial = spi(device=0, port=0, gpio_DC=24, gpio_RST=25)
device = ssd1309(serial)

with canvas(device) as draw:
    # Drawing a simple interface
    draw.rectangle(device.bounding_box, outline="white", fill="black")
    draw.text((30, 20), "Hello Pi!", fill="white")
    draw.text((10, 40), "1.51 inch OLED", fill="white")
    draw.line([(0,0),(107,0)], fill = 0)


while True:
    time.sleep(1)


