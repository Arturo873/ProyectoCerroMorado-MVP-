# -*- coding: utf-8 -*-
"""
Created on Sun Oct 06 14:00:00 2024

@author: Curso desarrollo ágil
"""

import tkinter as tk
from tkinter import ttk
from tkinter import messagebox  # Import necesario para mostrar mensajes


class VListar_Cam_Ina(tk.Toplevel):

    def __init__(self, *args, gestor_camionetas, **kwargs):

        super().__init__(*args, **kwargs)

        self.gestor_camionetas = gestor_camionetas

        # Dimensiones de la ventana
        start_width = 500
        min_width = 400
        start_height = 300
        min_height = 250
        posx = 300
        posy = 100

        # Posición de la ventana
        self.geometry(f"{start_width}x{start_height}+{posx}+{posy}")
        self.minsize(width=min_width, height=min_height)
        self.maxsize(width=min_width, height=min_height)

        # Título de la ventana
        self.title("Ventana listar camionetas inactivas")

        # Etiqueta del título visible en la ventana
        self.Label_titulo = tk.Label(self, text='Listado de camionetas inactivas')
        self.Label_titulo.place(x=200, y=20, width=200, anchor='center')

        # Lista donde se mostrarán las camionetas
        self.listaDatos = tk.Listbox(self, width=40, height=10)
        self.mostrar_camionetas()  # Llamada al método para mostrar camionetas
        self.listaDatos.place(x=100, y=50)

        # Botón para volver al menú de jefe de ventas
        self.boton_volver = ttk.Button(self,
                                       text="Volver al menú jefe de ventas",
                                       command=self.volver_menu)
        self.boton_volver.pack(side=tk.BOTTOM, pady=(10, 10))  # Posiciona el botón al final de la ventana

    def mostrar_camionetas(self):
        lista_camionetas_DTO = self.gestor_camionetas.listar_camionetas_ina()

        # Verificar si la lista está vacía
        if lista_camionetas_DTO.lenLista_camioneta() == 0:
            self.mostrar_mensaje("No hay camionetas inactivas registradas.")
        else:
            for i in range(0, lista_camionetas_DTO.lenLista_camioneta()):
                camioneta = lista_camionetas_DTO.getNext_camioneta()
                self.listaDatos.insert(i, f"Info: {camioneta}")

    def mostrar_mensaje(self, mensaje):
        messagebox.showinfo("Información", mensaje)

    def volver_menu(self):
        self.destroy()
        self.ventana.deiconify()

    def obj_ventana(self, ventana):
        self.ventana = ventana


        