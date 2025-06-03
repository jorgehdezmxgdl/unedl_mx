import datetime

class Logica:
    def __init__(self):
        self.usuario = None
    
    def primer_paso(self, usuario):
        self.usuario = usuario
        
    def segundo_paso(self):
        self.usuario.visitas = self.usuario.visitas + 1
        self.usuario.fecha_registro = datetime.datetime.now()
        pago = self.usuario.auto.get_costo_lavado()
        if self.usuario.auto.get_es_plataforma():
            if self.usuario.historial >= 4:
                pago *= .9 
        return pago
           
    def tercer_paso(self, puntaje):
        self.usuario.historial += 1
        self.usuario.calificacion = puntaje