from .auto import Auto

class Auto_Chico(Auto):
    def __init__(self, costo_lavado=150): 
        self.subcategoria = None
        self.set_precio_lavado(costo_lavado)
        
    def get_subcategoria(self):
        return self.subcategoria
    
    def set_subcategoria(self, subcategoria):
        self.subcategoria = subcategoria