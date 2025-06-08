from class_factory import FactoryMatriz
from calculadora import CalculadoraMatrices
from class_matriz import Matriz
def main():
    # Crear una matriz usando la Factory
    fabrica = FactoryMatriz()
    fabrica.crear_fila_matriz([1, 2])
    fabrica.crear_fila_matriz([3, 4])
    matriz1 = fabrica.retornar_matriz()

    # Crear otra matriz directamente
    fabrica2 = FactoryMatriz()
    fabrica2.crear_fila_matriz([5, 6]) 
    fabrica2.crear_fila_matriz([7, 8])
    matriz2 = Matriz(fabrica2.retornar_matriz())

    # Crear objetos de CalculadoraMatrices
    calc = CalculadoraMatrices(matriz1)

    print("Matriz 1:")
    print(calc)

    print("\nMatriz 2:")
    print(matriz2)

    print("\nSuma:")
    print(calc.suma(matriz2))

    print("\nResta:")
    print(calc.resta(matriz2))

    print("\nMultiplicación:")
    print(calc.multiplicacion(matriz2))

    print("\nTranspuesta de la matriz 1:")
    print(calc.transpuesta())

    print("\nDeterminante de la matriz 1:")
    print(calc.determinante())

if __name__ == "__main__":
    main()
