import numpy as np
class Matriz():
    def __init__(self,lista_bidimensional):
        self.matriz = np.array(lista_bidimensional)

    def transpuesta(self):
        return self.matriz.T

    def determinante(self):
        if self.matriz.shape[0] == self.matriz.shape[1]:
            return np.linalg.det(self.matriz)
        else:
            return "La matriz debe ser cuadrada para calcular el determinante."
        
    def __str__(self):
        return str(self.matriz)
    
    def devolver_matriz(self):
        return self.matriz