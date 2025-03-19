# Control de LED con FastAPI

Este proyecto utiliza **FastAPI** para crear una API simple que permite controlar un LED mediante un endpoint.

## Descripción

La API tiene dos endpoints principales:

1. **`/`**: Muestra un mensaje de inicio que confirma que FastAPI está funcionando correctamente.
2. **`/led`**: Este endpoint simula el control de un LED, siempre respondiendo con el estado 'ON'.

## Requisitos

- Python 3.7 o superior
- FastAPI
- Uvicorn (para ejecutar el servidor)

## Instalación

1. Clona este repositorio:

    ```bash
    git clone https://github.com/tu-usuario/tu-repositorio.git
    ```

2. Crea un entorno virtual (opcional pero recomendado):

    ```bash
    python -m venv venv
    ```

3. Activa el entorno virtual:

    - En Windows:

    ```bash
    venv\Scripts\activate
    ```

    - En macOS/Linux:

    ```bash
    source venv/bin/activate
    ```

4. Instala las dependencias necesarias:

    ```bash
    pip install -r requirements.txt
    ```

   Si no tienes un archivo `requirements.txt`, puedes instalar las dependencias manualmente:

    ```bash
    pip install fastapi uvicorn
    ```

## Uso

1. Ejecuta el servidor de desarrollo con Uvicorn:

    ```bash
    uvicorn main:app --reload
    ```

    Donde `main` es el nombre del archivo Python que contiene el código (sin la extensión `.py`).

2. Accede a la API en tu navegador o usando herramientas como **Postman** o **curl**:

    - **`/`**: Navega a `http://127.0.0.1:8000/` para verificar que FastAPI está funcionando.
    - **`/led`**: Navega a `http://127.0.0.1:8000/led` para simular el control del LED.

## Documentación

FastAPI genera automáticamente una documentación interactiva para los endpoints de la API. Puedes acceder a ella en:

- [Documentación de la API (Swagger UI)](http://127.0.0.1:8000/docs)
- [Redoc](http://127.0.0.1:8000/redoc)
