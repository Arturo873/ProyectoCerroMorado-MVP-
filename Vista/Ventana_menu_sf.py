# -*- coding: utf-8 -*-
"""
Created on Sun Oct 06 14:00:00 2024

@author: Curso desarrollo ágil
"""

import tkinter as tk
from tkinter import ttk
from Vista.Ventana_listar_klm import Vlistar_Klm_Act  # Importa la ventana de listado por kilometraje

class VMenu_Sf(tk.Tk):
    def __init__(self, *args, presenter, gestor_camionetas, **kwargs):
        super().__init__(*args, **kwargs)
        self.presenter = presenter  # Referencia al Presenter
        self.gestor_camionetas = gestor_camionetas  # Referencia al gestor de camionetas

        # Configuración de dimensiones de la ventana
        start_width = 500
        min_width = 400
        start_height = 300
        min_height = 400
        posx = 300
        posy = 100

        self.geometry(f"{start_width}x{start_height}+{posx}+{posy}")
        self.minsize(width=min_width, height=min_height)
        self.maxsize(width=min_width, height=min_height)

        self.title("Gestión Supervisor de Flota")

        # Título visible en la ventana
        self.Label_titulo = tk.Label(self, text='Menú Supervisor de Flota')
        self.Label_titulo.place(x=200, y=50, width=300, anchor='center')

        # Botón para listar camionetas por kilometraje
        self.boton_listar_kilometraje = ttk.Button(
            self,
            text="Ver Camionetas por Kilometraje",
            command=self.abrir_ventana_listar_klm
        )
        self.boton_listar_kilometraje.place(x=150, y=100)

        # Botón para cerrar la aplicación
        self.boton_cerrar = ttk.Button(
            self,
            text="Salir aplicación",
            command=self.salir_aplicacion
        )
        self.boton_cerrar.place(x=150, y=200)

    # Método para abrir la ventana de listado por kilometraje
    def abrir_ventana_listar_klm(self):
        self.vlistar_klm_act = Vlistar_Klm_Act(gestor_camionetas=self.gestor_camionetas)
        self.vlistar_klm_act.obj_ventana(self)
        self.withdraw()

    # Método para cerrar la ventana y volver a la ventana principal
    def salir_aplicacion(self):
        self.destroy()
        self.ventana.deiconify()

    # Método para configurar la ventana padre
    def obj_ventana(self, ventana):
        self.ventana = ventana
