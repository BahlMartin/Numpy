from class_factory import FactoryMatriz, FactoryProcesadorImagen

# Crear una matriz usando la Factory
fabrica = FactoryMatriz()
fabrica.crear_fila_matriz([1, 2])
fabrica.crear_fila_matriz([3, 4])
matriz1 = fabrica.retornar_matriz()

# Crear otra matriz directamente
fabrica2 = FactoryMatriz()
fabrica2.crear_fila_matriz([5, 6]) 
fabrica2.crear_fila_matriz([7, 8])
matriz2 = fabrica2.retornar_matriz()




# Crear objetos de CalculadoraMatrices
print("Matriz 1:")
print(matriz1)

print("\nMatriz 2:")
print(matriz2)

print("\nSuma:")
print(matriz1.suma_matrices(matriz2))

print("\nResta:")
print(matriz1.resta_matrices(matriz2))

print("\nMultiplicación:")
print(matriz1.multiplicacion(matriz2))

print("\nTranspuesta de la matriz 1:")
print(matriz1.transpuesta())

print("\nDeterminante de la matriz 1:")
print(matriz1.determinante())

# Crear un objeto ProcesadorImagen y realizar operaciones
fabricaimg = FactoryProcesadorImagen()
fabricaimg.cargar_imagen('C:/Users/bahlm/Downloads/fotocolorida.jpg')
procesador = fabricaimg.retornar_imagen()
procesador.Convertir_y_Mostrar_Imagen_gris()
procesador.imagen_blanco_negro()              
imagen_invertida = procesador.invertir()
procesador.mostrar_imagen(imagen_invertida)
procesador.Redimensionar(100, 100)
procesador.NormalizarRGB() 
