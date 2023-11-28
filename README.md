# ExamenPatronesEstructurales

Link a mi repositorio de [GitHub](https://github.com/pelahumi/ExamenPatronesEstructurales)

## Índice



## Pizzería

### Implementación del patrón
Para la implementación del patrón de diseño Composite, creamos una clase abstracta llamada ```Component```, que básicamente es la interface que implementaremos para crear los menús, ya sean simples (hojas), o compuestos.

#### Clase Hoja
A continuación, definimos todas las clases "Hoja", que representan los componentes más básicos que integran nuestros menús. En nuestro caso tenemos las siguientes: ```Entrantes```, ```Bebidas```, ```Postres```, además de la clase ```Pizza``` que ya estaba creada con el patrón builder. Todas ellas implementan la interface ```Leaf``` que a su vez implementa la clase ```Component```.

#### Clase Combo
La clase ```Combo``` representa la composición de varios elementos hoja. También implementa la interface ```Component```, ya que un combo más grande puede estar compuesto por varios combos más pequeños (como es el caso de nuestro menú pareja, que implementa dos menús simples). Además, la clase ```Combo``` cuenta con un método adicional ```operation()``` el cual calcula el precio del combo sumando el precio de todos sus componentes.

#### Clase DirectorMenus
La clase ```DirectorMenus``` se encarga de crear los menús, para seguir utilizando el patrón builder. Simplemente tiene varios métodos para crear los diferentes menús que tiene nuestra pizzería.

Para ver mejor la estructura del patrón composite creamos el siguiente diagrama UML:

<p align="center">
  <img src="https://github.com/pelahumi/ExamenPatronesEstructurales/assets/91721764/099fdb2a-f06e-4df3-94fd-ac97e7eea46b" alt="CompositeUML">
</p>


### Base de datos
Para guardar toda la información de lo que vende nuestro negocio, hemos creado una base de datos pequeña (SQLite) que contiene una tabla con tres columnas: el id (indice), el precio del combo, y otra para sus elementos. Toda esta información la guardamos en la base de datos que creamos en el fichero baseDatos.py con la función ```guardar_combo()``` ubicada en el fichero auxiliar.py. Esta última función lo que hace es establecer una conexión con la base de datos y añadir a la columna correspondiente el precio y elementos del combo.


## Samur

### Patrón Composite
Para crear los diferentes tipos y jerarquías de documentos, carpetas y links, utilizaremos el patrón Composite, que implementamos en el ejercicio anterio. Donde los elementos más sencillos(hojas) son las clases ```Documentos``` y ```Links``` y la clase ```Carpetas``` es una clase compuesta, que puede contener tanto hojas(documentos y links) como carpetas más pequeñas. 

### Patrón Proxy
Además, se nos pide que para acceder a los documentos el usuario tiene que pasar por un control de acceso. Para ello, implementamos el patrón Proxy, con el fin de que deje pasar únicamente a usuarios que estén registrados en nuestra base de datos. Este patrón se compone de tres clases: la clase ```Subject``` que actúa como interface, la clase ```RealSubject``` que es la que se encarga de realizar la petición del usuario, y la clase ```Proxy```, que se conecta con dos bases de datos: una para comprobar si el usuario está registrado, y otra para registrar el usuario que accede, sus cambios y la hora de acceso. La función ```check_user()``` comprueba si el usuario que quiere acceder a los documentos y devuelve un booleano. Las funciones ```log_user()```, ```log_change()``` y ```log_time()``` se encargan de registrar usuario, si hizo cambios(0 -> no hizo cambios, 1 -> si hizo cambios) y la fecha y hora de acceso, respectivamente. Por último, el método ```request()``` determina si el usuario puede realizar la petición.

<p align="center">
  <img src="https://github.com/pelahumi/ExamenPatronesEstructurales/blob/main/Samur/UMLs/ProxyUML.svg" alt="ProxyUML">
</p>

### Bases de datos
En este ejercicio tenemos dos bases de datos:
  1) usuarios_autorizados: tiene una única columna usuarios, para llevar un registro de los usuarios que pueden tener acceso a los documentos.
  2) acceso: tiene una columna usuario, que registra el usuario, una columna modificacion, que registra si el usuario hizo algún cambio y hora_modificacion que registra la fecha y hora.

### Fichero auxiliar
En este fichero auxiliar.py tenemos una función llamada ```generar_usuario(n)``` que se encarga de generar n usuarios aleatorios y registrarlos en la base de datos correspondiente. Para generar los nombres de usuario de una manera aleatoria, utilizamos la librería Faker.

### Fichero launcher
La función ```launcher()``` se encarga de inicializar todo el programa creando los documentos y archivos, y generando el proxy de acceso y registro.
