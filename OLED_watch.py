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
try:
 disp = OLED_1in51.OLED_1in51()
 # Initialize library.
 disp.Init()
 # Clear display.
 #logging.info("clear display")
 #disp.clear()

except IOError as e:
 logging.info(e)
        

while True:
 try:
 
  # Create blank image for drawing.
  image1 = Image.new('1', (disp.width, disp.height), "WHITE")
  draw = ImageDraw.Draw(image1)
  #font2 = ImageFont.truetype(os.path.join(picdir, 'Font.ttc'), 24)
  #logging.info ("***draw line")
  #draw.line([(0,0),(127,0)], fill = 0)
  #draw.line([(0,0),(0,63)], fill = 0)
  #draw.line([(0,63),(127,63)], fill = 0)
  #draw.line([(127,0),(127,63)], fill = 0)
  
  now = datetime.now()
  formatted_time = now.strftime("%H:%M:%S")
  
  logging.info ("***draw time")
  #draw.text((25,10), 'Waveshare', fill = 0)
  draw.text((25,30), f"{formatted_time}" , fill = 0)
  image1 = image1.rotate(180) 
  disp.ShowImage(disp.getbuffer(image1))
  time.sleep(0.1)
 
 except KeyboardInterrupt:
  logging.info("ctrl + c:")
  disp.module_exit()
  exit()
    
