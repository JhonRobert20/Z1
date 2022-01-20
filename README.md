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

Para las notificaiones se utilizaria PushBullet, cada vez que se creara un nuevo post y fuese publico o protegido se enviaria a las personas que te siguen una notificación

Muchas gracias!
# Requerimientos
Para utilizar el proyecto se necesita docker, docker-compose y git

### Si no sabes como: 
- [documentación docker](https://docs.docker.com/)
- [documentación docker-compose](https://docs.docker.com/compose/)
- [documentación git](https://git-scm.com/doc)

Copia uno por uno los siguientes comandos
```
$ git clone https://github.com/JhonRobert20/z1.git
$ cd z1
$ sudo docker-compose up -d
```
Ahora ya podemos utilizar el proyecto:
```
$ sudo docker-compose up -d
$ sudo docker-compose exec web python code/manage.py migrate
$ sudo docker-compose down
$ sudo docker-compose up -d
```
¡Y ya estaria, el proyecto esta en http://localhost:8000/!

# Guia de uso
### Crear super usuario
Si queremos ver como afectan los cambios que vayamos efectuando, que mejor manera que create un super usuario
```
$ sudo docker-compose exec web python code/manage.py createsuperuser
```
Podemos ir a [GraphQL](http:/localhost:8000/graphql)

Ahora probemos a crear un usuario, antes de nada si quieres ver tus mensajes en la consola tienes varias opciones,
si deseas unicamnete usa
`sudo docker-compose logs -f web` siempre que hayas utilizado antes `sudo docker-compose up -d`.
<br/>

Si no puedes simplemente usar `sudo docker-compose up` y tendras los logs disponibles, son necesarios para la simulacion de envio de emails


Bien ahora provemos a crear un usuario:
![Registro](/fotos/register_graphql.png)
Al crear un usuario nos saldra esto en la consola, necesitaremos copiar el token
![Consola Token](/fotos/verification_token_console.png)

Podemos acceder al [admin panel](http:/localhost:8000/admin) con el *super usuario* para comprobar que el nuevo usuario no esta verificado.
![Registro](/fotos/not_verification_admin_panel.png)

Ahora procedamos a verificar nuestra cuenta con el token antes obtenido
![Registro](/fotos/verification_graphql.png)
![Registro](/fotos/verification_admin_panel.png)



Deberemos guardarnos el token