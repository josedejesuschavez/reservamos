# Documentación de Reservamos

1. [Levantar el proyecto el local si se tiene docker](#levantar-el-proyecto-si-se-tiene-docker)
2. [Levantar el proyecto usando virtualenv](#Levantar-el-proyecto-usando-virtualenv)
3. [Ejecucion_de_pruebas_unitarias](#Ejecucion-de-pruebas-unitarias)
4. [Mejoras_de_performance](#Mejoras-de-performance)

## Levantar el proyecto si se tiene docker

#### Si se tiene docker instalado en la maquina se puede ejecutar con el siguiente comando:
`docker compose up --build`

#### Si se tiene docker instalado y la posibilidad de ejecutar makefiles
`make build`


## Levantar el proyecto usando virtualenv

#### 1. Se tiene que crear el virtualenv con el siguiente comando
`python3 -m venv venv`

#### 2. Se habilita el virtualenv
`source venv/bin/activate`

#### 3. Se instala los paquetes necesarios
`pip install -r requirements.txt`

#### 4. Nos metemos a la carpeta reservamos y se debe de encontrar el archivo manage.py y lo ejecutamos
`python manage.py runserver`

## Ejecucion de todas las pruebas unitarias
`pytest`

## Mejoras de performance

#### Tiempo de ejecución sin metodos asincronos.
`13.45 segundos`

#### Tiempo de ejecución con metodos asincronos.
`2.14 segundos`