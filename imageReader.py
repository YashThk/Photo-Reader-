# -*- coding: utf-8 -*-
"""
Created on Sun Oct 11 19:29:04 2020

@author: HP
"""

import pytesseract as pt
pt.pytesseract.tesseract_cmd = r'C:\Users\Default.migrated\AppData\Local\tesseract.exe'
import os 
import cv2
import pandas as pd


directory = r'C:\Users\HP\Desktop\Research Assistant\Instagram_BB\Insta_B@B'
list_number = []
list_image = []
def image_to_text(folder):
    i = 1
    for fn in os.listdir(folder):
        img = cv2.imread(os.path.join(folder,fn))
        if img is not None:
            text = pt.image_to_string(img)
            list_image.extend([text]) 
            list_number.extend([i])
        i = i+1
    return list_image
    return list_number

image_to_text(directory)

df = pd.DataFrame()
df['ImageNo'] = list_number
df['ImageContent'] = list_image
df.to_csv('Insta_B@B_ImageContent.csv', index=True)

