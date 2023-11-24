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
