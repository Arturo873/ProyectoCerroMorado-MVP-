# -*- coding: utf-8 -*-
"""
Created on Thu Oct 31 17:55:51 2024

@author: Carlos Luco Montofré
"""

class Usuario_DTO:

    def __init__(self, usuario, password, categoria = None):
        self.usuario = usuario
        self.password = password
        self.categoria = categoria
        
        
    def setUsuario(self, usuario):
        self.usuario = usuario
                      
    def setPassword(self, password):
        self.password = password
                            
    def setCategoria(self, categoria):
        self.categoria = categoria
        
    def getUsuario(self):
        return self.usuario
    
    def getPassword(self):
        return self.password
        
    def getCategoria(self):
        return self.categoria