# -*- coding: utf-8 -*-
"""
Created on Sun Oct 06 14:00:00 2024

@author: Curso desarrollo ágil
"""
from Modelo.Camionetas_data import Camionetas_Data

class Gestor_Camionetas:
    
    def __init__(self):
        self.camionetas_data=Camionetas_Data
    
    #recibe y entrega la lista de camionetas activas
    def listar_camionetas_act(self):
        return self.camionetas_data.listar_camionetas_act()

    #recibe y entrega la lista de camionetas inactivas
    def listar_camionetas_ina(self):
        return self.camionetas_data.listar_camionetas_ina()

             
    def inyectar_camionetas_data(self, camionetas_data):
        self.camionetas_data = camionetas_data
