# -*- coding: utf-8 -*-
"""
Created on Sun Oct 06 14:00:00 2024

@author: Curso desarrollo ágil
"""

from Modelo.Camionetas_data import Camionetas_Data

class Gestor_Camionetas:
    def __init__(self, model):
        # Almacena el modelo recibido
        self.model = model
        self.camionetas_data = self.model.get_camionetas_data()  # Usa el método del modelo para obtener los datos de camionetas

    # Recibe y entrega la lista de camionetas activas
    def listar_camionetas_act(self):
        return self.camionetas_data.listar_camionetas_act()

    # Recibe y entrega la lista de camionetas inactivas
    def listar_camionetas_ina(self):
        return self.camionetas_data.listar_camionetas_ina()
