# -*- coding: utf-8 -*-
"""
Created on Sun Oct 06 14:00:00 2024

@author: Curso desarrollo ágil
"""

import tkinter as tk
from tkinter import ttk


from Vista.Ventana_listar_act import VListar_Cam_Act
from Vista.Ventana_listar_ina import VListar_Cam_Ina

class VMenu_Jf(tk.Tk):
    
    def __init__(self, *args, **kwargs):
        
        super().__init__(*args, **kwargs)

        #dimensiones de la ventana
        start_width  = 500
        min_width    = 400
        start_height = 300
        min_height   = 250
        posx = 300
        posy = 100
        #posicion de la ventana
        self.geometry(f"{start_width}x{start_height}+{posx}+{posy}")
        self.minsize(width=min_width, height=min_height)
        self.maxsize(width=min_width, height=min_height)
        
        #nombre de la ventana
        self.title("ventana_principal")

        #titulo visible en la ventana
        self.Label_titulo = tk.Label(self, text ='Menu Jefe de Ventas')
        self.Label_titulo.place(x=200, y=20, width=200, anchor='center')#posicion del btn

        #boton Camionetas activas
        self.boton_camionetas_activas = ttk.Button(self,
            text="Ver camionetas ACTIVAS", 
            command=self.abrir_ventana_listar_act)
        self.boton_camionetas_activas.place(x=150, y=50)#posicion del btn

        #boton Camionetas inactivas
        self.boton_camionetas_inactivas = ttk.Button(self,
            text="Ver camionetas INACTIVAS", 
            command=self.abrir_ventana_listar_ina)
        self.boton_camionetas_inactivas.place(x=150, y=90)#posicion del btn

    
        #boton cerrar
        self.boton_cerrar = ttk.Button(self,
            text="Salir", 
            command=self.destroy)
        self.boton_cerrar.pack(side=tk.BOTTOM, pady=(10, 10))#posicion el btn al final de la ventana


        
    def abrir_ventana_listar_act(self):
        self.vlistar_cam_act = VListar_Cam_Act(gestor_camionetas= self.gestor_camionetas)
        self.vlistar_cam_act.obj_ventana(self)
        self.withdraw()
        
            
    def abrir_ventana_listar_ina(self):
        self.vlistar_cam_ina = VListar_Cam_Ina(gestor_camionetas= self.gestor_camionetas)
        self.vlistar_cam_ina.obj_ventana(self)
        self.withdraw()

        
    def cerrar_aplicacion(self):
        self.destroy()
        self.ventana.destroy()


    def inyectar_gestor(self, gestor_camionetas):
        self.gestor_camionetas = gestor_camionetas