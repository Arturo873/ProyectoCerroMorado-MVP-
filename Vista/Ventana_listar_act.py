# -*- coding: utf-8 -*-
"""
Created on Sun Oct 06 14:00:00 2024

@author: Curso desarrollo ágil
"""
# Ventana_listar_act.py
import tkinter as tk
from tkinter import ttk

class VListar_Cam_Act(tk.Toplevel):

    def __init__(self, *args, gestor_camionetas, **kwargs):
        super().__init__(*args, **kwargs)

        self.gestor_camionetas = gestor_camionetas

        # Dimensiones de la ventana
        self.geometry("500x300+300+100")
        self.minsize(width=400, height=250)

        # Título de la ventana
        self.title("Ventana Listar Camionetas Activas")

        # Título visible en la ventana
        self.Label_titulo = tk.Label(self, text='Listado de camionetas activas')
        self.Label_titulo.place(x=250, y=20, width=200, anchor='center')

        # Lista donde se mostrarán las camionetas
        self.listaDatos = tk.Listbox(self, width=50, height=15)
        self.listaDatos.place(relx=0.5, rely=0.5, anchor='center')

        # Scrollbar
        scrollbar = tk.Scrollbar(self)
        scrollbar.place(relx=0.95, rely=0.5, anchor='center', height=200)
        self.listaDatos.config(yscrollcommand=scrollbar.set)
        scrollbar.config(command=self.listaDatos.yview)

        # Botón para volver
        self.boton_volver = ttk.Button(self, text="Volver al menú", command=self.volver_menu)
        self.boton_volver.pack(side=tk.BOTTOM, pady=(10, 10))

        self.mostrar_camionetas()

    def mostrar_camionetas(self):
        # Llamar al método correcto 'listar_camionetas_act'
        lista_camionetas_DTO = self.gestor_camionetas.listar_camionetas_act()  # CORRECCIÓN AQUÍ
        camionetas = lista_camionetas_DTO.get_all()  # Obtener todas las camionetas
        for camioneta in camionetas:
            self.listaDatos.insert(tk.END, f"Patente: {camioneta[0]}, Marca: {camioneta[1]}, Kilometraje: {camioneta[2]}")

    def volver_menu(self):
        self.destroy()
        self.ventana.deiconify()

    def obj_ventana(self, ventana):
        self.ventana = ventana





        
        