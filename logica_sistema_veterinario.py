# Logica del sistema veterinario para facilitar el uso de testing

mascotas = []

def registrar_mascota(nombre, especie, edad, duenio):
    mascota = {
        "nombre": nombre,
        "especie": especie,
        "edad": edad,
        "duenio": duenio
    }
    mascotas.append(mascota)


def buscar_mascota(nombre):
    for mascota in mascotas:
        if mascota["nombre"].lower() == nombre.lower():
            return mascota
    return None


def eliminar_mascota(nombre):
    for i, mascota in enumerate(mascotas):
        if mascota["nombre"].lower() == nombre.lower():
            del mascotas[i]
            return True
    return False

def listar_mascotas():
    return mascotas.copy()

def contar_mascotas():
    return len(mascotas)


