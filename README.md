# 🧰 PythonTools

**Repositorio de utilidades y scripts en Python** para automatizar tareas comunes, procesamiento de archivos e implementar pequeñas herramientas útiles del día a día.

---

## 📁 Estructura del repositorio


utilidades-python/
│
├── convertir_a_webp.py         # Convierte imágenes PNG a formato WebP
├── otras_utilidades/           # Carpeta para futuros scripts
│   └── ...
├── imagenes_png/               # Carpeta de entrada para imágenes PNG
└── imagenes_webp/              # Carpeta de salida para imágenes WebP


## 🖼️ Convertir PNG a WebP

Este script permite convertir automáticamente todas las imágenes `.png` de una carpeta a formato `.webp`.

### 🚀 Uso

1. **Coloca tus archivos `.png` en la carpeta `imagenes_png/`.**
2. **Ejecuta el script**:

   ```bash
   python3 convertir_a_webp.py
    ```
### ✅ Requisitos

- Python 3
- Pillow (instalable con pip)

```bash
sudo apt update
sudo apt install python3 python3-pip -y
pip3 install --user pillow
bash
```