************************Introducción*****************************

Este repositorio lo he creado para compartirles la idea de CRUD que he tenido. Decido hacerlo en python ya que me parece mas facil, que Java.
Al principio solo se maneja a través de consola, ya que considero que es mas facil crear todo el CRUD como back-end
y luego crearle una vista front a cada funcionalidad.
Es solamente una idea, no estoy diciendo que debe ser así.

Por el momento existen dos clases:

1. Clase Producto:

    En este clase se definen los parametros del producto, los constructores y los modificadores. (Ver el archivo producto.py)
    
    Parametros
    Código
    Nombre
    Descripción
    Tipo
    Sabor
    Marca
    Presentación
    Gramaje
    Valor
    
2. Clase Validacion
    
    En esta clase se crea una lógica de validación donde el parametro ingresado por parte del admin del cátalogo debe cumplir
    con un mínimo y un máximo de caracteres. El cual se plantea así:
        
        Código min 1 y max 5
        Nombre min 3 y max 100
        Descripción min 20 y max 250
        Tipo min 1 y max 50
        Sabor min 4 y max 20
        Marca min 3 y max 20
        Presentación min 8 y max 20
        Gramaje min 1 y max 1000
        Valor min 100 y max 50000
        
En el archivo main.py se crea un menu para consola, una función run para ejecutar el menu, una función crear producto, y una función check, 
para conectar la clase Validacion con la entrada de datos que vaya a ejecutar el admin del cátalogo. (Ver archivo main.py para detalles)

Es este momento estoy investigando como agregar esta entrada de datos a una base de datos SQL.
