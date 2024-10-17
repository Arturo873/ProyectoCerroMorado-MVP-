# -*- coding: utf-8 -*-
"""
Created on Sun Oct 06 14:00:00 2024

@author: Curso desarrollo ágil
"""

from Modelo.main import Model
from Presentador.Gestor_camionetas import Gestor_Camionetas

class Presenter:
    
    def __init__(self):
        self.model = Model()
        self.gestor_camionetas = Gestor_Camionetas()
        self.gestor_camionetas.inyectar_camionetas_data(self.model.get_camionetas_data())
        
    def get_gestor_camionetas(self):
        return self.gestor_camionetas