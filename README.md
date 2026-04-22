# Proyecto: Sistema de Registro de Puntos de Interés

## Descripción

Aplicación web desarrollada con contenedores Docker que permite consultar puntos de interés geográficos.

El sistema utiliza:

- PostgreSQL + PostGIS
- Python Flask
- Nginx
- Docker Compose

## Arquitectura

Usuario -> Nginx -> Flask -> PostgreSQL

## Funcionalidades

- Página principal web
- Listado de lugares
- Filtro por categoría cultural
- Filtro por categoría natural
- Base de datos con carga inicial

## Contenedores

1. postgres_db
2. flask_app
3. nginx_proxy

## Ejecución

docker compose up --build

docker compose up -d

docker compose down

## URLs del sistema

- http://localhost
- http://localhost/lugares
- http://localhost/categoria/cultural
- http://localhost/categoria/natural

## Persistencia

postgres_data

## Autor

Nathaly Gabriela Alay Perez
