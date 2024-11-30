# -*- coding: utf-8 -*-
"""
Created on Tue Oct  8 10:01:03 2024

@author: Carlos Luco Montofré
"""

import mysql.connector
from mysql.connector import Error

class ConectorBD:

    def __init__(self, hostdb, userdb, passwordb, basedatosdb, port=3306):
        self.__hostdb = hostdb
        self.__userdb = userdb
        self.__passwordb = passwordb
        self.__basedatosdb = basedatosdb
        self.__port = port
        self.conexion = None
        self.cursor = None

    def activarConexion(self):
        try:
            # Conexión a la base de datos MySQL
            self.conexion = mysql.connector.connect(
                host=self.__hostdb,
                user=self.__userdb,
                password=self.__passwordb,
                database=self.__basedatosdb,
                port=self.__port
            )
            # Creación de un cursor para ejecutar consultas
            if self.conexion.is_connected():
                self.cursor = self.conexion.cursor()
                print("Conexión exitosa a la base de datos")
                return 0, "Conexión exitosa"
            else:
                return 66, "Conexión fallida"
        except Error as e:
            print(f"Error de conexión: {e}")
            return 66, e

    def ejecutarSelectOne(self, sql, params=None):
        try:
            if params:
                self.cursor.execute(sql, params)
            else:
                self.cursor.execute(sql)
            datos = self.cursor.fetchone()
            return 0, datos
        except Error as e:
            self.realizarRollback()
            return 1, e

    def ejecutarSelectAll(self, sql, params=None):
        try:
            if params:
                self.cursor.execute(sql, params)
            else:
                self.cursor.execute(sql)
            datos = self.cursor.fetchall()
            return 0, datos
        except Error as e:
            self.realizarRollback()
            return 1, e

    def ejecutarInsert(self, sql, params=None):
        try:
            if params:
                self.cursor.execute(sql, params)
            else:
                self.cursor.execute(sql)
            self.realizarCommit()
            return 0
        except Error as e:
            self.realizarRollback()
            return 1, e

    def ejecutarDelete(self, sql, params=None):
        try:
            if params:
                self.cursor.execute(sql, params)
            else:
                self.cursor.execute(sql)
            self.realizarCommit()
            return 0
        except Error as e:
            self.realizarRollback()
            return 1, e

    def ejecutarUpdate(self, sql, params=None):
        try:
            if params:
                self.cursor.execute(sql, params)
            else:
                self.cursor.execute(sql)
            self.realizarCommit()
            return 0
        except Error as e:
            self.realizarRollback()
            return 1, e

    def realizarCommit(self):
        try:
            self.conexion.commit()
        except Error as e:
            print(f"Error al hacer commit: {e}")

    def realizarRollback(self):
        try:
            self.conexion.rollback()
        except Error as e:
            print(f"Error al hacer rollback: {e}")

    def desactivarConexion(self):
        if self.cursor:
            self.cursor.close()
        if self.conexion:
            self.conexion.close()
        print("Conexión cerrada correctamente")
