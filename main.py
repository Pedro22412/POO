# main.py
from estudiante import Estudiante  # Importamos la clase Estudiante desde estudiante.py

# Lista para almacenar los estudiantes registrados
estudiantes = []

def mostrar_menu():
    print("\n----- MENÚ -----")
    print("1. Registrar nuevo estudiante")
    print("2. Ver estudiantes registrados")
    print("3. Salir")

def registrar_estudiante():
    # Pedimos al usuario los datos del estudiante
    nombre = input("Ingrese el nombre del estudiante: ")
    edad = int(input("Ingrese la edad del estudiante: "))
    direccion = input("Ingrese la dirección del estudiante: ")
    curso = input("Ingrese el curso del estudiante: ")
    
    # Creamos un objeto Estudiante y lo agregamos a la lista
    estudiante = Estudiante(nombre, edad, direccion, curso)
    estudiantes.append(estudiante)
    print(f"Estudiante {nombre} registrado con éxito.")

def ver_estudiantes():
    if not estudiantes:
        print("No hay estudiantes registrados.")
    else:
        print("\n----- Estudiantes Registrados -----")
        for estudiante in estudiantes:
            print(estudiante)

def main():
    while True:
        mostrar_menu()
        opcion = input("Seleccione una opción: ")

        if opcion == '1':
            registrar_estudiante()
        elif opcion == '2':
            ver_estudiantes()
        elif opcion == '3':
            print("¡Hasta luego!")
            break  # Salimos del ciclo y terminamos el programa
        else:
            print("Opción no válida. Por favor, elija nuevamente.")

if __name__ == "__main__":
    main()
