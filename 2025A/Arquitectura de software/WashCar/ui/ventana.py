import tkinter as tk
from entities.usuario import Usuario
from entities.auto_camioneta import Auto_Camioneta
from entities.auto_chico import Auto_Chico
from core.logica import Logica


class Ventana():
    def __init__(self):
        self.ventana = tk.Tk()
        self.ventana.title("Lavado de autos")
        self.ventana.geometry("400x300")
        self.lbltitulo = tk.Label(self.ventana, text="Wash Car")
        self.lbltitulo.place(x=90, y=10,width=150, height=25)
        self.lblMarca = tk.Label(self.ventana,text="Marca")
        self.lblMarca.place(x=30, y=30,width=150, height=25)
        self.lblModelo = tk.Label(self.ventana,text="Modelo")
        self.lblModelo.place(x=30, y=70,width=150, height=25)
        self.lblPlaca = tk.Label(self.ventana,text="Placa")
        self.lblPlaca.place(x=30, y=100,width=150, height=25)
        self.lblDuenio = tk.Label(self.ventana,text="Nombre del Cliente")
        self.lblDuenio.place(x=30, y=130,width=150, height=25)
        self.lblColor = tk.Label(self.ventana,text="Color del vehiculo")
        self.lblColor.place(x=30, y=160,width=150, height=25)
        self.txtMarca = tk.Entry(self.ventana)
        self.txtMarca.place(x=150, y=30,width=150, height=25)
        self.txtModelo = tk.Entry(self.ventana)
        self.txtModelo.place(x=150, y=70,width=150, height=25)
        self.txtPlaca = tk.Entry(self.ventana)
        self.txtPlaca.place(x=150, y=100,width=150, height=25)
        self.txtDuenio = tk.Entry(self.ventana)
        self.txtDuenio.place(x=150, y=130,width=150, height=25)
        self.txtColor = tk.Entry(self.ventana)
        self.txtColor.place(x=150, y=160,width=150, height=25)
        self.variable2 = tk.IntVar()
        self.chkPlataforma = tk.Checkbutton(self.ventana, variable=self.variable2, onvalue=1, text="Es plataforma")
        self.chkPlataforma.place(x=30, y=190,width=150, height=25)
        self.variable1 = tk.IntVar()
        self.chkTipoAuto = tk.Checkbutton(self.ventana, variable=self.variable1, onvalue=1,text="Tipo de auto")
        self.chkTipoAuto.place(x=30, y=220,width=150, height=25)
        self.btnGuardar = tk.Button(self.ventana, text="Registrar", command=self.registrar)
        self.btnGuardar.place(x=30, y=250,width=150, height=25)
        self.lblCostoPago = tk.Label(self.ventana, text="Costo de lavado")
        self.lblCostoPago.place(x=200, y=250,width=150, height=25)
        self.ventana.mainloop()
        
    def registrar(self):
        marca = self.txtMarca.get()
        modelo = self.txtModelo.get()
        placa = self.txtPlaca.get()
        duenio = self.txtDuenio.get()
        color = self.txtColor.get()
        es_plataforma = self.variable2.get()
        tipo_auto = self.variable1.get()
        auto = None
        if tipo_auto == 1:
            auto = Auto_Chico()
        else:
            auto = Auto_Camioneta()
        auto.set_marca(marca)
        auto.set_modelo(modelo) 
        auto.set_placa(placa)
        auto.set_duenio(duenio)
        auto.set_color(color)
        auto.set_es_plataforma(es_plataforma)
        usuario = Usuario(auto)
        logica = Logica()
        logica.primer_paso(usuario)
        costo_pago = logica.segundo_paso()  
        self.lblCostoPago.config(text=f"Costo de lavado: {costo_pago}")
        logica.tercer_paso(4)  
        
        
        
        
        
ventana = Ventana()
