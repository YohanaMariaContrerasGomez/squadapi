# squadapi
Python FastAPI Create, read, update and delete (CRUD) using PostgreSQL,

## Comenzando 

1. Clonar el repositorio:
`git clone`

2. Crear entorno virtual:
  * Windows:
  Ejecutar en terminal
   * `py -m venv env`
  
3. Iniciar el entorno virtual:
  * Windows:
   * `.\env\Scripts\activate.bat`
  * Mac/linux
   * `source env/bin/activate`
  
4. Instalar librerias:
  * `pip install -r requirements.txt`
  
5. Iniciar el servidor:
  * `uvicorn main:app --reload`

## Conexión a la bd

1. vamos a utilizar la base de datos PostgreSQL
  `CREATE DATABASE squad WITH OWNER = <your-database-user> ENCODING = 'UTF8' CONNECTION LIMIT = -1;`

2. Variables de entorno y settings
  * reemplazar los valores de autenticación y conexión a la base de datos en el archivo **.env**

   ```py
    Database connection
    DB_NAME=to_do_list
    DB_USER=my-user
    DB_PASS=my-pass
    DB_HOST=localhost
    DB_PORT=5432`
  ```

3.  ejecutar script, en la terminal
  * Importamos la función que acabamos de crear y pulsamos enter
  ```py
  from app.v1.scripts.create_tables import create_tables
  ```

4. Una vez importada solo debemos ejecutarla
  ```py
  create_tables()
  ```

## ¿Qué repositorio utilizarías?

Postgre=QL, MariaDB, Casandra, MongoDB, lastic=earch, Oracle, =QL =erver


1. Razona tu respuesta

  Particularmnete me gusta trabajar con Postgres sin embargo esto depende en gran parte de los requerimientos del proyecto En mi opinión particular MySQL y Postgres pueden ser las mejores por la cantidad de soporte disponible.

2. Crea la sentencia para crear la BBDD y el modelo de datos que requerirías

* CREATE DATABASE squad WITH OWNER = <your-database-user> ENCODING = 'UTF8' CONNECTION LIMIT = -1;
* 

3. Lo mismo que el punto anterior (si lo hiciste con una =QL) pero para un repositorio no=QL.
