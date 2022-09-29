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

# Desafio Teorico

1. Procesos o Hilos
    - Cuando usar Procesos
        -R= Cuando se necesita utilizar al maximo los procesadores en una maquina determinada para ejecutar una tarea, ejm: para procesar un gran numero de datos sin esperar por I/O se puede derivar en varios procesos si tenemos N cores disponibles.

    - Cuando usar Hilos o Threads
        -R= Cuando se necesitan ejecutar tareas no tan pesadas  y si se hace mucho de data compartida entre hilos entonces conveniente usar Threads [Un proceso puede tener varios hilos], llamar a funciones dentro de un bucle para que sea ejecutadas.
    
    - Cuando usar corrutinas
        -R= Cuando necesite llamar desde una funcion a otra funcion y esperar el resultado de la misma para continuar con la funcion principal parecido al (Async await en JS) / no es paralelismo pero su control es mas optimo.

    
