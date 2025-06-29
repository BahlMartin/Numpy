# 🖼️ Procesador de Imágenes y Calculadora de Matrices con Python

Este proyecto implementa una herramienta de procesamiento básico de **matrices** y **manipulación de imágenes** usando Python. Incluye:

- Operaciones con matrices: suma, resta, multiplicación, determinante, transpuesta, promedio, etc.
- Procesamiento de imágenes: conversión a escala de grises, binarización, inversión, redimensionado y normalización RGB.
- Uso de patrones de diseño `Factory` para crear matrices e imágenes de manera flexible.

---

## 📁 Estructura del Proyecto

```
.
├── main.py
├── class_matriz.py
├── class_ProcesadorImagen.py
├── class_factory.py
├── README.md
```

---

## 📦 Requisitos

Este proyecto utiliza las siguientes bibliotecas:

- `numpy`
- `Pillow`
- `matplotlib`

Instalación con pip:

```bash
pip install numpy pillow matplotlib
```

---

## ▶️ Ejecución

El archivo principal es `main.py`, donde se crean objetos para:

- Operaciones con matrices.
- Carga y procesamiento de una imagen desde una ruta local.

```bash
python main.py
```

> ⚠️ Asegúrate de modificar la ruta de imagen en el código:
>
> ```python
> fabricaimg.cargar_imagen('C:/Users/usuario/Downloads/mi_imagen.jpg')
> ```

---

## 📚 Tabla de Métodos

### 🔢 `Matriz`

| Método                        | Descripción                                                         |
| ----------------------------- | ------------------------------------------------------------------- |
| `transpuesta()`               | Devuelve la matriz transpuesta.                                     |
| `determinante()`              | Calcula el determinante (solo si es una matriz cuadrada).           |
| `__str__()`                   | Representación en cadena de la matriz.                              |
| `devolver_matriz()`           | Devuelve la matriz interna como array de NumPy.                     |
| `suma_matrices(otra_matriz)`  | Suma con otra instancia de `Matriz`.                                |
| `resta_matrices(otra_matriz)` | Resta otra instancia de `Matriz`.                                   |
| `multiplicacion(otra_matriz)` | Multiplica la matriz con otra si las dimensiones son compatibles.   |
| `multiplicacion_escalar(x)`   | Multiplica todos los elementos por un escalar.                      |
| `promedio()`                  | Devuelve el promedio de los valores de la matriz.                   |
| `resta_numero_matriz(n)`      | Resta cada valor de la matriz a un número (para invertir imágenes). |
| `normalizar_matriz_imagen()`  | Normaliza los valores de la matriz en el rango [0,1].               |

---

### 🖼️ `ProcesadorImagen`

| Método                              | Descripción                                                            |
| ----------------------------------- | ---------------------------------------------------------------------- |
| `Convertir_y_Mostrar_Imagen_gris()` | Convierte la imagen a escala de grises, calcula el promedio e imprime. |
| `mostrar_imagen(imagen=None)`       | Muestra una imagen específica o la imagen original.                    |
| `comparar_imagen(imagen)`           | Muestra lado a lado la imagen original y una modificada.               |
| `Redimensionar(ancho, alto)`        | Redimensiona la imagen a las dimensiones dadas.                        |
| `binarizar_pixel_gris(x)`           | Convierte un pixel a blanco o negro según un umbral (128).             |
| `imagen_blanco_negro()`             | Convierte imagen a binaria a partir de escala de grises.               |
| `invertir(imagen=None)`             | Invierte los colores de la imagen (255 - pixel).                       |
| `NormalizarRGB()`                   | Normaliza los valores RGB entre 0 y 1 si la imagen es RGB.             |

---

### 🏠 `FactoryMatriz`

| Método                             | Descripción                                                    |
| ---------------------------------- | -------------------------------------------------------------- |
| `crear_fila_matriz(lista_numeros)` | Añade una fila a la matriz si todos los elementos son números. |
| `retornar_matriz()`                | Devuelve una instancia de `Matriz` con las filas agregadas.    |

---

### 🏠 `FactoryProcesadorImagen`

| Método                | Descripción                                   |
| --------------------- | --------------------------------------------- |
| `cargar_imagen(ruta)` | Carga una imagen desde la ruta proporcionada. |
| `retornar_imagen()`   | Devuelve una instancia de `ProcesadorImagen`. |

---

## 📊 Resultados Esperados

Al ejecutar el proyecto:

- Se imprimen resultados de operaciones matriciales en consola.
- Se visualizan imágenes procesadas (binarizadas, invertidas, redimensionadas).

---

## 🛠️ Futuras Mejoras

- Agregar interfaz gráfica.
- Exportación de resultados (matrices e imágenes).
- Integración de pruebas unitarias.

---

## 🧑‍💻 Autor

Desarrollado por Martin ,Bahl, Julian ,Perez y Marcelo.