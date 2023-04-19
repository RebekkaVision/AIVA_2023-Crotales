# -*- coding: utf-8 -*-
"""
Created on Sat Apr 15 09:46:01 2023

@author: bfzjs

Class: Image
"""

class Image:
    """ 
        Clase que define al objeto imagen
    """ 
    #Constructor 
    def __init__(self, filepath, filename):
        self.__filename=filename
        self.__filepath=filepath
        self.__path=self.__filename+self.__filepath
       
    def get_filename(self):
        return self.__filename

    def get_filepath(self):
        return self.__filepath
    
    def get_path(self):
        return self.__filepath + self.__filename