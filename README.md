# Interpolación de Newton

Este programa realiza la interpolación de puntos utilizando el método de Newton. Permite ingresar una lista de valores de tiempo de captura y uso de CPU, y luego realiza la interpolación para obtener valores interpolados en puntos específicos.

## Descripción

La interpolación de Newton es un método utilizado para estimar valores desconocidos entre un conjunto de puntos conocidos. En este programa, se implementa el método de Newton para interpolar valores de uso de CPU en puntos de tiempo específicos, utilizando los datos de tiempo de captura y uso de CPU proporcionados.

## Documentación


- [Metodo_de_Interpolación_de_Newton.ipynb](Metodo_de_Interpolación_de_Newton.ipynb): Archivo principal que contiene el código del programa en formato Jupyter Notebook.

## Ejecutando en Google Colab

Si deseas ejecutar este programa en Google Colab, sigue los pasos a continuación:

1. Haz clic en el siguiente enlace para abrir el archivo `interpolacion_newton.ipynb` en Google Colab: [Abrir en Google Colab]https://colab.research.google.com/github/Augustelli/Interpolacion_de_Newton/blob/master/Metodo_de_Interpolaci%C3%B3n_de_Newton.ipynb).

2. Una vez abierto en Google Colab, puedes ejecutar el código siguiendo las celdas y las instrucciones proporcionadas en el notebook.

> Nota: Ten en cuenta que es posible que debas ajustar algunas partes del código para que funcione correctamente en el entorno de Google Colab, como la instalación de paquetes adicionales o la carga de archivos de datos.

¡Disfruta ejecutando el programa en Google Colab!


## Requisitos

- Python 3.7 o superior
- pip (administrador de paquetes de Python)

## Instalación

Siga los pasos a continuación para instalar y configurar el programa en su entorno local.

1. Clonar el repositorio:

   ```shell
   git clone https://github.com/Augustelli/Interpolacion_de_Newton.git
   ```

2. Activación de entorno virtual e instalación de dependencias:

   - Si estás utilizando Windows:
     - En CMD, ejecuta en la terminal: `install_windows_cmd.bat`
     - En PowerShell, ejecuta en la terminal: `.\install_windows_powershell.ps1`
   - Si estás utilizando Linux o MacOS, ejecuta en la terminal: `sh install.sh`

El script de instalación creará un entorno virtual llamado "interpolacion_newton", instalará las dependencias necesarias del archivo "requirements.txt" y configurará el entorno para ejecutar el programa.

> Nota: Asegúrate de tener permisos de administrador o superusuario para ejecutar el script de instalación.

## Uso

Para ejecutar el programa, sigue los siguientes pasos:

1. Activa el entorno virtual:

   ```shell
   source interpolacion_newton/bin/activate
   ```

2. Ejecuta el programa:

   ```shell
   python interpolacion_newton.py
   ```

3. Sigue las instrucciones en pantalla para ingresar los valores de tiempo de captura y uso de CPU, y obtener valores interpolados en puntos específicos.

> Nota: Asegúrate de tener los datos de tiempo de captura y uso de CPU preparados antes de ejecutar el programa.

## Contribuciones

¡Tu contribución al proyecto es bienvenida! Si deseas contribuir al proyecto, puedes seguir los siguientes pasos:

1. Realiza un fork del repositorio.
2. Crea una rama nueva para tu contribución.
3. Realiza los cambios o mejoras en tu rama.
4. Envía una solicitud de extracción para que revisemos tus cambios.

También puedes informar problemas o solicitar nuevas características utilizando el sistema de [Issues](https://github.com/Augustelli/Interpolacion_de_Newton/issues) en GitHub.

## Licencia

El proyecto se distribuye bajo la Licencia Pública General de GNU (GPL) versión X. Puedes ver el texto completo de la licencia en el archivo [LICENSE.md](LICENSE.md).

## Información adicional

- Autor: Augusto Tomás Mancuso
- Email: augusto.tomas.mancuso@gmail.com

Este proyecto es de código abierto y puedes usarlo, modificarlo y distribuirlo de acuerdo con los términos de la licencia GPL. Esperamos que este proyecto sea útil para la comunidad y animamos a otros desarrolladores a contribuir y mejorar el código.

¡Gracias por tu interés en mi proyecto de código abierto!
