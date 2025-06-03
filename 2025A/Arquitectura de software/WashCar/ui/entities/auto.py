class Auto:
    def __init__(self):
        self.modelo = None
        self.marca = None
        self.placa = None
        self.duenio = None
        self.color = None
        self.anio = None
        self.es_plataforma = None
        self.costo_lavado= None
    
    def get_modelo(self):
        return self.modelo
    
    def set_modelo(self, modelo):
        self.modelo = modelo
        
    def get_marca(self):
        return self.marca
    
    def set_marca(self, marca):
        self.marca = marca  
    
    def get_placa(self):
        return self.placa
    
    def set_placa(self, placa):
        self.placa = placa
    
    def get_duenio(self):
        return self.duenio
    
    def set_duenio(self, duenio):
        self.duenio = duenio
    
    def get_color(self):
        return self.color
    
    def set_color(self, color):
        self.color = color
        
    def get_anio(self):
        return self.anio
    
    def set_anio(self, anio):
        self.anio = anio
        
    def get_es_plataforma(self):
        return self.es_plataforma
    
    def set_es_plataforma(self, es_plataforma):
        self.anio = es_plataforma
        
    def get_precio_lavado(self):
        return self.costo_lavado
    
    def set_precio_lavado(self, costo_lavado):
        self.costo_lavado = costo_lavado