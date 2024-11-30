# -*- coding: utf-8 -*-
"""
Created on Sun Oct 06 14:00:00 2024

@author: Curso desarrollo ágil
"""

import tkinter as tk
from tkinter import ttk
from Vista.Ventana_listar_act import VListar_Cam_Act
from Vista.Ventana_listar_ina import VListar_Cam_Ina
from Vista.Ventana_listar_klm import Vlistar_Klm_Act  # Importar ventana de kilometraje

class VMenu_Jf(tk.Tk):
    def __init__(self, *args, presenter, gestor_camionetas, **kwargs):
        super().__init__(*args, **kwargs)

        self.presenter = presenter  # Referencia al presenter
        self.gestor_camionetas = gestor_camionetas  # Referencia al gestor de camionetas

        # Dimensiones de la ventana
        start_width = 500
        min_width = 400
        start_height = 300
        min_height = 250
        posx = 300
        posy = 100
        self.geometry(f"{start_width}x{start_height}+{posx}+{posy}")
        self.minsize(width=min_width, height=min_height)
        self.maxsize(width=min_width, height=min_height)

        # Nombre de la ventana
        self.title("Gestión Jefe de Flota")

        # Título visible en la ventana
        self.Label_titulo = tk.Label(self, text='Menú Jefe de Flota')
        self.Label_titulo.place(x=200, y=20, width=200, anchor='center')

        # Botón Camionetas Activas
        self.boton_camionetas_activas = ttk.Button(self,
                                                   text="Ver camionetas ACTIVAS",
                                                   command=self.abrir_ventana_listar_act)
        self.boton_camionetas_activas.place(x=150, y=50)

        # Botón Camionetas Inactivas
        self.boton_camionetas_inactivas = ttk.Button(self,
                                                     text="Ver camionetas INACTIVAS",
                                                     command=self.abrir_ventana_listar_ina)
        self.boton_camionetas_inactivas.place(x=150, y=90)

        # Botón para ver camionetas por kilometraje
        self.boton_camionetas_klm = ttk.Button(self,
                                               text="Ver Camionetas por Kilometraje",
                                               command=self.abrir_ventana_listar_klm)
        self.boton_camionetas_klm.place(x=150, y=130)

        # Botón cerrar
        self.boton_cerrar = ttk.Button(self, text="Salir", command=self.destroy)
        self.boton_cerrar.pack(side=tk.BOTTOM, pady=(10, 10))

    # Abre la ventana de listado de camionetas activas
    def abrir_ventana_listar_act(self):
        self.vlistar_cam_act = VListar_Cam_Act(gestor_camionetas=self.gestor_camionetas)
        self.vlistar_cam_act.obj_ventana(self)
        self.withdraw()

    # Abre la ventana de listado de camionetas inactivas
    def abrir_ventana_listar_ina(self):
        self.vlistar_cam_ina = VListar_Cam_Ina(gestor_camionetas=self.gestor_camionetas)
        self.vlistar_cam_ina.obj_ventana(self)
        self.withdraw()

    # Abre la ventana de camionetas por kilometraje
    def abrir_ventana_listar_klm(self):
        self.vlistar_klm_act = Vlistar_Klm_Act(gestor_camionetas=self.gestor_camionetas)
        self.vlistar_klm_act.obj_ventana(self)
        self.withdraw()

    # Método para configurar la ventana padre
    def obj_ventana(self, ventana):
        self.ventana = ventana
