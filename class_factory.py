from PIL import Image
from class_matriz import Matriz
from class_ProcesadorImagen import ProcesadorImagen

class FactoryMatriz:
    def __init__(self):
        self.lista_de_matriz = []
    
    def crear_fila_matriz(self, lista_de_numeros):
        if not isinstance(lista_de_numeros, list):
            return "La entrada debe ser una lista."
        if not all(isinstance(numeros, (int, float)) for numeros in lista_de_numeros): 
            return "La lista debe contener solo números."
        self.lista_de_matriz.append(lista_de_numeros)

    def retornar_matriz(self):
        if self.lista_de_matriz == []:
            return "La matriz está vacía."
        else:
            return Matriz(self.lista_de_matriz)
        
    

class FactoryProcesadorImagen:
    def __init__(self):
        self.imagen = None
    def cargar_imagen(self,ruta_imagen): 
        try:
            # exepcion para informar que la imagen no esta en la ruta dada    
            self.imagen = Image.open(ruta_imagen)  #variable  que habre la imagen usando pillow
        except FileNotFoundError:
            return "la imagen en '{ruta_imagen}' no se encontro"
        
    def retornar_imagen(self):
        if self.imagen is None:
            return "No hay imagen cargada."
        else:
            return ProcesadorImagen(self.imagen)
        

        