# -*- coding: utf-8 -*-
"""
Created on Sun Oct 06 14:00:00 2024

@author: Curso desarrollo ágil
"""

# Lista_camionetas_DTO.py
class Lista_Camionetas_DTO:

    def __init__(self):
        self.lista_camionetas = []
        self.posicion = -1  # Esta variable indica la posición actual en la lista

    def __iter__(self):
        self.posicion = -1  # Reiniciamos la posición para empezar desde el principio
        return self

    def __next__(self):
        # Incrementamos la posición y verificamos si hay más elementos en la lista
        self.posicion += 1
        if self.posicion < len(self.lista_camionetas):
            return self.lista_camionetas[self.posicion]
        else:
            raise StopIteration  # Lanza la excepción cuando se termina la lista

    # Método para agregar una camioneta a la lista
    def set_unidad(self, camioneta):
        self.lista_camionetas.append(camioneta)

    # Método para obtener la longitud de la lista
    def lenLista_camioneta(self):
        return len(self.lista_camionetas)

    # Método para obtener todas las camionetas de una vez
    def get_all(self):
        """
        Devuelve todas las camionetas de la lista.
        """
        return self.lista_camionetas





