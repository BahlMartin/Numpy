from PIL import Image
import matplotlib.pyplot as plt
from class_matriz import Matriz
class ProcesadorImagen():
    def __init__(self,imagen):
        self.imagen = imagen

    def Convertir_y_Mostrar_Imagen_gris(self):
        imagen_gris = self.imagen.convert("L")#convierte la imagen en todos de grises 
        imagen_gris_matriz= Matriz(imagen_gris)#transforma la imagen en yuna matriz usando numpy
        print (f"el promedio de intensidad es : {imagen_gris_matriz.promedio()}")
        self.comparar_imagen(imagen_gris_matriz.devolver_matriz())
        return None
    
    def mostrar_imagen(self,imagen=None):
        if imagen is None:
            self.imagen
            self.imagen.show()
        else:
            imagen.show()
        
    def comparar_imagen(self,imagen):
        fig, axes = plt.subplots(1,2, figsize=(12, 6))
        axes[0].imshow(imagen)
        axes[0].set_title("imagen comparada")
        axes[1].imshow(self.imagen)
        axes[1].set_title("imagen  original")
        plt.show()
        return None
    
    def Redimensionar(self, nuevo_ancho, nuevo_alto):
        print(f"imagen original: {self.imagen.size}")
        self.imagen = self.imagen.resize((nuevo_ancho, nuevo_alto))
        print(f"Imagen redimensionada a: {nuevo_ancho} x {nuevo_alto}")
        return self.imagen

    def binarizar_pixel_gris(self,x):
        # Función para binarizar un pixel en escala de grises
        # Si el valor del pixel es mayor que 128, lo convierte a blanco (255), de lo
        if x > 128:  
            return 255
        else:
            return 0
        
    def imagen_blanco_negro(self):
        imagen_gris = self.imagen.convert("L")
        imagen_binaria = imagen_gris.point(self.binarizar_pixel_gris)
        #se compara pixel a pixel con .point y se llama internamente el metodo binarizar_pixel_gris
        matriz_binaria = Matriz(imagen_binaria)
        print("Matriz binarizada:")
        print(matriz_binaria.devolver_matriz())
        self.comparar_imagen(matriz_binaria.devolver_matriz())
        return None
    
    def invertir(self,img_modificada = None):
        if img_modificada != None:
            if isinstance(img_modificada, Image.Image):
                matriz_img_modificada = Matriz(img_modificada)
                matriz_img_modificada.resta_numero_matriz(255)
                a = matriz_img_modificada.devolver_matriz()
                return Image.fromarray(a)
            else:
                raise TypeError("img_modificada debe ser una instancia de PIL.Image.Image")
        else:
            matriz_original = Matriz(self.imagen)
            matriz_invertida = matriz_original.resta_numero_matriz(255)
            return Image.fromarray(matriz_invertida)

    def NormalizarRGB(self):
        if self.imagen.mode != 'RGB':
            print("La imagen no está en formato RGB. No se puede normalizar.")
            return None
        
        matriz_rgb = Matriz(self.imagen).normalizar_matriz_imagen()
        print("Imagen RGB normalizada (valores entre 0 y 1).")
        print(f"Forma: {matriz_rgb.devolver_matriz()}")
        return matriz_rgb