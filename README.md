# Resumen
El proyecto quiere servir como backend para una red social con funciones basicas, tales como:
- solicitudes de amistad
- subir publicaciones(en este caso llamadas ideas)
- editar publicaciones
- envio de notificaciones
- registro por medio de correo electrónico
- confirmación por medio de correo electrónico

Hay alguna más pero estas serian las más importantes.

Se utilizan tecnologías tales como:
- docker
- docker-compose
- git
- Django(python)
- Postgres
- GraphQL

Para las notificaciones se utilizaria PushBullet, cada vez que se creara un nuevo post y fuese publico o protegido, se enviará a las personas que te siguen una notificación

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
¡Y ya estaría, el proyecto esta en http://localhost:8000/!
<br/>
<br/>

# Guia de uso
### Crear super usuario
Si queremos ver como afectan los cambios que vayamos efectuando, que mejor manera que create un super usuario
```
$ sudo docker-compose exec web python code/manage.py createsuperuser
```
Podemos ir a [GraphQL](http:/localhost:8000/graphql)

Ahora probemos a crear un usuario, antes de nada si quieres ver tus mensajes en la consola tienes varias opciones,
si deseas únicamente usa
`sudo docker-compose logs -f web` siempre que hayas utilizado antes `sudo docker-compose up -d`.
<br/>

Si no puedes simplemente usar `sudo docker-compose up` y tendrás los logs disponibles, son necesarios para la simulación de envio de emails


Bien ahora probemos a crear un usuario:
![Registro](/fotos/graphql/register.png)
Al crear un usuario nos saldra esto en la consola, necesitaremos copiar el token
![Consola Token](/fotos/console/verification_token.png)

Podemos acceder al [admin panel](http:/localhost:8000/admin) con el *super usuario* para comprobar que el nuevo usuario no esta verificado.
![Registro](/fotos/adminPanel/not_verification.png)

Ahora procedamos a verificar nuestra cuenta con el token antes obtenido
![Verificación Graphl](/fotos/graphql/verification.png)
![Verificación Admin Panel](/fotos/adminPanel/verification.png)



Ahora podemos iniciar sesión estando logeados, teniendo la cuenta activa podemos cambiar de contraseña o
pedir una nueva contraseña.

Probemos a recuperar una contraseña(ahora con insomnia),
primero probemos a autentificarnos.

![Auth Insomnia](/fotos/insomnia/auth.png)
Utilizaremos el token asi que guardarlo con cuidado

**Es importante tener esta configuración en insomnia o postman**
![Auth Insomnia](/fotos/insomnia/header.png)
Como podemos ver el JWT tiene que ser puesto antes del token, el cual caduca a los 60 minutos.

Recuperando la contraseña:
![Change Insomnia](/fotos/insomnia/email_reset_password.png)
Recibiremos un mensaje en la consola:
![Token console](/fotos/console/token_reset.png)
Copiamos el token y:
![Password Reset](/fotos/insomnia/password_reset.png)
hemos cambiado la contraseña, hagámoslo sin necesidad de email:
![Password Reset](/fotos/insomnia/password_change.png)

Genial, ahora probemos a crear un post,
a lo largo de esta guia tendremos tres usuarios: jhon, admin y jhon12,
atentos a las imágenes para saber quien es quien.

Ahora, creemos un post, actualizemoslo y eliminemoslo:

Antes de nada estas son las opciones de visibilidad para el post:

![Post Options](/fotos/code/post_options.png)

![Create Post](/fotos/insomnia/create_post.png)

![Update Post](/fotos/insomnia/update_post.png)

![Delete Post](/fotos/insomnia/delete_post.png)

La imagen del post actualizado fue tomada en otro momento, por eso el pk es diferente a cuando se crea y se elimina.

Ahora, intentemos seguir a alguien, aceptemos la solicitud y por último eliminemos a este seguidor, se utilizaran dos cuentas claramente: jhon y admin para esto:

![Send Follow](/fotos/insomnia/send_follow.png)
![Not Accepted Follow](/fotos/insomnia/not_accepted_yet.png)
![Not Accepted Follow](/fotos/insomnia/accepted_follow.png)
![Delete Follow](/fotos/insomnia/delete_follow.png)


Genial, solo nos quedaría ver la parte de los likes en los posts:

Se ha creado un post con el usuario admin, despues de esto hemos dado a like al post de admin desde la cuenta jhon, se muestra el filtro de likes para posicionar los post según esto, además se incluye otra captura de cuando admin le dio like a un post de jhon para que se vea la comparativa.
Finalmente se muestra como eliminar el like.
![Remove Follow](/fotos/insomnia/create_like_post.png)
![Remove Follow](/fotos/insomnia/order_by_likes_posts_admin.png)
![Remove Follow](/fotos/insomnia/order_by_likes_posts_jhon.png)
![Remove Follow](/fotos/insomnia/delete_like_post.png)

Y eso ha sido todo, agradeceria cualquier comentario que me ayudara a mejorar, en codigo, redacción o lo que sea, muchas gracias.