# -*- coding: utf-8 -*-
"""
Created on Thu Oct 31 19:14:24 2024

@author: Carlos Luco Montofré
"""

import tkinter as tk
from tkinter import ttk
from Vista.Ventana_menu_jf import VMenu_Jf
from Vista.Ventana_menu_sf import VMenu_Sf
from Modelo.Usuario_DTO import Usuario_DTO
import sys
class Vlogin(tk.Tk):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # Configuración de la ventana
        start_width = 500
        min_width = 400
        start_height = 300
        min_height = 400
        posx = 300
        posy = 100
        self.geometry(f"{start_width}x{start_height}+{posx}+{posy}")
        self.minsize(width=min_width, height=min_height)
        self.maxsize(width=min_width, height=min_height)

        self.title("Sistema Gestión Camionetas")

        # Componentes de la interfaz
        self.Label_titulo = tk.Label(self, text='Login del Sistema')
        self.Label_titulo.place(x=200, y=50, width=300, anchor='center')

        self.Label_usuario = tk.Label(self, text='Usuario', anchor='center')
        self.Label_usuario.place(x=20, y=100, width=70)

        self.campo_usuario = ttk.Entry(self)
        self.campo_usuario.place(x=130, y=100, width=160)

        self.Label_password = tk.Label(self, text='Password', anchor='center')
        self.Label_password.place(x=50, y=160, width=100, anchor='center')

        self.campo_password = ttk.Entry(self, show="*")
        self.campo_password.place(x=130, y=150, width=160)

        self.campo_mensaje = ttk.Entry(self, state="readonly")
        self.campo_mensaje.place(x=130, y=180, width=160)

        self.boton_ingresar = ttk.Button(self, text="Ingresar aplicación", command=self.abrir_ventana_menu)
        self.boton_ingresar.place(x=75, y=250)

        self.boton_cerrar = ttk.Button(self, text="Cerrar aplicación", command=self.cerrar_aplicacion)
        self.boton_cerrar.place(x=75, y=350)

    # Lógica para abrir la ventana de menú según el usuario
    def abrir_ventana_menu(self):
        usuario = self.campo_usuario.get()
        password = self.campo_password.get()
        usuario_DTO = Usuario_DTO(usuario, password)
        estado, usuario_DTO = self.presenter.get_gestor_usuarios().Validar_credenciales(usuario_DTO)

        if estado == 0:
            self.campo_usuario.delete(0, tk.END)
            self.campo_password.delete(0, tk.END)
            self.campo_mensaje.delete(0, tk.END)

            if usuario_DTO.getCategoria() == 1:  # Jefe de Flota
                self.vMenu_Jf = VMenu_Jf(
                    presenter=self.presenter,
                    gestor_camionetas=self.presenter.get_gestor_camionetas()
                )
                self.vMenu_Jf.obj_ventana(self)

            elif usuario_DTO.getCategoria() == 2:  # Supervisor de Flota
                self.vMenu_Sf = VMenu_Sf(
                    presenter=self.presenter,
                    gestor_camionetas=self.presenter.get_gestor_camionetas()  # Asegúrate de pasar el gestor aquí
                )
                self.vMenu_Sf.obj_ventana(self)

            self.withdraw()

        elif estado == 1:
            self.campo_mensaje.config(state='NORMAL')
            self.campo_mensaje.delete(0, tk.END)
            self.campo_mensaje.insert(0, "Password incorrecta")
            self.campo_mensaje.config(state='readonly')

        elif estado == 2:
            self.campo_mensaje.config(state='NORMAL')
            self.campo_mensaje.delete(0, tk.END)
            self.campo_mensaje.insert(0, "El usuario no existe")
            self.campo_mensaje.config(state='readonly')

    def cerrar_aplicacion(self):

        self.destroy()
        sys.exit()#cierra la ejecucion del programa

    # Inyecta el presenter
    def inyectar_presenter(self, presenter):
        self.presenter = presenter
