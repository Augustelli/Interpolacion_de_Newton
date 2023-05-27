@echo off

REM Crear entorno virtual
python -m venv interpolacion_newton

REM Activar el entorno virtual
call interpolacion_newton\Scripts\activate.bat

REM Instalar las dependencias desde requirements.txt
pip install -r requirements.txt

REM Otros comandos necesarios para la configuración adicional
REM ...

REM Desactivar el entorno virtual
deactivate

echo Instalación completada.
