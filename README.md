# Plataforma Rayuela
Esta plataforma propone un abordaje para incorporar ludificación adaptativa a proyectos de ciencia ciudadana

## Pre-requisitos 📋

* Python 3.8
* Se recomienda utilizar un [entorno virtual](https://docs.python.org/es/3.8/library/venv.html) pasándole como parámetro la versión de python
* mysql instalado en el sistema (servidor y cliente)

## Instalación de dependencias 🔧
Revisar que las versiones de python y pip son las correctas (python3.8):
```
   python --version
   pip --version
```
Para la instalación de todas las dependencias necesarias se debe ejecutar el siguiente comando:
```
   pip install -r requirements.txt
```

Dependiendo del sistema, y en particular de la versión de Python que se esté usando, puede ocurrir que se necesiten algunas dependencias mas, entonces se debe editar el archivo manualmente y ejecutar nuevamente el comando anterior.

## Creación y configuración de la base de datos

Ingresar al cliente mysql con root:
```
sudo mysql -u root
```
Crear base de datos, crear usuario adminRayuela y configurar permisos:
```
CREATE DATABASE rayuela;
CREATE USER 'adminRayuela'@'localhost' IDENTIFIED BY 'changethisone';
GRANT ALL ON rayuela.* TO 'adminRayuela'@'localhost';
GRANT ALL ON test_rayuela.* TO 'adminRayuela'@'localhost';
FLUSH PRIVILEGES;
```

- Se debe copiar el archivo **_env.example_** en la misma raíz del proyecto donde está ubicado y llamarlo **_.env_**, modificando las variables necesarias para configurar el entorno, como las relacionadas con la base de datos, el dominio, las leyendas en algunos botones, etc.

A continuación ejecutar los siguientes comandos para realizar las migraciones de las tablas a la base de datos: 

```
python manage.py makemigrations
python manage.py migrate
```

Finalmente, ejecutar el siguiente comando para cargar información de configuración (Usuarios, días, criterios de valoración) en la base de datos: 

```
python manage.py loaddata data.json
```
Para ingresar al sistema se generan los siguientes 3 usuarios:
- root
- admin
- player

En los 3 casos la contraseña es `ContraseñaInsegura`.

NOTA: **NO** debe usarse esta información para producción, sólo para trabajar en desarrollo

## Despliegue de la aplicación 📦
```
python manage.py runserver
```

## Ejecución de los tests 🔧
```
python manage.py test
```

## Créditos ✒️

* **Sergio** - [tarbz2](https://github.com/tarbz2).
* **Micael Jotar** - *Trabajo Completo* - [jotarMicael](https://github.com/jotarMicael).
* **Valentin Gallardo Ucero** - *Trabajo Completo*.
