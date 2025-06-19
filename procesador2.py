#importamos numpy para manejar imagenes como arreglos bidimensionales para los calculos de los valores de los pixeles cada valor de RGB se multiplica por un peso
#y se suma para obtener el valor en gris
import numpy as np
# importamos PIL para el manejo de imagenes
from PIL import Image
import matplotlib.pyplot as plt

class ProcesadorImagen():
    def __init__(self,ruta_imagen=None):
        self.imagen = None
        self.imagen_gris = None
        self.imagen_array = None
        if ruta_imagen:
            self.Cargar_imagen(ruta_imagen)
    def Cargar_imagen(self,ruta_imagen):
        #pasamos la ruta donde se archiva la imagen    
        try:# exepcion para informar que la imagen no esta en la ruta dada
            
            self.imagen = Image.open(ruta_imagen)  #variable  que habre la imagen usando pillow
            self.imagen_gris =self.imagen.convert("L")#convierte la imagen en todos de grises 
            self.imagen_array= np.array(self.imagen_gris)#transforma la imagen en yuna matriz usando numpy
            return True
        except FileNotFoundError:
            print(f"la imagen en '{ruta_imagen}' no se encontro")
            return False #informa que la foto no se pudo cargar
    def procesar_Imagen(self):
        if self.imagen_array is None:
            print ("no se a cargado ninguna imagen")
            return None
        promedio=np.mean(self.imagen_array)
        print (f"el promedio de intensidad es : {promedio}")


procesador =ProcesadorImagen('C:/Users/marcelo/Downloads/fotoyo.jpg')
if procesador.imagen:
    promedio=procesador.procesar_Imagen()
else:
    print ("no se pudo cargar la imagen")

        
if procesador.imagen is not None:
          fig, axes = plt.subplots(1,2, figsize=(12, 6))
          axes[0].imshow(procesador.imagen_array, cmap='gray')
          axes[0].set_title("imgen en grises")
          axes[1].imshow(procesador.imagen, cmap='gray')
          axes[1].set_title("imgen  original")
plt.show()
                 