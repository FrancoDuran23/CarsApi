# CarsApi
Este repositorio contiene una API de backend desarrollada en Django Rest Framework para administrar información relacionada con automóviles. La API permite realizar operaciones CRUD (Crear, Leer, Actualizar y Eliminar) sobre recursos de automóviles, como marcas, modelos y tipos de vehículos.

## Requisitos previos

Asegúrate de tener los siguientes requisitos previos instalados en tu sistema:

- Python 3.x: https://www.python.org/downloads/
- Pip: https://pip.pypa.io/en/stable/installing/
- Virtualenv (opcional pero recomendado): https://virtualenv.pypa.io/en/latest/installation.html

## Configuración del entorno

1. Clona este repositorio en tu máquina local.

2. Abre una terminal y navega hasta la carpeta raíz del proyecto.

3. Crea un entorno virtual (opcional pero recomendado) ejecutando el siguiente comando:
  ```
  virtualenv venv
  ```
4. Activa el entorno virtual ejecutando el siguiente comando:
- En Windows:
  ```
  venv\Scripts\activate
  ```
- En macOS y Linux:
  ```
  source venv/bin/activate
  ```

5. Instala las dependencias del proyecto ejecutando el siguiente comando:
  ```
  pip install -r requirements.txt
  ```
6. Configura las variables de entorno en un archivo `.env` en la raíz del proyecto. Puedes copiar el archivo `.env.example` y proporcionar los valores necesarios.

7. Realiza las migraciones de la base de datos ejecutando el siguiente comando:
  ```
  python manage.py migrate
  ```

## Ejecución del proyecto

Una vez que hayas configurado el entorno, puedes ejecutar el proyecto localmente:

1. Inicia el servidor de desarrollo ejecutando el siguiente comando:
  ```
  python manage.py runserver
  ```
2. Accede a la API en tu navegador web en la siguiente dirección:
  ```
  http://localhost:8000/
  ```
Ahora deberías tener el proyecto de Django Rest Framework en funcionamiento en tu entorno local.

## Rutas de la API

La API proporciona las siguientes rutas y endpoints para interactuar con los recursos:

### Autos

- `GET /api/cars/`: Obtiene la lista de todos los autos.
- `GET /api/cars/<id>/`: Obtiene los detalles de un auto específico.
- `POST /api/cars/`: Crea un nuevo auto.
- `PUT /api/cars/<id>/`: Actualiza los detalles de un auto específico.
- `DELETE /api/cars/<id>/`: Elimina un auto específico.

### Endpoint: Filtrado y Ordenamiento de Automóviles

Este endpoint permite filtrar y ordenar automóviles en base a diferentes criterios. A continuación se muestra una explicación detallada de su funcionamiento:

### URL

- `GET /api/filter_and_sort/<filter_by>/<order_by>/`: Filtra y Ordena la Lista de todos los Autos

### Parámetros de consulta

### filter_by: (obligatorio) Indica el tipo de filtro a aplicar. Los valores posibles son:

  0: Sin filtro
  1: Filtrar por autos
  2: Filtrar por pickups y comerciales
  3: Filtrar por SUVs y crossovers

### order_by: (obligatorio) Indica el tipo de ordenamiento a aplicar. Los valores posibles son:

  1: Ordenar por precio de menor a mayor
  2: Ordenar por precio de mayor a menor
  3: Ordenar por nuevos primeros 
  4: Ordenar por viejos primeros 


