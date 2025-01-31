# Experimentación Docker

Los experimentos con los diferentes tipos de Docker nos dejaron las siguientes conclusiones, los Docker creados con Python-alpine o python-slim-buster contienen el mínimo de espacio necesario para el correcto funcionamiento de nuestro sistema. 

La creación de un Docker con alpine, instalando python unicamente, nos dio una imagen muy ligera, que aunque no llegaba a tener tan poco peso como python-alpine era bastante aceptable. 

La imagen creada utilizando el sistema operativo fedora fue bastante ligera en comparación con las imágenes creadas utilizando pyhon-alpine y Python-slim-buster. 

Podemos observar los resultados obtenidos de la experimentación en la siguiente imagen:
![Pesos Dockers]( https://raw.githubusercontent.com/OscarRubioGarcia/CC/blob/master/example/Docker-pesos.jpg)

Procedí a diseñar un archivo Docker sencillo con alpine, debido a ser esta una de las opciones más populares y a que mi experimentación me llevo a concluir que esta era la imagen más ligera, adicionalmente me gusto tener la posibilidad de actualizar el software y establecer el entorno de python manualmente.

Explicaremos el contenido del Docker a continuación:

```python
FROM alpine:3.10
MAINTAINER Oscar Rubio Garcia 

WORKDIR /code

RUN apk update && apk upgrade 
RUN apk add --update py-pip
RUN apk add linux-headers python3 py3-virtualenv

ENV VIRTUAL_ENV=/opt/venv
RUN python3 -m virtualenv --python=/usr/bin/python3 $VIRTUAL_ENV
ENV PATH="$VIRTUAL_ENV/bin:$PATH"

COPY requirements-img.txt requirements.txt
RUN pip install -r requirements.txt
COPY . /code

CMD [ "python", "app.py" ]
```

Para empezar, establecemos la imagen utilizada a ser una imagen que contenga en este caso el sistema alpine. Después definimos el entorno de trabajo en la imagen Docker que crearemos, en este caso el entorno será el directorio /code, adicionalmente estableceremos el maintainer del Docker siendo yo como autor.

Procedemos con la fase de preparación de la imagen Docker, aquí nos aseguramos de que el sistema esta actualizado y al día, tras actualizar el sistema procedemos a la instalación de aquellos programas indispensables para el correcto funcionamiento de nuestro microservicio. En nuestro caso instalaremos pip, las cabeceras de linux para prevenir errores y python3 con su entorno.

Tras instalar python3 procedemos a asegurarnos que el entorno del entorno virtual de python es configurado correctamente con el fin de evitar posibles errores debidos a la falta de módulos. Este apartado fue desarrollado gracias al tutorial proporcionado en este [enlace.](https://pythonspeed.com/articles/activate-virtualenv-dockerfile/)

A continuación, empezamos el proceso de creación de la imagen Docker, copiamos el archivo de requirements-img.txt de nuestro proyecto, el cual contiene solamente las dependencias necesarias a instalar en la imagen Docker para que funcione el proyecto, a un archivo requirements.txt en la imagen Docker. Proseguimos utilizando pip para instalar todas las dependencias del archivo requirements.txt en la imagen Docker. Despues, copiamos el resto de los archivos del proyecto en el directorio /code que creamos anteriormente.

El paso final será la utilización del comando cmd para inicializar el microservicio, utilizamos Python app.py para ejecutar el archivo Python en la imagen del Docker e inicializar el proyecto.

Tras la creación del archivo Docker procedimos a su generación, despliegue y subida a Docker Hub utilizando los siguientes comandos:
* Docker image build . -t microservicionews:1.4

Usando este comando especificamos la creación de una imagen Docker basándonos en el directorio en el cual estamos situados y damos como tag a nuestro nombre el nombre de microservicionews con versión 1.3

Comprobamos la creación y tamaño de nuestra imagen Docker utilizando:

* Docker image ls

En nuestro caso el Docker fue creado con un tamaño de 173MB. 

Procedemos a probar el correcto comportamiento del docker:

* Docker container run –-publish 5000:5000 microservicionews:1.4

Este comando se encarga de ejecutar el Docker que especificamos como microservicionews:1.3 y de publicarlo al puerto 5000:5000, que es el puerto por predefinido que estamos utilizando con Python flask.

* Docker login

Realizamos un login en el servidor de Docker hub, con el fin de tener los permisos necesarios para realizar la subida de la imagen al repositorio previamente creado.

* Docker push oscarrubiogarcia/proyectoccdocker:microservicionews

Comando utilizado para subir la imagen especificada como microservicionews al repositorio oscarrubiogarcia/proyectoccdocker. Destacaremos que previamente realizamos el comando Docker tag para cambiar el nombre de nuestro Docker.

Una vez realizados estos comandos obtendríamos la imagen del Docker creado de alpine, en nuestro repositorio de Docker hub. A continuación, desplegaremos nuestro docker en heroku, para hacer esto tendremos que crear un archivo heroku.yml en nuestro proyecto, preferiblemente junto a nuestro archivo Dockerfile.
