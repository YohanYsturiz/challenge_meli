## MERCADO LIBRE CHALLENGE | BACKEND

Microservicio para lectura de un archivo cargado con items y luego consultar su informacion el api de mercado libre.

## Tecnologias aplicadas
- Python 3.9.6
- Flask 2.2.2
- docker-compose
- PostgreSQL

## Environment Variables
```sh
# variable de entorno para la conexion a la base de datos
CHALLANGE_DB=postgresql://postgres:postgres@localhost:5436/challengedb
```

## Desplegar proyecto en tu servidor local
Se recomienda instalar pyenv virtualenv crear tu entorno e instalar Docker antes de ejecutar los siguientes pasos:
- https://github.com/pyenv/pyenv-virtualenv
- https://docs.docker.com/compose/install/

**Levantar tu base de datos con docker-compose:**

```sh
docker-compose up -d
```

**Instalar las dependencias o paquetes que necesita el proyecto:**

```sh
pip install -r requirements.txt 
```
**Ejecutar las migraciones para crear las tablas de la BD:**

```sh
sh migrate.sh
```
**levantar el proyecto con el siguiente comando:**

```sh
sh run.sh
```

## Endpoints
**Status del servicio**
```sh
[GET] {host}/api/health
```
**Subir archivo csv/txt**
```sh
[POST] {host}/api/upload

# - form-data inputs
    the_file: archivo a procesar
    params: "{\"separator\":\",\",\"format\":\"csv\",\"encoding\":\"utf-8\"}"
```