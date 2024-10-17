# -*- coding: utf-8 -*-
"""
Created on Sun Oct 06 14:00:00 2024

@author: Curso desarrollo ágil
"""

import tkinter as tk
from tkinter import ttk


class VListar_Cam_Act(tk.Toplevel):
    
    def __init__(self, *args, gestor_camionetas, **kwargs):
        
        super().__init__(*args, **kwargs)
        
        self.gestor_camionetas=gestor_camionetas
        
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
        
        #titulo
        self.title("ventana listar Act")

        #titulo visible en la ventana
        self.Label_titulo = tk.Label(self, text ='Listado de camionetas activas')
        self.Label_titulo.place(x=200, y=20, width=200, anchor='center')

        #lista donde se mostraran las camionetas
        self.listaDatos=tk.Listbox(self,width=40, height=10)
        self.mostrar_camionetas()
        self.listaDatos.place(x=100,y=50)
        

        #boton volver al menu de jefe de ventas
        self.boton_volver = ttk.Button(self,
            text="Volver menu jefe de ventas", 
            command=self.volver_menu)
        self.boton_volver.pack(side=tk.BOTTOM, pady=(10, 10))#posicion el btn al final de la ventana

        
    def mostrar_camionetas(self):
        lista_camionetas_DTO = self.gestor_camionetas.listar_camionetas_act()
        cantidad=lista_camionetas_DTO.lenLista_camioneta()#cantidad de elementos dentro de la lista
        for i in range(0,cantidad):
            camioneta=lista_camionetas_DTO.getNext_camioneta()
            self.listaDatos.insert(i,f"Info: {camioneta}")
        
 
        
    def mostrar_mensaje(self):
        pass

           
    def volver_menu(self):
        self.destroy()
        self.ventana.deiconify()
        
               
    def obj_ventana(self, ventana):
        self.ventana = ventana

        
        