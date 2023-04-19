# -*- coding: utf-8 -*-
"""
Created on Sat Apr 15 09:46:01 2023

@author: bfzjs

Class: Image
"""
import os
import Image
from Image import *

class ExtractCode(Image):      
    def __init__(self, filename, filepath, dest_path):
        Image.__init__(self, filename, filepath)
        self.__dest_path=dest_path
   
    def Ejecutar(self):
        error=0
        if not '.tif' in self.get_filename():
            print('Formato de imagen incorrecto')   
            error=1
            #raise Exception('Formato de imagen incorrecto')
        if not os.path.isdir(self.get_filepath()):
            print('La ruta especificada de la imagen no existe')
            error=1
            #raise Exception('La ruta especificada de la imagen no existe')
        if not os.path.isfile(self.get_filepath() + self.get_filename()):
            print('Imagen no encontrada o no es válida')
            error=1
            #raise Exception('Imagen no encontrada')
        if not os.path.isdir(self.__dest_path):
            print ('Ruta destino no existe')
            error=1
            #raise Exception('Ruta destino no existe')
        return error