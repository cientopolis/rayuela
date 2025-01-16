# Imagen oficial de python
FROM python:3.8

# Crear directorio para el proyecto
RUN mkdir /app

# Ingresar a la carpeta del proyecto
WORKDIR /app

# Copiar el proyecto a la carpeta interna
COPY . /app

# Configurar variables de entorno
ENV PIP_DISABLE_PIP_VERSION_CHECK=1
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1 

# Actualizar pip
RUN pip install --upgrade pip 

# Instalar dependencias python para el proyecto
RUN pip install --no-cache-dir -r requirements.txt

# Exponer el puerto
EXPOSE 8000

# Ejecutar migraciones
RUN python manage.py makemigrations
RUN python manage.py migrate

# Ejecutar scripts para generar datos
RUN python manage.py create_roles_and_users
RUN python manage.py create_criteria_and_days
RUN python manage.py create_projects

# Ejecutar el entorno de desarrollo Django
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
