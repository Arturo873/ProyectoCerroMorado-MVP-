# -*- coding: utf-8 -*-
"""
Created on Sun Oct  6 17:40:53 2024

@author: Carlos Luco Montofré
"""

# Camionetas_DAO.py
from Modelo.Lista_camionetas_DTO import Lista_Camionetas_DTO

class Camionetas_DAO:
    def __init__(self, conectorBD):
        self.conectorBD = conectorBD

    def registrar_camioneta(self, patente, marca, modelo, estado, kilometraje, año_fabrica, año_registro):
        try:
            sql_buscar_marca = "SELECT id FROM marcas WHERE nombre = %s"
            estado_marca, marca_id = self.conectorBD.ejecutarSelectOne(sql_buscar_marca, (marca,))

            if estado_marca != 0 or marca_id is None:
                if self.insertar_marca(marca) != 0:
                    print(f"Error al insertar la marca '{marca}'.")
                    return False
                estado_marca, marca_id = self.conectorBD.ejecutarSelectOne(sql_buscar_marca, (marca,))
                if estado_marca != 0 or marca_id is None:
                    print("Error al recuperar el ID de la marca después de insertarla.")
                    return False

            sql_insertar_camioneta = """
            INSERT INTO camionetas (patente, marca_id, modelo, estado, kilometraje, año_fabrica, año_registro)
            VALUES (%s, %s, %s, %s, %s, %s, %s)
            """
            params = (patente, marca_id[0], modelo, estado, kilometraje, año_fabrica, año_registro)
            estado_camioneta = self.conectorBD.ejecutarInsert(sql_insertar_camioneta, params)

            if estado_camioneta == 0:
                print("Camioneta registrada correctamente.")
                return True
            else:
                print("Error al registrar la camioneta.")
                return False

        except Exception as e:
            print(f"Excepción al registrar camioneta: {e}")
            return False

    def insertar_marca(self, marca):
        try:
            sql = "INSERT INTO marcas (nombre) VALUES (%s)"
            estado = self.conectorBD.ejecutarInsert(sql, (marca,))
            if estado == 0:
                print(f"Marca '{marca}' insertada correctamente.")
                return 0
            else:
                print(f"Error al insertar la marca '{marca}'.")
                return 1
        except Exception as e:
            print(f"Excepción al insertar marca: {e}")
            return 1

    def recupera_camionetas_act(self):
        """
        Recupera las camionetas activas de la base de datos.
        """
        lista_camionetas_DTO = Lista_Camionetas_DTO()
        sql = """
        SELECT c.patente, m.nombre AS marca, c.kilometraje
        FROM camionetas c
        INNER JOIN marcas m ON c.marca_id = m.id
        WHERE c.estado = TRUE
        """
        estado, camionetas = self.conectorBD.ejecutarSelectAll(sql)

        if estado == 0:
            for patente, marca, kilometraje in camionetas:
                lista_camionetas_DTO.set_unidad((patente, marca, kilometraje))
        else:
            print("Error al obtener camionetas activas.")

        return lista_camionetas_DTO

    def recupera_camionetas_ina(self):
        """
        Recupera las camionetas inactivas de la base de datos.
        """
        lista_camionetas_DTO = Lista_Camionetas_DTO()
        sql = """
        SELECT c.patente, m.nombre AS marca, c.kilometraje
        FROM camionetas c
        INNER JOIN marcas m ON c.marca_id = m.id
        WHERE c.estado = FALSE
        """
        estado, camionetas = self.conectorBD.ejecutarSelectAll(sql)

        if estado == 0:
            for patente, marca, kilometraje in camionetas:
                lista_camionetas_DTO.set_unidad((patente, marca, kilometraje))
        else:
            print("Error al obtener camionetas inactivas.")

        return lista_camionetas_DTO

