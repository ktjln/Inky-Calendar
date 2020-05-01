#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
Stock module for Inky-Calendar software.

Based on Weather module by aceisace
Add infos on source for shares.....

Copyright by sjstrobl
"""
from __future__ import print_function
from configuration import *

#"""Optional parameters"""
#round_temperature = True
#...

print('Initializing stock...', end=' ')
#owm = pyowm.OWM(api_key, language=language)
print('Done')

"""Add a border to increase readability"""
border_top = int(top_section_height * 0.05)
border_left = int(top_section_width * 0.02)

"""Calculate size for each stock sub-section"""
#row_height = (top_section_height-(border_top*2)) // 3
row_height = (top_section_height-(border_top*2)) // 3
coloumn_width = (top_section_width-(border_left*2)) // 6

"""Calculate paddings"""
x_padding = int( (top_section_width % coloumn_width) / 2 )
y_padding = int( (top_section_height % row_height) / 2 )

#"""Allocate sizes for stock icons"""
#icon_small = row_height
#icon_medium = row_height * 2

"""Calculate the x-axis position of each coloumn"""
coloumn1 = x_padding
coloumn2 = coloumn1 + coloumn_width
coloumn3 = coloumn2 + coloumn_width
coloumn4 = coloumn3 + coloumn_width
coloumn5 = coloumn4 + coloumn_width
coloumn6 = coloumn5 + coloumn_width

"""Calculate the y-axis position of each row"""
row1 = y_padding
row2 = row1 + row_height
row3 = row2 + row_height

"""Allocate positions for indices"""
text11_pos = (coloumn1, row1)
text12_pos = (coloumn1, row2)
text13_pos = (coloumn1, row3)
text21_pos = (coloumn2, row1)
text22_pos = (coloumn2, row2)
text23_pos = (coloumn2, row3)
text31_pos = (coloumn3, row1)
text32_pos = (coloumn3, row2)
text33_pos = (coloumn3, row3)
text41_pos = (coloumn4, row1)
text42_pos = (coloumn4, row2)
text43_pos = (coloumn4, row3)

print ("## DEBUG text positions")
print ('text11_pos ',text11_pos)
print ('text12_pos ',text12_pos)
print ('text13_pos ',text13_pos)
print ('text21_pos ',text21_pos)
print ('text22_pos ',text22_pos)
print ('text23_pos ',text23_pos)
print ('text31_pos ',text31_pos)
print ('text32_pos ',text32_pos)
print ('text33_pos ',text33_pos)
print ('text41_pos ',text41_pos)
print ('text42_pos ',text42_pos)
print ('text43_pos ',text43_pos)

"""Choose font optimised for the stock section"""
fontsize = 8
font = ImageFont.truetype(NotoSans+'Medium.ttf', fontsize)
fill_height = 0.8

while font.getsize('hg')[1] <= (row_height * fill_height):
  fontsize += 1
  font = ImageFont.truetype(NotoSans+'.ttf', fontsize)

def generate_image():
  """Connect to ****** API and fetch stock data"""
  if top_section == "inkycal_stock":#  and rss_feeds != [] and internet_available() == True:
    try:
      clear_image('top_section')
#      print('Stock module: Connectivity check passed, Generating image...',
#        end = '')
#      get data / connect to server / whatever

      text11_str = 'DAX'
      text12_str = 'DowJones'
      text13_str = 'S&P500'
      text21_str = '0000'
      text22_str = '1111'
      text23_str = '1111'
      text31_str = 'Öl'
      text32_str = 'Gold'
      text33_str = 'Silber'
      text41_str = 'XXXX'
      text42_str = 'YYYY'
      text43_str = 'ZZZZ'

      print('coloumn_width: ', coloumn_width)
      print('row_height: ', row_height)
      print('text11_str: ', text11_str)
      print('text11_pos: ', text11_pos)
      """column 1"""
      write_text(coloumn_width, row_height, text11_str, text11_pos, font = font,
        alignment='right')
      write_text(coloumn_width, row_height, text12_str, text12_pos, font = font,
        alignment='right')
      write_text(coloumn_width, row_height, text13_str, text13_pos, font = font,
        alignment='right')

      """column 2"""
      write_text(coloumn_width, row_height, text21_str, text21_pos, font = font,
        alignment='left')
      write_text(coloumn_width, row_height, text22_str, text22_pos, font = font,
        alignment='left')
      write_text(coloumn_width, row_height, text23_str, text23_pos, font = font,
        alignment='left')

      """column 3"""
      write_text(coloumn_width, row_height, text31_str, text31_pos, font = font,
        alignment='right')
      write_text(coloumn_width, row_height, text32_str, text32_pos, font = font,
        alignment='right')
      write_text(coloumn_width, row_height, text33_str, text33_pos, font = font,
        alignment='right')

      """column 2"""
      write_text(coloumn_width, row_height, text41_str, text41_pos, font = font,
        alignment='left')
      write_text(coloumn_width, row_height, text42_str, text42_pos, font = font,
        alignment='left')
      write_text(coloumn_width, row_height, text43_str, text43_pos, font = font,
        alignment='left')
      
      """Add vertical lines between forecast sections"""
      draw = ImageDraw.Draw(image)
      line_start_y = int(top_section_height*0.1)
      line_end_y = int(top_section_height*0.9)

      draw.line((coloumn3, line_start_y, coloumn3, line_end_y), fill='black')
      draw.line((coloumn5, line_start_y, coloumn5, line_end_y), fill='black')

      if three_colour_support == True:
        draw_col.line((0, top_section_height-border_top, top_section_width-
        border_left, top_section_height-border_top), fill='black', width=3)
      else:
        draw.line((0, top_section_height-border_top, top_section_width-
        border_left, top_section_height-border_top), fill='black', width=3)

      stock_image = crop_image(image, 'top_section')  
      stock_image.save(image_path+'inkycal_stock.png')

      if three_colour_support == True:
        stock_image_col = crop_image(image_col, 'top_section')  
        stock_image_col.save(image_path+'inkycal_stock_col.png')
        
      print('Done')

    except Exception as e:
      """If something went wrong, print a Error message on the Terminal"""
      print('Error in stock module!')
      print('Reason: ',e)
      clear_image('top_section')
#      write_text(top_section_width, top_section_height, str(e),
#                 (0, top_section_offset), font = font)
      write_text(top_section_width, top_section_height, str(e),
                 (0, 0), font = font)
      stock_image = crop_image(image, 'top_section')
      stock_image.save(image_path+'inkycal_stock.png')
      pass

def main():
  generate_image()

main()
