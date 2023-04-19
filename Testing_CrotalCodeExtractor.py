# -*- coding: utf-8 -*-
"""
Created on Sat Apr 15 23:11:19 2023

@author: Rebeca Villarraso

PRACTICA 2: CROTALES

"""

import ProcessImage, ExtractCode, ExportCode
import time
from ExtractCode import *
from ProcessImage import *
from ExportCode import *
from termcolor import colored
pytesseract_path='C:\\Users\\bfzjs\\AppData\\Local\\Programs\\Tesseract-OCR\\tesseract.exe'

#-----------------------------------------------------------------------------
#  Main()   AUTOMATED TEST, NO ARGUMENTS ARE REQUIRED
#-----------------------------------------------------------------------------                    
# DEFAULT VALUES
image_path = './TestSamples/' 
image_name = '0001.tif'       
output_path = './Codes/'

count=0
if __name__ == '__main__':
    print('STARTED AUTOMATED POSITIVE TESTING, please wait...') ########################################################♦
    # TEST 1. 
    # - Check if path of image to load/read exists
    # - Check the format of image. Shall be .tif
    # - Check that the image specified in path exists
    # - Check if the existing destination folder exists
    
    txt=colored('TEST 1. Testing correct image path', "magenta")
    print(txt)
    my_object=ExtractCode(image_path, image_name, output_path)
    error=my_object.Ejecutar()
    if error == 0: 
        txt=colored('Positive Testing is PASS', "cyan")
        count+=1
    else: txt=colored('Positive Testing is FAIL', 'red')
    print(txt, error)
    print('')
    
    print('STARTED AUTOMATED NEGATIVE TESTING, please wait...') ########################################################♦
    # TEST 2. Check the path of image to load/read
    txt=colored('TEST 2. Testing with wrong image path', "magenta")
    print(txt)
    image_path='./empty/'
    my_object=ExtractCode(image_path, image_name, output_path)
    error=my_object.Ejecutar()
    if error == 1: 
        txt=colored('Testing with wrong image path is PASS', "cyan")
        count+=1
    else:  txt=colored('Testing with wrong image path is FAIL', 'red')
    print(txt, error)
    print('')
    
    # TEST 3. Check the format of image. Shall be .tif (image exists)
    txt=colored('TEST 3. Testing with wrong image format', "magenta")
    print(txt)
    image_path = './TestSamples/' 
    image_name='0001.jpg'
    my_object=ExtractCode(image_path, image_name, output_path)
    error=my_object.Ejecutar()
    if error == 1: 
        txt=colored('Testing with wrong image format is PASS', "cyan")
        count+=1
    else:  txt=colored('Testing with wrong image format is FAIL', 'red')
    print(txt, error)
    print('')
      
    # TEST 4. Check that the image specified in path exists (image no exists)
    txt=colored('TEST 4. Testing if image specified exists in path', "magenta")
    print(txt)
    image_path = './TestSamples/' 
    image_name='0002.jpg'
    my_object=ExtractCode(image_path, image_name, output_path)
    error=my_object.Ejecutar()
    if error == 1: 
        txt=colored('Testing if image exists is PASS', "cyan")
        count+=1
    else:  txt=colored('Testing if image exists is FAIL', 'red')
    print(txt, error)
    print('')
    
    # TEST 5. Check that the destination folder exists 
    txt=colored('TEST 5. Testing destination folder', "magenta")
    print(txt)
    image_path = './TestSamples/' 
    image_name = '0001.tif'   
    output_path = './empty/'
    my_object=ExtractCode(image_path, image_name, output_path)
    error=my_object.Ejecutar()
    if error == 1: 
        txt=colored('Testing destination folder is PASS', "cyan")
        count+=1
    else:  txt=colored('Testing destination folder is FAIL', 'red')
    print(txt, error)
    print('')
      
    # TEST 6. Check that execution time
    txt=colored('TEST 6. Testing execution time', "magenta")
    print(txt)
    st = time.time()
    image_path = './TestSamples/' 
    image_name = '0001.tif'       
    output_path = './Codes/'
    my_object=ExtractCode(image_path, image_name, output_path)
    error=my_object.Ejecutar()    
    if error == 0: 
        elapsed_time=0
        image=ProcessImage(image_path, image_name, pytesseract_path) 
        code=image.get_code()
        export=ExportCode(image_name, output_path, code) 
        export.saveCodetoTxt()
        et = time.time()       
        elapsed_time = et - st
        print('Execution time:', elapsed_time, 'seconds')   
        if elapsed_time < 31:
            txt=colored('Testing execution time PASS', "cyan")
            count+=1
        else:
            txt=colored('Testing execution time is FAIL', 'red')
    print(txt, error)
    print('')
    
if count == 6: txt=colored('Automated test is PASS',  "green")   
else: txt=colored('Automated test is FAIL, almost one test is FAIL', 'red')
print(txt)


                