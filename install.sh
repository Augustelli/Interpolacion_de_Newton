#!/bin/bash

python3 -m venv interpolacion_newton
source interpolacion_newton/bin/activate

# Actualizar pip
pip install --upgrade pip

# Instalar las dependencias
pip install -r requirements.txt

echo "El entorno virtual y las dependencias han sido instaladas correctamente."
echo "Puedes activar el entorno virtual con 'source interpolacion_newton/bin/activate'."

# Dar permisos de ejecución al script
chmod +x interpolacion_newton.py