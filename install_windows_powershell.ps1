# Crear el entorno virtual
python -m venv interpolacion_newton
.\interpolacion_newton\Scripts\Activate.ps1

# Actualizar pip
python -m pip install --upgrade pip

# Instalar las dependencias
pip install -r requirements.txt

Write-Host "El entorno virtual y las dependencias han sido instaladas correctamente."
Write-Host "Puedes activar el entorno virtual ejecutando '.\interpolacion_newton\Scripts\Activate.ps1'."
