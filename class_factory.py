import numpy as np

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
            return self.lista_de_matriz
