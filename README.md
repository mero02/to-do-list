# To-Do List App

Una aplicación para gestionar tareas de distintos usuarios utilizando Flask.

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
- Modificar tareas: Permite modificar tareas existentes.
- Eliminar tareas: Permite eliminar tareas existentes.
- Marcar tareas como completadas: Permite marcar tareas como completadas y actualiza su apariencia visual en la tabla.
- Visualización de tareas con categorías y prioridades: Las tareas se muestran con su categoría y prioridad, lo que facilita su gestión.
- Interfaz responsiva: Utiliza Bootstrap para crear una interfaz de usuario adaptativa y amigable para dispositivos móviles y de escritorio.
- Autenticación de usuarios: Los usuarios pueden iniciar sesión para gestionar sus propias tareas. Cada usuario solo puede ver y modificar sus tareas, evitando la mezcla de datos entre usuarios diferentes.

## Próximas mejoras
- Agregar notificaciones tipo "Toast": Mejorar la experiencia del usuario con notificaciones emergentes para las acciones como agregar, editar o eliminar tareas.
- Filtrado y búsqueda de tareas: Agregar funcionalidades para filtrar tareas por fecha de vencimiento, prioridad, estado (completada/no completada) o categoría.
