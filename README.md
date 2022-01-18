# Resumen
El proyecto quiere servir como backend para una red social con funciones basicas, tales como:
- solicitudes de amistad
- subir publicaciones(en este caso llamadas ideas)
- editar publicaciones
- envio de notificaciones
- registro por medio de correo electronico
- confirmación por medio de correo electronico

Hay alguna más pero estas serian las más importantes.

Se utilizan tecnologias tales como:
- docker
- docker-compose
- git
- Django(python)
- Postgres
- GraphQL

Muchas gracias!
# Requerimientos
Para utilizar el proyecto se necesita docker, docker-compose y git

Si no sabes como: 
- [documentación docker](https://docs.docker.com/)
- [documentación docker-compose](https://docs.docker.com/compose/)
- [documentación git](https://git-scm.com/doc)

Copia uno por uno los siguientes comandos
```
$ git clone https://github.com/JhonRobert20/z1.git
$ cd z1
$ sudo docker-compose up -d db
$ sudo docker-compose exec db bash
```

En este punto estaremos en el bash, dentro de el usar:
```
$ psql -U postgres
```
En este punto estaremos dentro de la consola de postgres
```
$ CREATE USER testUser WITH PASSWORD 'testUser';
$ CREATE USER z1 WITH PASSWORD 'adminZ1';
$ CREATE DATABASE test;
$ CREATE DATABASE entrevista;
$ GRANT ALL PRIVILEGES ON DATABASE test TO testUser;
$ GRANT ALL PRIVILEGES ON DATABASE entrevista TO z1;
$ exit
$ exit
```
Ahora ya podemos utilizar el proyecto:
```
$ sudo docker-compose up -d
$ sudo docker-compose exec web python code/manage.py migrate
$ sudo docker-compose down
$ sudo docker-compose up
```
¡Y ya estaria, el proyecto esta en http://localhost:8000/!