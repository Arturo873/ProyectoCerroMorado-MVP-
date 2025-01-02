

import tkinter as tk
from tkinter import ttk
from tkinter import messagebox  # Para mostrar mensajes

class VListar_Marcas(tk.Toplevel):
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

        self.title("Listado de Marcas de Camionetas")

        # Etiqueta del título
        self.Label_titulo = tk.Label(self, text='Marcas de Camionetas')
        self.Label_titulo.place(x=200, y=20, width=300, anchor='center')

        # Lista para mostrar las marcas de las camionetas
        self.listaMarcas = tk.Listbox(self, width=50, height=10)
        self.mostrar_marcas()
        self.listaMarcas.place(x=50, y=50)

        # Botón para volver al menú
        self.boton_volver = ttk.Button(self, text="Volver al Menú", command=self.volver_menu)
        self.boton_volver.pack(side=tk.BOTTOM, pady=(10, 10))

    def mostrar_marcas(self):
        """
        Obtiene las camionetas del gestor y muestra solo las marcas
        """
        # Usar el método correcto listar_camionetas_act para obtener todas las camionetas activas
        lista_camionetas_DTO = self.gestor_camionetas.listar_camionetas_act()  # CORRECCIÓN AQUÍ
        cantidad = lista_camionetas_DTO.lenLista_camioneta()

        if cantidad == 0:
            self.mostrar_mensaje("No hay camionetas registradas.")
            return

        marcas = set()  # Usamos un set para evitar marcas duplicadas
        # Iterar sobre la lista completa de camionetas usando get_all()
        for camioneta in lista_camionetas_DTO.get_all():
            marcas.add(camioneta[1])  # Asumimos que el índice 1 es la marca

        # Mostrar las marcas en la lista
        for marca in marcas:
            self.listaMarcas.insert(tk.END, marca)

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


