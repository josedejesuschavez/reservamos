# Documentación de Reservamos

1. [Modificar API Key del proyecto](#1-Modificar-API-Key-del-proyecto)
2. [Levantar el proyecto el local si se tiene docker](#2-levantar-el-proyecto-si-se-tiene-docker)
3. [Levantar el proyecto usando virtualenv](#3-Levantar-el-proyecto-usando-virtualenv)
4. [Ejecucion de pruebas unitarias](#4-Ejecucion-de-pruebas-unitarias)
5. [Endpoints disponibles](#5-Endpoints-disponibles)
   - [Obtener varios lugares con match](#Obtener-varios-lugares-con-match)
   - [Obtener el lugar con mejor match](#Obtener-el-lugar-con-mejor-match)
6. [Mejoras de performance](#6-Mejoras-de-performance)

---

## 1. Modificar API Key del proyecto
Se tiene que modificar el archivo settings.py y buscar la siguiente variable y cambiarla por tu API Key
```API_KEY_OPEN_WEATHER = 'a5a47c18197737e8eeca634cd6acb581'```

---

## 2. Levantar el proyecto si se tiene docker

#### Si se tiene docker instalado en la maquina se puede ejecutar con el siguiente comando:
`docker compose up --build`

#### Si se tiene docker instalado y la posibilidad de ejecutar makefiles
`make build`

---

## 3. Levantar el proyecto usando virtualenv

#### 1. Se tiene que crear el virtualenv con el siguiente comando
`python3 -m venv venv`

#### 2. Se habilita el virtualenv
`source venv/bin/activate`

#### 3. Se instala los paquetes necesarios
`pip install -r requirements.txt`

#### 4. Nos metemos a la carpeta reservamos y se debe de encontrar el archivo manage.py y lo ejecutamos
`python manage.py runserver`

---

## 4. Ejecucion de todas las pruebas unitarias
`pytest`


`pytest weather/tests/test_get_wather_by_name.py::test_happy_path`
`pytest weather/tests/test_get_wather_by_name.py::test_not_return_data_places_api`
`pytest weather/tests/test_get_wather_by_name.py::test_not_return_data_weather_api`


---

## 5. Endpoints disponibles

## Obtener varios lugares con match
### Descripción:
Retorna los lugares que tuvieron match

### Endpoint
`GET http://localhost:8000/api/weathers/?name=mon`

### Ejemplo de Solicitud:
```bash
curl -X GET "http://localhost:8000/api/weathers/?name=mon"
```

## Obtener el lugar con mejor match
### Descripción:
Retorna el lugar con mejor match

### Endpoint
`GET http://localhost:8000/api/weather/?name=mon`


### Ejemplo de Solicitud:
```bash
curl -X GET "http://localhost:8000/api/weather/?name=mon"
```

## 6. Mejoras de performance

#### Tiempo de ejecución sin metodos asincronos.
`13.45 segundos`

#### Tiempo de ejecución con metodos asincronos.
`2.14 segundos`