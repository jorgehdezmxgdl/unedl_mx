
from .auto import Auto


class Auto_Camioneta(Auto):
    def __init__(self, costo_lavado=300):
        self.doblecabina = None
        self.set_precio_lavado(costo_lavado)
     
    def get_doblecabina(self):
        return self.doblecabina
    
    def set_doblecabina(self, doblecabina):
        self.doblecabina = doblecabina   
    
     