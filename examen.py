from tkinter import ttk
from tkinter import *

class Desk:
    def __init__(self, window):
        # Initializations
        
        #ancho
        ancho = 800
        
        #alto
        alto = 600
        
        # asignamos la ventana a una variable de la clase llamada wind
        self.wind = window

        #le asignamos el ancho y el alto a la ventana con la propiedad geometry
        self.wind.geometry(str(ancho)+'x'+str(alto))

        #centramos el contenido 
        self.wind.columnconfigure(0, weight=1)
        
        #le damos un titulo a la ventana
        self.wind.title('Aplicación con interface gráfica en Python - By Ing. andrick')
        
        # creamos un contenedor
        frame = LabelFrame(self.wind, text = 'multiply 2 valores')
        frame.grid(row = 0, column = 0, columnspan = 3, pady = 20)
        
        # creamos un etiqueta
        Label(frame, text = 'primer numero: ').grid(row = 1, column = 0)
        
        #creamos un input donde ingresar valores
        str.var1 = Entry(frame)
        str.var1.focus()
        str.var1.grid(row = 1, column = 1)
        
        #creamos un input donde ingresar valores 3 
        str.var3 = Entry(frame)
        str.var3.focus()
        str.var3.grid(row = 1, column = 1)
        
        # igual que arriba una etiqueta y un campo input para ingresar valores
        Label(frame, text = 'segundo numero: ').grid(row = 2, column = 0)
        str.var2 = Entry(frame)
        str.var2.grid(row = 2, column = 1)
        
        #Creamos un boton para ejecutar la multiply
        Button(frame, text = 'multiply', command = self.multiply).grid(row = 3, columnspan = 2, sticky = W * E)

        #designamos un área para mensajes
        self.message = Label(text = '', fg = 'red')
        self.message.grid(row = 3, column = 0, columnspan = 2, sticky = W * E)
        
    # creamos una función para validar que los campos no esten en blanco
    def validation(self):
        return len(self.var1.get()) != 0 and len(self.var2.get()) != 0
    
    # esta es la función que ejecuta la multiplicacion
    def multiply(self):
        if self.validation():
            resultado = float( self.var1.get() ) * float( self.var3.get() )
            self.message['text'] = 'La multiply de las 2 variables es: {}'.format(resultado)
        else:
            self.message['text'] = 'los campos son requeridos'

#validamos si estamos en la aplicación inicial
if __name__ == '__main__':
    
    #asignamos la propiedad de tkinter a la variable window
    window = Tk()
    
    #en la variable app guardamos la clase Desk y le enviamos como parametro la ventana 
    app = "str"Desk(window)
    
    #ejecutamos un mainloop para que se ejecute la ventana
    window.mainloop()