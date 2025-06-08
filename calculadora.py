import numpy as np
from class_matriz import Matriz
class CalculadoraMatrices(Matriz):
    def __init__(self, matriz):
        super().__init__(matriz)

    def suma(self, otra_matriz):
        return self.matriz + otra_matriz.devolver_matriz()

    def resta(self, otra_matriz):
        return self.matriz - otra_matriz.devolver_matriz()
    
    def multiplicacion(self, otra_matriz):
        if self.matriz.shape[1] == otra_matriz.devolver_matriz().shape[0]:
            return self.matriz @ otra_matriz.devolver_matriz()
        else:   
            return "Las matrices no se pueden multiplicar: número de columnas de la primera matriz debe ser igual al número de filas de la segunda."
        
   
        
