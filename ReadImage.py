# -*- coding: utf-8 -*-
"""
Created on Sat Apr 15 09:46:30 2023

@author: bfzjs

Class: ReadImage
"""
import Image
import cv2
from Image import *
  
class ReadImage(Image):
    def __init__(self, filename, filepath):
        Image.__init__(self, filename, filepath)
        self.__image=cv2.imread(self.get_path())

    def ShowImage(self):
        cv2.imshow(self.get_filename(), self.__image)
        cv2.waitKey(0)
        cv2.destroyAllWindows()
        
    def Shape(self):
        self.__height=self.__image.shape[0]
        self.__width=self.__image.shape[1]
        self.__channels=self.__image.shape[2]
        return (self.__height, self.__width, self.__channels)