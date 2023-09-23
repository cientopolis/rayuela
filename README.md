# Plataforma Rayuela
Esta plataforma propone un abordaje para incorporar ludificación adaptativa a proyectos de ciencia ciudadana

## Pre-requisitos 📋

* Python 3.8
* Se recomienda utilizar un [entorno virtual](https://docs.python.org/es/3.8/library/venv.html) pasándole como parámetro la versión de python
* Solo para producción: _mysql_ instalado en el sistema (servidor y cliente)

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

### Para desarrollo
En el archivo _settings.py_ está configurada la base de datos para usarse con sqlite.
Al hacer las migraciones, aparecerá en la raíz un archivo llamado _rayuela.sqlite3_.

NOTA: ante problemas o necesidad de comenzar de nuevo, simplemente borrar el archivo y ejecutar migraciones nuevamente.

### Para producción
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

En el archivo settings.py cambiar la base de datos default:
```
"default": {
    "ENGINE": "django.db.backends.mysql",
    "NAME": config('MYSQL_DB'),
    'USER' : config('MYSQL_USER'),
    'PASSWORD': config('MYSQL_PASSWORD'),
    'HOST': config('MYSQL_HOST'),
    'PORT':config('MYSQL_PORT')
}
```

## Creación de tablas y datos

- Se debe copiar el archivo **_env.example_** en la misma raíz del proyecto donde está ubicado y llamarlo **_.env_**, modificando las variables necesarias para configurar el entorno, como las relacionadas con la base de datos, el dominio, las leyendas en algunos botones, etc.

A continuación ejecutar los siguientes comandos para realizar las migraciones de las tablas a la base de datos: 

```
python manage.py makemigrations
python manage.py migrate
```

Finalmente, ejecutar los siguientes comandos para cargar información de configuración en la base de datos (roles, usuarios/as, días, proyectos, criterios de valoración): 

```
python manage.py create_roles_and_users && python manage.py create_criteria_and_days && python manage.py create_projects
```
NOTA: los archivos de creación se encuentran dentro de ```rayuelaApp/management/commands```

Para ingresar al sistema se generan los siguientes usuarios:
- root
- admin1
- admin2
- admin3
- pv1
- pv2
- pv3
- pv4

En todos los casos la contraseña es `ContraseñaInsegura`.

NOTA: **NO** debe usarse esta información para producción, solo para trabajar en desarrollo

## Despliegue de la aplicación 📦
```
python manage.py runserver
```

## Ejecución de los tests 🔧
```
python manage.py test
```
## Documentación de API con Swagger y ReDoc

En las siguientes rutas se encuentra documentada la API:
- `swagger/`
- `redoc/`

## Créditos ✒️

- **Sergio** - [tarbz2](https://github.com/tarbz2)
- **Micael Jotar** - [jotarMicael](https://github.com/jotarMicael)
- **Valentin Gallardo Ucero**
