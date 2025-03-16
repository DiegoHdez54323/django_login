Django Login con CRUD de Usuarios

Este repositorio contiene un sistema de autenticación (Login) y un CRUD de usuarios desarrollado en Django, utilizando TailwindCSS y Flowbite para los estilos, y PostgreSQL como base de datos.

🚀 Tecnologías Utilizadas

Django (Backend)

TailwindCSS & Flowbite (Frontend)

PostgreSQL (Base de datos)

npm (Para gestionar los estilos con TailwindCSS)

📌 Instalación y Configuración

Sigue estos pasos para ejecutar el proyecto en tu entorno local:

1️⃣ Crear y activar el entorno virtual

python -m venv venv

Activar el entorno virtual:

Windows:

venv\Scripts\activate

Mac/Linux:

source venv/bin/activate

2️⃣ Instalar las dependencias del proyecto

pip install -r requirements.txt

3️⃣ Instalar los paquetes de npm para TailwindCSS y Flowbite

npm install

4️⃣ Compilar los estilos de TailwindCSS

npm run buildcss

5️⃣ Configurar la base de datos PostgreSQL

Asegúrate de tener PostgreSQL instalado y configurado. Luego, en el archivo settings.py, edita la configuración de la base de datos:

DATABASES = {
'default': {
'ENGINE': 'django.db.backends.postgresql',
'NAME': 'nombre_de_tu_base',
'USER': 'tu_usuario',
'PASSWORD': 'tu_contraseña',
'HOST': 'localhost',
'PORT': '5432',
}
}

6️⃣ Ejecutar migraciones de Django

python manage.py makemigrations
python manage.py migrate

7️⃣ Levantar el servidor de desarrollo

python manage.py runserver

El servidor estará disponible en: http://127.0.0.1:8000/

🛠 Funcionalidades

✅ Registro y autenticación de usuarios
✅ CRUD (Crear, Leer, Actualizar, Eliminar) de usuarios
✅ Interfaz moderna con TailwindCSS y Flowbite
✅ Base de datos PostgreSQL para almacenar usuarios
