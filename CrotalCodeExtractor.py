# -*- coding: utf-8 -*-
"""
Created on Sat Apr 15 09:46:01 2023

@author: Rebeca Villarraso

Class: Image
"""
import argparse, time
import ProcessImage, ExtractCode, ExportCode
from ExtractCode import *
from ProcessImage import *
from ExportCode import *

#-----------------------------------------------------------------------------
#  Main()
#-----------------------------------------------------------------------------                    
#Parámetros de entrada:
#--image_path='./TestSamples/' --image_name='0001.tif' --output_path='./Codes/' --pytesseract_path='C:\\Users\\bfzjs\\AppData\\Local\\Programs\\Tesseract-OCR\\tesseract.exe'

parser=argparse.ArgumentParser()
parser.add_argument('--image_path', type=str, default='./TestSamples/', help='Introduzca ruta de la imagen')
parser.add_argument('--image_name', type=str, default='0001.tif', help='Introduzca nombre de la imagen')
parser.add_argument('--output_path', type=str,default='./Codes/', help='Introduzca ruta destino')
parser.add_argument('--pytesseract_path', type=str,default='C:\\Users\\bfzjs\\AppData\\Local\\Programs\\Tesseract-OCR\\tesseract.exe', help='Introduzca ruta Tesseract-OCR')

#pytesseract.pytesseract.tesseract_cmd = 'C:\\Users\\bfzjs\\AppData\\Local\\Programs\\Tesseract-OCR\\tesseract.exe'     
args = parser.parse_args()
image_path = args.image_path  
image_name = args.image_name               
output_path = args.output_path   
pytesseract_path = args.pytesseract_path

if __name__ == '__main__':
    # get the start time
    st = time.time()
    
    # check requierements of image path, image format, and destination folder
    my_object=ExtractCode(image_path, image_name, output_path)
    error=my_object.Ejecutar()
    
    if error == 0: 
            image=ProcessImage(image_path, image_name, pytesseract_path) 
            code=image.get_code()
            export=ExportCode(image_name, output_path, code) 
            export.saveCodetoTxt()
            
# get the end time
et = time.time()       
# get the execution time
elapsed_time = et - st
print('Execution time:', elapsed_time, 'seconds')       
    
    

    

 
