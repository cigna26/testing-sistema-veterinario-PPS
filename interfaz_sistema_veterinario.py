# Interfaz grafica para uso de usuario

mascotas = []

def registrar_mascota():
    nombre = input("Nombre de la mascota: ")
    especie = input("Especie (ej: perro, gato): ")
    edad = input("Edad: ")
    duenio = input("Nombre del dueño: ")
    mascota = {
        "nombre": nombre,
        "especie": especie,
        "edad": edad,
        "duenio": duenio
    }
    mascotas.append(mascota)
    print("Mascota registrada correctamente.\n")

def buscar_mascota():
    nombre = input("Ingrese el nombre de la mascota a buscar: ")
    for mascota in mascotas:
        if mascota["nombre"].lower() == nombre.lower():
            print(f"🔎 {mascota['nombre']} es un(a) {mascota['especie']} de {mascota['edad']} años. Dueño: {mascota['duenio']}\n")
            return
    print("Mascota no encontrada.\n")

def eliminar_mascota():
    nombre = input("Ingrese el nombre de la mascota a eliminar: ")
    for i, mascota in enumerate(mascotas):
        if mascota["nombre"].lower() == nombre.lower():
            del mascotas[i]
            print("🗑️ Mascota eliminada.\n")
            return
    print("Mascota no encontrada.\n")

def listar_mascotas():
    if not mascotas:
        print("📭 No hay mascotas registradas.\n")
        return
    print("Lista de mascotas registradas:")
    for i, mascota in enumerate(mascotas, 1):
        print(f"{i}. {mascota['nombre']} - {mascota['especie']} - {mascota['edad']} años - Dueño: {mascota['duenio']}")
    print()

def contar_mascotas():
    total = len(mascotas)
    print(f"🐾 Hay {total} mascota(s) registrada(s).\n")

def mostrar_menu():
    print("=== SISTEMA VETERINARIO ===")
    print("1. Registrar mascota")
    print("2. Buscar mascota por nombre")
    print("3. Eliminar mascota")
    print("4. Listar todas las mascotas")
    print("5. Contar mascotas")
    print("6. Salir")

def ejecutar():
    while True:
        mostrar_menu()
        opcion = input("Seleccione una opción: ")
        print()
        if opcion == "1":
            registrar_mascota()
        elif opcion == "2":
            buscar_mascota()
        elif opcion == "3":
            eliminar_mascota()
        elif opcion == "4":
            listar_mascotas()
        elif opcion == "5":
            contar_mascotas()
        elif opcion == "6":
            print("👋 ¡Gracias por usar el sistema veterinario!")
            break
        else:
            print("⚠️ Opción inválida. Intente nuevamente.\n")

if __name__ == '__main__':
    ejecutar()
