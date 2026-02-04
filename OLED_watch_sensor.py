#!/usr/bin/python
# -*- coding:utf-8 -*-




from datetime import datetime

import sys
import os
picdir = os.getcwd() #os.path.join(os.path.dirname(os.path.dirname(os.path.realpath(__file__))), 'pic')
#picdir = os.path.join(os.path.dirname(os.path.dirname(os.path.realpath(__file__))), 'pic')
#libdir = os.path.join(os.path.dirname(os.path.dirname(os.path.realpath(__file__))), 'lib')
#if os.path.exists(libdir):
#    sys.path.append(libdir)

import logging    
import time
import traceback
import OLED_1in51
#from waveshare_OLED import OLED_1in51
from PIL import Image,ImageDraw,ImageFont
logging.basicConfig(level=logging.DEBUG)

font_file_name = "SonicAdvanced2.ttf"
#"NickTurboItalic3D.ttf"
#"groovysmoothielaser.ttf" #FinalLap.ttf

## sensor readout
import board

# CO2 
import adafruit_scd4x

# humidity and temp
import adafruit_sht31d
import time
i2c = board.I2C()
sensor_sht31 = adafruit_sht31d.SHT31D(i2c)
scd4x = adafruit_scd4x.SCD4X(i2c)
scd4x.start_periodic_measurement()

def read_sensor_co2( ):
    sensor_co2 = scd4x.CO2
    #1800
    return(f"CO2:{sensor_co2}")

def read_sensor_temp( ):
    sensor_temp = round( sensor_sht31.temperature, 1)
    #23.1
    return(f"T:{sensor_temp}")

def read_sensor_humi( ):
    sensor_humi = round( sensor_sht31.relative_humidity )
    # 40
    return(f"H:{sensor_humi}")

try:
 disp = OLED_1in51.OLED_1in51()
 # Initialize library.
 disp.Init()
 font2 = ImageFont.truetype(os.path.join(picdir, font_file_name), 24)
 # Clear display.
 #logging.info("clear display")
 #disp.clear()

except IOError as e:
 logging.info(e)
        

try:
  
 while True:
  # Create blank image for drawing.
  image1 = Image.new('1', (disp.width, disp.height), "WHITE")
  draw = ImageDraw.Draw(image1)
  
  #logging.info ("***draw line")
  # draw.line([(0,0),(127,0)], fill = 0)
  # draw.line([(0,0),(0,63)], fill = 0)
  draw.line([(5,28),(122,28)], fill = 0)
  draw.line([(5,29),(122,29)], fill = 0)
  # draw.line([(127,0),(127,63)], fill = 0)
  
  # time
  now = datetime.now()
  formatted_time = now.strftime("%H:%M")
  
  # sensor
  sensor_temp_text = read_sensor_temp()
  sensor_humi_text = read_sensor_humi()
  sensor_co2_text  = read_sensor_co2()

  #logging.info ("***draw time")
  #draw.text((25,10), 'Waveshare', fill = 0)
  draw.text((3, 3), f"{formatted_time}" , font = font2 , fill = 0)
  draw.text((50,3),  sensor_co2_text , font = font2 , fill = 0)
  draw.text((3,25) , sensor_temp_text , font = font2 , fill = 0)
  draw.text((55,25), sensor_humi_text , font = font2 , fill = 0)

  #image1 = image1.rotate(180) 
  disp.ShowImage(disp.getbuffer(image1))
  
  time.sleep(0.1)
 
except KeyboardInterrupt:
 logging.info("ctrl + c:")
 disp.module_exit()
 exit()
    
