# Parcial I - Programación Orientada a Objetos

## Asignatura: Programación Orientada a Objetos

### Tema: Clases, objetos, constructores, estructura de datos y archivos

### 1. Sistema de Gestión de Empleados

Crea una aplicación de gestión de empleados. Debes crear las siguientes clases:

#### Clase Empleado

**Atributos:**
- Nombre (cadena de texto)
- ID (entero)
- Salario Base (flotante)
- Años de Experiencia (entero)

**Métodos:**
- Constructor para inicializar todos los atributos.
- `calcular_salario()`: Retorna el salario total del empleado. El salario total se calcula sumando un bono al salario base que depende de los años de experiencia:
    - Entre 0 y 2 años: bono de 5% del salario base.
    - Entre 3 y 5 años: bono de 10% del salario base.
    - Más de 5 años: bono de 15% del salario base.
- Método para representar al empleado en formato de texto.

#### Clase GestorEmpleados

**Atributos:**
- Una lista de empleados.

**Métodos:**
- `agregar_empleado(empleado: Empleado)`: Agrega un empleado a la lista.
- `eliminar_empleado(id: int)`: Elimina un empleado de la lista según su ID.
- `buscar_empleado(id: int)`: Busca y devuelve un empleado por su ID.
- `editar_empleado(id: int)`: Busca un empleado y permite editar la información del empleado, luego se debe actualizar el archivo donde está guardada la información.
- `mostrar_empleados()`: Muestra todos los empleados de la lista junto con sus salarios totales.
- `guardar_empleados(archivo: str)`: Guarda la lista de empleados en un archivo.
- `cargar_empleados(archivo: str)`: Carga la lista de empleados desde un archivo.

**Requerimiento adicional:** Implementa un sistema de menús que permita al usuario interactuar con la clase `GestorEmpleados`, agregar empleados, eliminarlos, buscar por ID y ver la lista de empleados y sus salarios.

### 2. Sistema de Ventas de Productos con Inventario

Crea un sistema de ventas que gestione productos y clientes. El sistema debe llevar control de los productos en inventario y de las ventas realizadas. Para ello, crea las siguientes clases:

#### Clase Producto

**Atributos:**
- Nombre (cadena de texto)
- ID (entero)
- Precio (flotante)
- Cantidad en inventario (entero)

**Métodos:**
- Constructor para inicializar todos los atributos.
- `disminuir_inventario(cantidad: int)`: Disminuye la cantidad del inventario al realizar una venta.
- `aumentar_inventario(cantidad: int)`: Aumenta la cantidad del inventario al reponer stock.
- `mostrar_informacion()`: Muestra la información del producto en formato legible.

#### Clase Cliente

**Atributos:**
- Nombre (cadena de texto)
- ID (entero)
- Saldo (flotante)

**Métodos:**
- Constructor para inicializar los atributos.
- `realizar_compra(producto: Producto, cantidad: int)`: Reduce el saldo del cliente y reduce la cantidad en inventario del producto, siempre que el saldo y el stock lo permitan.
- `mostrar_informacion()`: Muestra la información del cliente en formato legible.

#### Clase Tienda

**Atributos:**
- Una lista de productos disponibles.
- Una lista de clientes registrados.

**Métodos:**
- `agregar_producto(producto: Producto)`: Agrega un nuevo producto a la lista de productos.
- `agregar_cliente(cliente: Cliente)`: Agrega un cliente a la lista de clientes.
- `realizar_venta(id_cliente: int, id_producto: int, cantidad: int)`: Realiza una venta de un producto a un cliente si se cumplen las condiciones de stock y saldo.
- `mostrar_productos()`: Muestra todos los productos disponibles.
- `mostrar_clientes()`: Muestra todos los clientes registrados.
- `guardar_datos(archivo: str)`: Guarda los productos y clientes en un archivo.
- `cargar_datos(archivo: str)`: Carga los productos y clientes desde un archivo.

### 3. Número Entero de 4 Cifras

Diseñe un programa que reciba un número entero de 4 cifras, diga si el primer número es múltiplo del cuarto número y debe mostrar la suma del segundo número y el tercero (no requiere implementar el paradigma orientado a objetos). Este punto se debe hacer usando operaciones aritméticas para descomponer el número de 4 cifras.

### 4. Algoritmo de Cifrado y Descifrado César

Implemente el algoritmo de cifrado y descifrado César haciendo uso de POO, archivos y listas. Para este algoritmo se deja documentación en la sección de “Parcial I”.