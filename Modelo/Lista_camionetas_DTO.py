# -*- coding: utf-8 -*-
"""
Created on Sun Oct 06 14:00:00 2024

@author: Curso desarrollo ágil
"""


class Lista_Camionetas_DTO:

    def __init__(self):
        self.posicion = -1
        self.lista_camionetas = []

    # entrega la camioneta en la siguiente posicion
    def getNext_camioneta(self):
        self.posicion += 1
        return self.lista_camionetas[self.posicion]

    # agrega una camioneta a la lista
    def set_unidad(self, camioneta):
        self.lista_camionetas.append(camioneta)

    # retorna el tamanño de la lista
    def lenLista_camioneta(self):
        return len(self.lista_camionetas)
