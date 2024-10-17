# -*- coding: utf-8 -*-
"""
Created on Sun Oct 06 14:00:00 2024

@author: Curso desarrollo ágil
"""

from Modelo.Camionetas_data import Camionetas_Data

class Model:
    
    def __init__(self):
        self.camionetas_data = Camionetas_Data()
        
    def get_camionetas_data(self):
        return self.camionetas_data