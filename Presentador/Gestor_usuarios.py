# -*- coding: utf-8 -*-
"""
Created on Thu Oct 31 18:26:37 2024

@author: Carlos Luco Montofré
"""



class Gestor_Usuarios:
        
    def __init__(self, model):
        self.model = model
        pass
    
    def validar_datos(self, usuario_DTO):
        pass
    
    def Validar_credenciales(self, usuario_DTO):
        password = usuario_DTO.getPassword()

        estado, usuario_DTO = self.model.get_usuarios_DAO().recuperar_usuario(usuario_DTO)
        
                
        if estado == 0:
            if usuario_DTO.getPassword() == password:
                return 0, usuario_DTO
            else:
                return 1, usuario_DTO

        return 2, usuario_DTO
    
