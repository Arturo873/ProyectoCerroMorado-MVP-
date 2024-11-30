# -*- coding: utf-8 -*-
"""
Created on Tue Oct  8 10:20:31 2024

@author: Carlos Luco Montofré
"""


class Usuario_DAO:

    def __init__(self, conectorBD) -> None:

        self.conectorBD = conectorBD


    def recuperar_usuario(self, usuario_DTO):
        estado = self.conectorBD.activarConexion()

        if estado == 66:
            del self.conectorBD
            return estado, None
        
        sql = "select password, categoria from usuarios where usuario = '{}'".format(usuario_DTO.getUsuario())
        estado, datos = self.conectorBD.ejecutarSelectOne(sql)

        if estado == 0:
            if datos:

                usuario_DTO.setPassword(datos[0])
                usuario_DTO.setCategoria(datos[1])
            else:    
                usuario_DTO.setPassword(None)
                usuario_DTO.setCategoria(None)
                estado = 2

        self.conectorBD.desactivarConexion()

        return estado, usuario_DTO
