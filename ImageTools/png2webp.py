import os
import argparse
from PIL import Image

parser = argparse.ArgumentParser(description='Convierte imágenes PNG a WebP.')
parser.add_argument('input_folder', help='Carpeta donde se encuentran las imágenes PNG')
parser.add_argument('output_folder', help='Carpeta donde se guardarán las imágenes WebP')

args = parser.parse_args()

input_folder = args.input_folder
output_folder = args.output_folder

print(f"Iniciando conversión de imágenes PNG a WebP desde '{input_folder}' a '{output_folder}'...")

if not os.path.exists(input_folder):
    print(f"Error: La carpeta de entrada '{input_folder}' no existe.")
    exit(1)

os.makedirs(output_folder, exist_ok=True)
print(f"Carpeta de salida '{output_folder}' preparada.")

for filename in os.listdir(input_folder):
    
    # imagen PNG (ignorando mayúsculas/minúsculas)
    if filename.lower().endswith('.png'):
        print(f"\nProcesando: {filename}...")

        ruta_entrada = os.path.join(input_folder, filename)
        nombre_salida = os.path.splitext(filename)[0] + '.webp'
        ruta_salida = os.path.join(output_folder, nombre_salida)

        try:
            with Image.open(ruta_entrada) as img:
                img.save(ruta_salida, 'webp')
            print(f"¡Éxito! {filename} convertido a {nombre_salida}")
        except Exception as e:
            print(f"Error al procesar {filename}: {e}")
    
    else:
        print(f"{filename} no es un archivo PNG, se omite.")

print("\nConversión completada.")

