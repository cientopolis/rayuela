# Plataforma Rayuela
Esta plataforma propone un abordaje para incorporar ludificación adaptativa a proyectos de ciencia ciudadana

## Pre-requisitos 📋

* Python 3.8 (Se recomienda utilizar un entorno virtual)
* Base de datos mysql (servidor y cliente)
* Configurar el archivo .env con las variables para configurar:
   * Acceso a la base de datos
   * ??

## Instalación de dependencias 🔧

Para la instalación de todas las dependencias necesarias se debe ejecutar el siguiente comando:
```
   pip install -r requirements.txt
```
Dependiendo del sistema, y en particular de la versión de Python que se esté usando, puede ocurrir que se necesiten algunas dependencias mas, entonces se debe editar el archivo manualmente y ejecutar nuevamente el comando anterior.

## Setup de la base de datos

En primer lugar, se debe crear la base de datos y un primer super usuario *adminRayuela*:
 
```
sudo mysql -u root

CREATE DATABASE rayuela;
CREATE USER 'adminRayuela'@'localhost' IDENTIFIED BY 'changethisone';
GRANT ALL ON rayuela.* TO 'adminRayuela'@'localhost';
GRANT ALL ON test_rayuela.* TO 'adminRayuela'@'localhost';
FLUSH PRIVILEGES;
```

A continuación ejecutar los siguientes comandos para realizar las migraciones de las tablas a la base de datos: 

```
python3 manage.py makemigrations
python3 manage.py migrate
```

Finalmente, ejecutar el siguiente comando para cargar información de configuración (Usuarios, días, criterios de valoración) en la base de datos: 

```
python3 manage.py loaddata data.json
```
> Qué datos carga en la base de datos????? Describir

## Despliegue de la aplicación 📦
```
python3 manage.py runserver
```

## Ejecución de los tests 🔧
```
python3 manage.py test
```

## Configuraciones

El fichero .env permite hacer un conjunto de configuraciones relacionadas con la base de datos a utilizar, el dominio, las leyendas en algunos botones, etc:

```
#DB
MYSQL_HOST='valor'
MYSQL_USER='valor'
MYSQL_PASSWORD='valor'
MYSQL_DB='valor'
MYSQL_PORT=''

#SERVICE_EMAIL
EMAIL_BACKEND='valor'
EMAIL_HOST='valor'
EMAIL_USE_TLS='valor'
EMAIL_PORT='valor'
EMAIL_HOST_USER='valor'
EMAIL_HOST_PASSWORD='valor'
  
#DOMAINS
DEFAULT_DOMAIN = 'http://localhost:8000'

#NAVBAR_COLOR
NAVBAR_COLOR = 'bg-info'

#ROOT_NAVBAR
ROOT_CREATE_ADMIN='Alta de admin'
ROOT_CREATE_PROJECT='Crear proyecto'
#

#ROOT_HEADER
ROOT_HEADER='Como Root tiene acceso a crear projectos y asignarselos a los usuarios administradores, desde las opciones en el menú de su izquierda'
#

#PROJECT_TITLE
PROJECT_TITLE='ALA'
#

#ADMIN_NAVBAR
ADMIN_CREATE_BADGE='Crear Insignia'
ADMIN_CREATE_CHALLENGE='Crear Desafío'
#

#PLAYER_NAVBAR
PLAYER_CREATE_CHECKIN='Realizar checkin'
PLAYER_SEE_MY_GE='Ver mis EJ'
PLAYER_SEE_ALL_PROJECTS='Todos los proyectos'
PLAYER_MY_PROJECTS='Mis proyectos'
#

#TIME_RESTRICTION
CREATE_TIME_RESTRICTION='Crear RT'
#

#BUTTON
REGISTER_BUTTON='Unirme'
MODIFY_BUTTON='Modificar'
DISJOIN_BUTTON='Dar Baja'
#
```


## Créditos ✒️

* **Sergio** [github](https://github.com/jotarMicael).
* **Micael Jotar** - *Trabajo Completo* - [jotarMicael](https://github.com/jotarMicael).
* **Valentin Gallardo Ucero** - *Trabajo Completo*.

  
