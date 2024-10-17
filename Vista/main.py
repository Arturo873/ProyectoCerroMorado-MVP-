# -*- coding: utf-8 -*-
"""
Created on Sun Oct 06 14:00:00 2024

@author: Curso desarrollo ágil
"""

from Presentador.main import Presenter
from Vista.Ventana_menu_jf import VMenu_Jf

class View:
    
    def __init__(self):
        self.presenter = Presenter()
        self.vmenu_jf = VMenu_Jf()
        self.vmenu_jf.inyectar_gestor(self.presenter.get_gestor_camionetas())
        
        
        
    def start(self):
        self.vmenu_jf.mainloop()