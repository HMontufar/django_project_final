# Guía para ejecutar proyecto

### 1. Abrir Git Bash para `Windows` o una terminal para `Linux/Unix`.

### 2. Realizar la clonacion del proyecto

- Clonar el proyecto
*** bash
git clone https://github.com/HMontufar/django_project_final.git

***

### 3. Crear y activar entorno virtual
(Windows)
*** bash
python -m venv venv
.\venv\Scripts\activate

***

(Linux)
***bash
python3 -m venv venv
source venv/bin/activate

***

### 4. Instalar las dependencias del proyecto
***bash
pip install -r requirements.txt

***

### 5. Navegamos hacia la carpeta del proyecto `my_blog`
```bash
cd my_blog
```

### 6. Crear la base de datos para nuestro proyecto de Django (Eliminar bd.sqlite3 en caso de que exista)
***bash
python manage.py makemigrations

***

### 7. Ejecuta la migración para crear la base de datos de nuestro proyecto
***bash
python manage.py migrate

***

### 8. Crear super usuario para nuestro proyecto y poder ralizar las pruebas tanto usuario con privilegios y usuario normal
***bash
python manage.py createsuperuser
***
Ingrese `Username`, `Email address` y `Password` 

### 9. Se levanta el servidor de Django 
`http://127.0.0.1:8000/`

***bash
python manage.py runserver

***