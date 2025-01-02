# -*- coding: utf-8 -*-
"""
Created on Sun Oct 06 14:00:00 2024

@author: Curso desarrollo ágil
"""

from Modelo.ConectorBD import ConectorBD
from Modelo.Usuario_DAO import Usuario_DAO
from Modelo.Camionetas_data import Camionetas_Data

class Model:
    def __init__(self):
        # Conexión con la base de datos actualizada según tus parámetros
        self.conectorBD = ConectorBD(
            hostdb="localhost",      # Cambiado a "hostdb" para coincidir con ConectorBD
            userdb="root",           # Cambiado a "userdb"
            passwordb="root",        # Cambiado a "passwordb"
            basedatosdb="dbminera",  # Cambiado a "basedatosdb"
            port=3306
        )
        self.usuarios_DAO = Usuario_DAO(self.conectorBD)
        self.camionetas_data = Camionetas_Data()

    def get_usuarios_DAO(self):
        return self.usuarios_DAO

    def get_camionetas_data(self):
        return self.camionetas_data
