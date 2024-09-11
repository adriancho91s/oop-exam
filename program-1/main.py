class Empleado:
    def __init__(self, nombre, id, salario_base, tiempo_de_experiencia):
        self.nombre = nombre
        self.id = id
        self.salario_base = salario_base
        self.tiempo_de_experiencia = tiempo_de_experiencia

    def calcular_salario(self):
        bono = 1.05 if self.tiempo_de_experiencia < 2 else 1.1 if self.tiempo_de_experiencia < 5 else 1.15
        return self.salario_base * bono

    def representar_empleado(self):
        print(f"Nombre: {self.nombre}, ID: {self.id}, Salario base: {self.salario_base}, "
              f"Experiencia: {self.tiempo_de_experiencia} años, Salario total: {self.calcular_salario():.2f}")


class GestorEmpleados:
    def __init__(self, lista_empleados):
        self.lista_empleados = lista_empleados

    def agregar_empleado(self, empleado):
        self.lista_empleados.append(empleado)

    def eliminar_empleado(self, id):
        empleado = self.buscar_empleado(id)
        if empleado:
            self.lista_empleados.remove(empleado)
            print(f"Empleado con ID {id} ha sido eliminado.")
        else:
            print(f"No se encontró ningún empleado con el ID {id}.")

    def buscar_empleado(self, id):
        for elem in self.lista_empleados:
            if elem.id == id:
                return elem
        return None

    def mostrar_empleados(self):
        if not self.lista_empleados:
            print("No hay empleados para mostrar.")
        else:
            for emp in self.lista_empleados:
                emp.representar_empleado()

    def guardar_empleados(self, filename):
        with open(filename, 'w') as file:
            for elem in self.lista_empleados:
                file.writelines(f"{elem.nombre}\n")
                file.writelines(f"{elem.id}\n")
                file.writelines(f"{elem.salario_base}\n")
                file.writelines(f"{elem.tiempo_de_experiencia}\n")

    def cargar_empleados(self, filename):
        try:
            with open(filename, 'r') as file:
                while True:
                    nombre = file.readline().strip()
                    if not nombre:
                        break
                    id = int(file.readline().strip())
                    salario_base = float(file.readline().strip())
                    tiempo_experiencia = int(file.readline().strip())
                    empleado = Empleado(nombre, id, salario_base, tiempo_experiencia)
                    self.agregar_empleado(empleado)
        except FileNotFoundError:
            print(f"El archivo {filename} no se encuentra.")

    def editar_empleado(self, id):
        empleado = self.buscar_empleado(id)
        if not empleado:
            print(f"No se encontró ningún empleado con el ID {id}.")
            return

        print(f"Empleado encontrado: {empleado.nombre}, ID: {empleado.id}")
        while True:
            print("\n¿Qué desea editar?")
            print("1. Nombre")
            print("2. Salario base")
            print("3. Años de experiencia")
            print("4. Salir de la edición")

            opcion = input("Digite el número de la opción que desea editar: ")
            if opcion == "1":
                nuevo_nombre = input("Ingrese el nuevo nombre: ")
                empleado.nombre = nuevo_nombre
            elif opcion == "2":
                nuevo_salario = validar_entrada("Ingrese el nuevo salario base: ", float)
                empleado.salario_base = nuevo_salario
            elif opcion == "3":
                nueva_experiencia = validar_entrada("Ingrese los nuevos años de experiencia: ", int)
                empleado.tiempo_de_experiencia = nueva_experiencia
            elif opcion == "4":
                print("Saliendo de la edición.")
                break
            else:
                print("Opción no válida. Intente de nuevo.")

        # Guardar los cambios en el archivo
        self.guardar_empleados("empleados.txt")
        print(f"Información del empleado {empleado.nombre} actualizada correctamente.")


def solicitar_datos_empleado():
    nombre = input("Digite el nombre del empleado: ")
    id = validar_entrada("Digite el ID del empleado (número entero): ", int)
    salario_base = validar_entrada("Digite el salario base del empleado: ", float)
    tiempo_experiencia = validar_entrada("Digite los años de experiencia del empleado: ", int)
    return Empleado(nombre, id, salario_base, tiempo_experiencia)


def validar_entrada(mensaje, tipo):
    while True:
        try:
            return tipo(input(mensaje))
        except ValueError:
            print(f"Entrada inválida, por favor ingrese un valor {tipo.__name__}.")


def menu_gestor_empleados():
    gestorEmp = GestorEmpleados([])
    gestorEmp.cargar_empleados("empleados.txt")

    while True:
        try:
            opcion = int(input('''
\n\n--- MENU GESTOR DE EMPLEADOS ---
1. Agregar un empleado
2. Eliminar un empleado
3. Buscar un empleado por ID
4. Ver la lista de empleados y sus salarios
5. Editar información de un empleado
6. Salir
Digite el número correspondiente a la opción que desea realizar: '''))
        except ValueError:
            print("Entrada inválida. Por favor, ingrese un número entero.")
            continue

        match opcion:
            case 1:
                empleado = solicitar_datos_empleado()
                if gestorEmp.buscar_empleado(empleado.id):
                    print(f"Actualmente ya se encuentra un empleado registrado con el ID {empleado.id}")
                else:
                    gestorEmp.agregar_empleado(empleado)
                    print(f"Empleado {empleado.nombre} agregado con éxito.")

            case 2:
                id = validar_entrada("Digite el ID del empleado que desea eliminar: ", int)
                gestorEmp.eliminar_empleado(id)
            case 3:
                id = validar_entrada("Digite el ID del empleado que desea buscar: ", int)
                empleado_buscado = gestorEmp.buscar_empleado(id)
                if empleado_buscado:
                    print(f"A continuación se presenta la información del empleado con ID: {id}:")
                    empleado_buscado.representar_empleado()
                else:
                    print(f"No se ha encontrado ningún empleado con el ID {id}.")
            case 4:
                gestorEmp.mostrar_empleados()
            case 5:
                id = validar_entrada("Digite el ID del empleado que desea editar: ", int)
                gestorEmp.editar_empleado(id)
            case 6:
                gestorEmp.guardar_empleados("empleados.txt")
                print("Datos guardados. Saliendo del programa...")
                break
            case _:
                print("Opción ingresada inválida.\n")


# Llamada principal para iniciar el programa
if __name__ == "__main__":
    menu_gestor_empleados()
