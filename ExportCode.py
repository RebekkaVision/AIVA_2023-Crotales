# -*- coding: utf-8 -*-
"""
Created on Sat Apr 15 09:57:25 2023

@author: bfzjs

Class: ExportCode
"""

class ExportCode:
    def __init__(self, image_name, dest_path, code):
        self.__txt_name=image_name.replace('.tif', '.txt')
        self.__dest_path=dest_path
        self.__code=code
        
    def getDestinationPath(self):
        return self.__dest_path
    
    def saveCodetoTxt(self):
        print('Code extracted in file: ', self.__txt_name)
        full_path=self.__dest_path+ self.__txt_name
        txt_file = open(full_path, 'w')
        txt_file.write(self.__code)
        txt_file.close()