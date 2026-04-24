from PIL import Image
import numpy as np
from tkinter import Tk, filedialog

# Ocultar ventana principal
Tk().withdraw()

# Abrir explorador para seleccionar imagen
ruta = filedialog.askopenfilename(
    title="Selecciona una imagen",
    filetypes=[("Imágenes", "*.jpg *.jpeg *.png")]
)

# Cargar imagen
imagen = Image.open(ruta).convert("L")
matriz = np.array(imagen)

# Filtro de bordes
filtro = np.array([
    [-1, -1, -1],
    [-1,  8, -1],
    [-1, -1, -1]
])

resultado = np.zeros_like(matriz)

for i in range(1, matriz.shape[0]-1):
    for j in range(1, matriz.shape[1]-1):
        region = matriz[i-1:i+2, j-1:j+2]
        resultado[i, j] = np.sum(region * filtro)

# Guardar resultado
imagen_resultado = Image.fromarray(resultado)
imagen_resultado.save("resultado.jpg")

print("Imagen procesada correctamente")