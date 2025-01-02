# Ventana_registro_camionetas.py
import tkinter as tk
from tkinter import ttk, messagebox

class VRegistroCamioneta(tk.Toplevel):
    def __init__(self, gestor_camionetas, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.gestor_camionetas = gestor_camionetas  # Referencia al gestor de camionetas

        # Configuración de la ventana
        self.geometry("500x500+400+150")
        self.title("Registrar Nueva Camioneta")

        # Etiquetas y campos para la información de la camioneta
        self.label_marca = tk.Label(self, text="Marca:")
        self.label_marca.pack(pady=5)

        marcas = self.obtener_marcas()
        self.combo_marca = ttk.Combobox(self, values=marcas)
        self.combo_marca.pack(pady=5)

        self.label_modelo = tk.Label(self, text="Modelo:")
        self.label_modelo.pack(pady=5)
        self.entry_modelo = tk.Entry(self)
        self.entry_modelo.pack(pady=5)

        self.label_estado = tk.Label(self, text="Estado (Activo/Inactivo):")
        self.label_estado.pack(pady=5)
        self.combo_estado = ttk.Combobox(self, values=["Activo", "Inactivo"])
        self.combo_estado.pack(pady=5)
        self.combo_estado.set("Activo")

        self.label_ano_fabrica = tk.Label(self, text="Año de Fabricación:")
        self.label_ano_fabrica.pack(pady=5)
        self.entry_ano_fabrica = tk.Entry(self)
        self.entry_ano_fabrica.pack(pady=5)

        self.label_ano_registro = tk.Label(self, text="Año de Registro:")
        self.label_ano_registro.pack(pady=5)
        self.entry_ano_registro = tk.Entry(self)
        self.entry_ano_registro.pack(pady=5)

        self.label_kilometraje = tk.Label(self, text="Kilometraje:")
        self.label_kilometraje.pack(pady=5)
        self.entry_kilometraje = tk.Entry(self)
        self.entry_kilometraje.pack(pady=5)

        self.label_patente = tk.Label(self, text="Patente:")
        self.label_patente.pack(pady=5)
        self.entry_patente = tk.Entry(self)
        self.entry_patente.pack(pady=5)

        self.boton_guardar = ttk.Button(self, text="Registrar", command=self.registrar_camioneta)
        self.boton_guardar.pack(pady=10)

        self.boton_cancelar = ttk.Button(self, text="Cancelar", command=self.destroy)
        self.boton_cancelar.pack(pady=5)

    def obtener_marcas(self):
        """
        Obtiene las marcas disponibles llamando al gestor de camionetas.
        """
        marcas = self.gestor_camionetas.obtener_marcas()
        return marcas

    def registrar_camioneta(self):
        """
        Maneja el registro de una nueva camioneta.
        """
        marca = self.combo_marca.get()
        modelo = self.entry_modelo.get()
        estado = self.combo_estado.get()
        ano_fabrica = self.entry_ano_fabrica.get()
        ano_registro = self.entry_ano_registro.get()
        kilometraje = self.entry_kilometraje.get()
        patente = self.entry_patente.get()

        if not marca or not modelo or not ano_fabrica or not ano_registro or not kilometraje or not patente:
            messagebox.showerror("Error", "Todos los campos son obligatorios.")
            return

        camioneta = {
            "marca": marca,
            "modelo": modelo,
            "estado": estado,
            "ano_fabrica": ano_fabrica,
            "ano_registro": ano_registro,
            "kilometraje": kilometraje,
            "patente": patente
        }

        if self.gestor_camionetas.agregar_camioneta(camioneta):
            messagebox.showinfo("Éxito", "La camioneta se registró exitosamente.")
            self.destroy()
        else:
            messagebox.showerror("Error", "Hubo un problema al registrar la camioneta.")
