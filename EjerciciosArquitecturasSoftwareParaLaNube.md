# CC 2019-2020, Ejercicios Arqutecturas Software para la nube

# Ejercicio 1
# Buscar una aplicación de ejemplo, preferiblemente propia, y deducir qué patrón es el que usa. ¿Qué habría que hacer para evolucionar a un patrón tipo microservicios?

Hace ya unos años desarrollamos un compañero mío y yo en Oviedo una aplicación sencilla basada en el control de votos online y su representación gráfica. Esta aplicación utilizaba HTML, javascript, java y una base de datos MySQL. La aplicación de por si se encargaba de asegurar la identidad de las personas en la aplicación, permitir el voto entre diversas opciones y la representación gráfica de los resultados.
Esta aplicación de por sí podría ser convertida al patrón de los microservicios dividiendo los servicios que ya proporcionábamos y modificándolos para que funcionaran como microservicios.


# Ejercicio 2
# En la aplicación que se ha usado como ejemplo en el ejercicio anterior, ¿podría usar diferentes lenguajes? ¿Qué almacenes de datos serían los más convenientes?

Técnicamente si fuéramos a implementar el patrón de microservicios en la aplicación anterior, no debería de haber problemas con la programación en múltiples lenguajes siempre y cuando estos fueran adaptados correctamente y siguieran el patrón.
Las bases de datos que podríamos utilizar serian variadas, MongoDB, Redis, CosmosDB, SQL… Cada una tiene sus usos y dependería del contexto de la aplicación y del tipo de datos que serian tratados en ella. Es posible incluso que podríamos utilizar múltiples bases de datos diferentes en la aplicación, cada una para un tipo de dato. En esta aplicación la base de datos de los votantes podría utilizar MySQL o SQLlite y los resultados de las votaciones o las votaciones en si utilizasen bases de datos NoSQL.
