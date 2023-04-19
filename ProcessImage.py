# -*- coding: utf-8 -*-
"""
Created on Sat Apr 15 09:52:13 2023

@author: Rebeca Villarraso

Class: ProcesImage
"""
import Image, ReadImage
import cv2
import pytesseract
from Image import *
from ReadImage import *
    
class ProcessImage(ReadImage, Image):       
    #pytesseract.pytesseract.tesseract_cmd = 'C:\\Users\\bfzjs\\AppData\\Local\\Programs\\Tesseract-OCR\\tesseract.exe'     
    def __init__(self, filename, filepath, py_path):
        Image.__init__(self, filename, filepath)   
        self.__tesseract_path=py_path
        pytesseract.pytesseract.tesseract_cmd = py_path
        
    def BGRtoGray(self):
        self.__gray=cv2.imread(self.get_filepath() + self.get_filename(), 0)
        return self.__gray
    
    def otsu_binarization(self):
        # Always force to open image in gray scale
        ret, imgf = cv2.threshold(self.BGRtoGray(), 0, 255, cv2.THRESH_BINARY+cv2.THRESH_OTSU)
        return imgf
           
    def get_code(self):
        self.__code=pytesseract.image_to_string(self.otsu_binarization(), lang='eng', config='--psm 6')
        return self.__code
