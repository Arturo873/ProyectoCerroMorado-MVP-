# -*- coding: utf-8 -*-
"""
Created on Sun Oct 06 14:00:00 2024

@author: Curso desarrollo ágil
"""

from Modelo.Camionetas_DAO import Camionetas_DAO

class Camionetas_Data:
    
    def __init__(self):
        self.camionetas_DAO = Camionetas_DAO()
        
        
    def listar_camionetas_act(self):
        lista_camionetas_DTO = self.camionetas_DAO.recupera_camionetas_act()
        return lista_camionetas_DTO
        
        
    def listar_camionetas_ina(self):
        lista_camionetas_DTO = self.camionetas_DAO.recupera_camionetas_ina()        
        return lista_camionetas_DTO        
    


            
