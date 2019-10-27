# Desarrollo basado en pruebas

## Ejercicio 1:

Instalar alguno de los entornos virtuales de node.js (o de cualquier otro lenguaje con el que se esté familiarizado) y, con ellos, instalar la última versión existente, la versión minor más actual de la 4.x y lo mismo para la 0.11 o alguna impar (de desarrollo).

![Microservicios]( https://raw.githubusercontent.com/OscarRubioGarcia/CC/master/Images/EjeT2_1.jpg )
Verificación de la instalacion de nvm

![Microservicios]( https://raw.githubusercontent.com/OscarRubioGarcia/CC/master/Images/EjeT2_2.jpg )
Instalación de la última versión de node.js

![Microservicios]( https://raw.githubusercontent.com/OscarRubioGarcia/CC/master/Images/EjeT2_3.jpg )
Instalación de versión 4.9 de node.js

![Microservicios]( https://raw.githubusercontent.com/OscarRubioGarcia/CC/master/Images/EjeT2_4.jpg )
Instalación de versión 0.11.9 de node.js

## Ejercicio 2:

Crear una descripción del módulo usando package.json. En caso de que se trate de otro lenguaje, usar el método correspondiente.
Descripción del módulo package.json

{
  "author": "Oscar Rubio Garcia (https://github.com/OscarRubioGarcia/CC )",
  "name": "porrio",
  "description": "Apuesta en una porra",
  "version": "0.0.1",
  "repository": {
    "url": "git://github.com/OscarRubioGarcia/CC.git "
  },
  "main": "./Apuesta.js",
  "scripts": {
    "test": "make test"
  },
  "dependencies": {
    "sqlite": "^3.0.3",
    "sqlite3": "~3.0"
  },
  "devDependencies": {
  },
  "optionalDependencies": {},
  "engines": {
    "node": ">=0.8"
  }
}

## Ejercicio 3:

Descargar el repositorio de ejemplo anterior, instalar las herramientas necesarias (principalmente Scala y sbt) y ejecutar el ejemplo desde sbt. Alternativamente, buscar otros marcos para REST en Scala tales como Finatra o Scalatra y probar los ejemplos que se incluyan en el repositorio.

![Microservicios]( https://raw.githubusercontent.com/OscarRubioGarcia/CC/master/Images/EjeT2_5.jpg )
Descarga del ejemplo

![Microservicios]( https://raw.githubusercontent.com/OscarRubioGarcia/CC/master/Images/EjeT2_6.jpg )
Ejecución en proceso del comando sbt en el directorio del proyecto

![Microservicios]( https://raw.githubusercontent.com/OscarRubioGarcia/CC/master/Images/EjeT2_7.jpg )
SBT termina de actualizar y inicia correctamente en el proyecto

![Microservicios]( https://raw.githubusercontent.com/OscarRubioGarcia/CC/master/Images/EjeT2_8.jpg )
Extracto del comando compile en sbt

![Microservicios]( https://raw.githubusercontent.com/OscarRubioGarcia/CC/master/Images/EjeT2_9.jpg )
Compilación correcta del proyecto

![Microservicios]( https://raw.githubusercontent.com/OscarRubioGarcia/CC/master/Images/EjeT2_10.jpg )
Ejecución de los tests del proyecto correctamente

![Microservicios]( https://raw.githubusercontent.com/OscarRubioGarcia/CC/master/Images/EjeT2_11.jpg )
Inicialización del proyecto en http://localhost:8080/

![Microservicios]( https://raw.githubusercontent.com/OscarRubioGarcia/CC/master/Images/EjeT2_12.jpg )
Realización de peticiones al proyecto en localhost:8080

![Microservicios]( https://raw.githubusercontent.com/OscarRubioGarcia/CC/master/Images/EjeT2_13.jpg )
Realización de petición PUT en el proyecto en localhost:8080

![Microservicios]( https://raw.githubusercontent.com/OscarRubioGarcia/CC/master/Images/EjeT2_14.jpg )
Parada del despliegue en localhost:8080 de la aplicación utilizando re-stop

## Ejercicio 4:

Para la aplicación que se está haciendo, escribir una serie de aserciones y probar que efectivamente no fallan. Añadir tests para una nueva funcionalidad, probar que falla y escribir el código para que no lo haga. A continuación, ejecutarlos desde mocha (u otro módulo de test de alto nivel), usando descripciones del test y del grupo de test de forma correcta. Si hasta ahora no has subido el código que has venido realizando a GitHub, es el momento de hacerlo, porque lo vamos a necesitar un poco más adelante
	
	--Esperar a después del seminario--

## Ejercicio 5:

1.	Darse de alta. Muchos están conectados con GitHub por lo que puedes usar directamente el usuario ahí. A través de un proceso de autorización, acceder al contenido e incluso informar del resultado de los tests.
2.	Activar el repositorio en el que se vaya a aplicar la integración continua. Travis permite hacerlo directamente desde tu configuración; en otros se dan de alta desde la web de GitHub.
3.	Crear un fichero de configuración para que se ejecute la integración y añadirlo al repositorio.


![Microservicios]( https://raw.githubusercontent.com/OscarRubioGarcia/CC/master/Images/EjeT2_15.jpg )
Autorización de Travis en GitHub

![Microservicios]( https://raw.githubusercontent.com/OscarRubioGarcia/CC/master/Images/EjeT2_16.jpg )
Activación del proyecto en Travis

![Microservicios]( https://raw.githubusercontent.com/OscarRubioGarcia/CC/master/Images/EjeT2_17.jpg )
Creación del archivo .travis.yml en el proyecto

![Microservicios]( https://raw.githubusercontent.com/OscarRubioGarcia/CC/master/Images/EjeT2_18.jpg )
Archivo .travis.yml

![Microservicios]( https://raw.githubusercontent.com/OscarRubioGarcia/CC/master/Images/EjeT2_19.jpg )
Integración de Travis en el proyecto, técnicamente falla debido a la falta de archivos de test

