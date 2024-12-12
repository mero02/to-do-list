# To-Do List App

Una aplicación sencilla para gestionar tareas utilizando Flask.

## Tecnologías

- Python
- Flask
- SQLite
- Bootstrap

## Instalación

1. Clona este repositorio:
   ```bash
   git clone https://github.com/mero02/to-do-list.git
   cd to-do-list
   ```
2. Crea un entorno virtual y actívalo:
    ```bash
        python -m venv venv
    ```
    Activar en Windows:
    ```bash
        venv\Scripts\activate
    ```
    Activar en Linux/Mac:
    ```bash
        source venv/bin/activate
    ```
3. Instala las dependencias:
    ```bash
        pip install -r requirements.txt
    ```
4. Crea un archivo .env con las siguientes variables:

    ```bash
       FLASK_APP=app.py
       FLASK_ENV=development
       DATABASE_URL=sqlite:///tasks.db
       SECRET_KEY=tu_clave_secreta
    ```
    
5. Ejecuta la aplicación:
    ```bash
        python app.py
    ```

## Funcionalidades
- Agregar tareas: Permite agregar nuevas tareas a la lista.
- Eliminar tareas: Permite eliminar tareas existentes.

## Próximas mejoras
- Agregar usuarios y autenticación.