# -*- coding: utf-8 -*-
"""
Created on Sun Oct  6 17:40:53 2024

@author: Carlos Luco Montofré
"""

from Modelo.Lista_camionetas_DTO import Lista_Camionetas_DTO

class Camionetas_DAO:
    
    def __init__(self):
        self.stock_camionetas = {}
        self.stock_camionetas["AA0001"]= {"estado":True,"marca":"changan","modelo":"hunter","añofabrica":2014,"añoregistro":2016,"kilometraje":5000}
        self.stock_camionetas["AA0002"]= {"estado":False,"marca":"chevrolet","modelo":"montana","añofabrica":2016,"añoregistro":2017,"kilometraje":7000}        
        self.stock_camionetas["AA0003"]= {"estado":True,"marca":"chevrolet","modelo":"silverado","añofabrica":2015,"añoregistro":2016,"kilometraje":6000}        
        self.stock_camionetas["AA0004"]= {"estado":True,"marca":"ford","modelo":"ranger","añofabrica":2020,"añoregistro":2020,"kilometraje":1000}

        
    def recupera_camionetas_act(self):
        lista_camionetas_DTO = Lista_Camionetas_DTO()        
               
        for patente in self.stock_camionetas.keys():
            data = self.stock_camionetas[patente]
            if data["estado"]:
                lista_camionetas_DTO.set_unidad((patente,data["marca"],data["kilometraje"]))
            
        return lista_camionetas_DTO
    
    
    def recupera_camionetas_ina(self):
        lista_camionetas_DTO = Lista_Camionetas_DTO()        
               
        for patente in self.stock_camionetas.keys():
            data = self.stock_camionetas[patente]
            if not data["estado"]:
                lista_camionetas_DTO.set_unidad((patente,data["marca"],data["kilometraje"]))
            
        return lista_camionetas_DTO        
        
        