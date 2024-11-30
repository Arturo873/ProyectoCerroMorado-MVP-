# -*- coding: utf-8 -*-
"""
Created on Sun Oct 06 14:00:00 2024

@author: Curso desarrollo ágil
"""

import tkinter as tk
from tkinter import ttk
from tkinter import messagebox  # Para mostrar mensajes

class Vlistar_Klm_Act(tk.Toplevel):
    def __init__(self, *args, gestor_camionetas, **kwargs):
        super().__init__(*args, **kwargs)

        self.gestor_camionetas = gestor_camionetas  # Referencia al gestor de camionetas

        # Configuración de la ventana
        start_width = 500
        min_width = 400
        start_height = 300
        min_height = 250
        posx = 300
        posy = 100

        self.geometry(f"{start_width}x{start_height}+{posx}+{posy}")
        self.minsize(width=min_width, height=min_height)
        self.maxsize(width=min_width, height=min_height)

        self.title("Listado de Camionetas por Kilometraje")

        # Etiqueta del título
        self.Label_titulo = tk.Label(self, text='Camionetas Ordenadas por Kilometraje')
        self.Label_titulo.place(x=200, y=20, width=300, anchor='center')

        # Lista para mostrar las camionetas
        self.listaDatos = tk.Listbox(self, width=50, height=10)
        self.mostrar_camionetas_por_kilometraje()
        self.listaDatos.place(x=50, y=50)

        # Botón para volver al menú
        self.boton_volver = ttk.Button(
            self,
            text="Volver al Menú",
            command=self.volver_menu
        )
        self.boton_volver.pack(side=tk.BOTTOM, pady=(10, 10))

    def mostrar_camionetas_por_kilometraje(self):
        """
        Obtiene camionetas del gestor, las ordena por kilometraje y las muestra.
        """
        lista_camionetas_DTO = self.gestor_camionetas.listar_camionetas_act()
        cantidad = lista_camionetas_DTO.lenLista_camioneta()

        if cantidad == 0:
            self.mostrar_mensaje("No hay camionetas registradas.")
            return

        camionetas = []
        for i in range(cantidad):
            camioneta = lista_camionetas_DTO.getNext_camioneta()
            camionetas.append(camioneta)

        # Ordenar las camionetas por kilometraje (índice 2 de cada tupla)
        camionetas.sort(key=lambda x: x[2])

        # Mostrar las camionetas en la lista
        for i, camioneta in enumerate(camionetas):
            self.listaDatos.insert(i, f"{camioneta[0]} - {camioneta[1]} - {camioneta[2]} km")

    def mostrar_mensaje(self, mensaje):
        """
        Muestra un mensaje en un cuadro de diálogo.
        """
        messagebox.showinfo("Información", mensaje)

    def volver_menu(self):
        """
        Cierra la ventana actual y vuelve al menú anterior.
        """
        self.destroy()
        self.ventana.deiconify()

    def obj_ventana(self, ventana):
        """
        Configura la ventana padre para poder deiconificarla al cerrar.
        """
        self.ventana = ventana
