# Proyecto GR5 - Sistema de Autenticación y Gestión de Usuarios

# Descripción

Esta  aplicación permite a los usuarios crear, administrar listas de tareas y registrar la fecha en la que se realizara la tarea. Los usuarios pueden registrarse, iniciar sesión y gestionar sus tareas de manera eficiente.

# Funcionalidades
- Registro e inicio de sesión de usuarios.
- Creación y elimiación de tareas
- Organización de tareas
- Posibilidad de asignar fecha/hora inicio y final tarea

# Instalación y Ejecución (pruebas local)
1. Clonar el repositorio
- git clone https://github.com/jaimesg00/GR5.git

2. Crear un entorno virtual e instalar dependecias:
- python -m venv myenv
- Linux: source myenv/bin/activate Windows: source myenv\Scripts\activate
- pip install -r requirements.txt

3. Ejecutar la aplicación
- flask run

4. IMPORTANTE!!!!
- Si vas a usar otra base de datos modifica el config.py con tu configuración y añade el consultas.sql a tu base de datos.
- Para ejecutarla en local o PythonAnywhere cambiar la ultima línea :(app.run(debug=True))
- Para docker si configuramos en el puerto 5000: app.run(host="0.0.0.0", port=5000, debug=True)

# Despliegue en Docker
1. Construir la imagen Docker
- docker build -t lista-tareas
2. Ejecutar el contenedor:
- docker run -p 5000:5000 lista-tareas
- La aplicación estara disponible en http://localhost:5000

# Despliegue usando Docker Hub
Si no deseas construir la imagen manualmente, puedes descargarla directamente

1. Descargar la imagen desde Docker Hub:
- jaimesag00/lista-tareas:latest

2. Ejecutar el contenedor
- docker run -d -p 5000:5000 --name lista-tareas jaimesg00/lista-tareas:latest
- La aplicación estara disponible en http://localhost:5000

# Despliegue en PythonAnywhere

1. Subir el proyecto a PythonAnywhere
2. Configurar la base de datos 
- En el apartado databases crea la base de datos
- Asigna la contraseña mysql y abre una consola para añadir las consultas y asi crear las tablas y campos.
- Apunta todo los datos de conexión y modificalos en el archivo config.py
3. Configuracion web
- Crea la web(es recomendable antes de subir el proyecto)
- Ajusta directorio de trabajo y directorio virtual (directorio virtual podemos crearlo por consola siguiendo los pasos de instalación y ejecucion #2)
- Tambien especifica el directorio estatico como imagenes, plantilas ...
- Configurar el WSGI(recuerda adaptar el path a la ruta de tu aplicación):

import sys

path = '/home/joseliza/flask-agenda-db-login/app'
if path not in sys.path:
    sys.path.insert(0, path)

from app import app as application

4. Recarga y prueba la pagina si todo esta correcto funcionara perfecto!!!!


# CREDITOS
Esto es una aplicación creada con flash para un proyecto de IAW 
