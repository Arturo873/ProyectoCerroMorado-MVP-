# -*- coding: utf-8 -*-
"""
Created on Sun Oct 06 14:00:00 2024

@author: Curso desarrollo ágil
"""

import tkinter as tk
from tkinter import ttk
from Vista.Ventana_listar_act import VListar_Cam_Act
from Vista.Ventana_listar_ina import VListar_Cam_Ina
from Vista.Ventana_listar_marcas import VListar_Marcas
from Vista.Ventana_registro_camionetas import VRegistroCamioneta  # Importar la ventana de registro de camionetas

class VMenu_Jf(tk.Tk):
    def __init__(self, *args, presenter, gestor_camionetas, **kwargs):
        super().__init__(*args, **kwargs)

        self.presenter = presenter
        self.gestor_camionetas = gestor_camionetas

        # Dimensiones de la ventana
        self.geometry("500x300+300+100")
        self.minsize(width=400, height=250)

        # Título de la ventana
        self.title("Gestión Jefe de Flota")

        # Título visible en la ventana (centrado)
        self.Label_titulo = tk.Label(self, text='Menú Jefe de Flota', font=("Helvetica", 16))
        self.Label_titulo.place(relx=0.5, rely=0.1, anchor='center')

        # Botón Camionetas Activas (centrado y más cerca)
        self.boton_camionetas_activas = ttk.Button(self, text="Ver camionetas ACTIVAS", command=self.abrir_ventana_listar_act)
        self.boton_camionetas_activas.place(relx=0.5, rely=0.2, anchor='center', width=200)

        # Botón Camionetas Inactivas (centrado y más cerca)
        self.boton_camionetas_inactivas = ttk.Button(self, text="Ver camionetas INACTIVAS", command=self.abrir_ventana_listar_ina)
        self.boton_camionetas_inactivas.place(relx=0.5, rely=0.4, anchor='center', width=200)

        # Botón Marcas de Camionetas (centrado y más cerca)
        self.boton_marca_camionetas = ttk.Button(self, text="Ver Marcas de Camionetas", command=self.abrir_ventana_listar_marcas)
        self.boton_marca_camionetas.place(relx=0.5, rely=0.6, anchor='center', width=200)

        # Botón Registrar Camioneta (centrado y más cerca)
        self.boton_registrar_camioneta = ttk.Button(self, text="Registrar Camioneta", command=self.abrir_ventana_registro)
        self.boton_registrar_camioneta.place(relx=0.5, rely=0.8, anchor='center', width=200)

        # Botón salir (centrado)
        self.boton_cerrar = ttk.Button(self, text="Salir", command=self.destroy)
        self.boton_cerrar.pack(side=tk.BOTTOM, pady=(10, 10))

    def abrir_ventana_listar_act(self):
        self.vlistar_cam_act = VListar_Cam_Act(gestor_camionetas=self.gestor_camionetas)
        self.vlistar_cam_act.obj_ventana(self)
        self.withdraw()

    def abrir_ventana_listar_ina(self):
        self.vlistar_cam_ina = VListar_Cam_Ina(gestor_camionetas=self.gestor_camionetas)
        self.vlistar_cam_ina.obj_ventana(self)
        self.withdraw()

    def abrir_ventana_listar_marcas(self):
        self.vlistar_marcas = VListar_Marcas(gestor_camionetas=self.gestor_camionetas)
        self.vlistar_marcas.obj_ventana(self)
        self.withdraw()

    def abrir_ventana_registro(self):
        # Abrir la ventana de registro de camionetas
        self.vregistro_camioneta = VRegistroCamioneta(gestor_camionetas=self.gestor_camionetas)
        self.vregistro_camioneta.grab_set()  # Hacer la ventana modal

    def obj_ventana(self, ventana):
        self.ventana = ventana


