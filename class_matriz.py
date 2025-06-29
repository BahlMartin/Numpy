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
    
    def suma_matrices(self, otra_matriz):
        return self.matriz + otra_matriz.devolver_matriz()

    def resta_matrices(self, otra_matriz):
        return self.matriz - otra_matriz.devolver_matriz()
    
    def multiplicacion(self, otra_matriz):
        if self.matriz.shape[1] == otra_matriz.devolver_matriz().shape[0]:
            return self.matriz @ otra_matriz.devolver_matriz()
        else:   
            return "Las matrices no se pueden multiplicar: número de columnas de la primera matriz debe ser igual al número de filas de la segunda."
    
    def multiplicacion_escalar(self, escalar):
        if  not isinstance(escalar, (int, float)):
            return "El escalar debe ser un número."
        else:
            return self.matriz * escalar
        
    def promedio(self):
        return np.mean(self.matriz)
    
    def resta_numero_matriz(self, numero):
        if isinstance(numero, int):
            self.matriz = numero - self.matriz 
            return  self.matriz
        else:
            return "El número debe ser un entero o un flotante."
        
    def normalizar_matriz_imagen(self):
        if self.matriz.size == 0:
            return "La matriz está vacía."
        else:
           matriz_01 = self.matriz.astype(np.float32) / 255.0
           return Matriz(matriz_01)