# -*- coding: utf-8 -*-
"""
Created on Sun Oct 06 14:00:00 2024

@author: Curso desarrollo ágil
"""

from Presentador.main import Presenter
from Vista.Ventana_login import Vlogin


class View:
    
    def __init__(self):
        self.presenter = Presenter()
        self.vlogin = Vlogin()
        self.vlogin.inyectar_presenter(self.presenter)

                
    def start(self):
        self.vlogin.mainloop()