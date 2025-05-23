# test_logica_sistema_veterinario.py

import pytest
from logica_sistema_veterinario import mascotas, registrar_mascota

@pytest.fixture
def limpiar_mascotas():
    mascotas.clear()
    return mascotas

# TEST UNITARIOS

def test_registro(limpiar_mascotas):
    registrar_mascota('Luna', 'gato', '3', 'Ana')
    assert len(limpiar_mascotas) == 1
    assert limpiar_mascotas[0]['nombre'] == 'Luna'


def test_busqueda_existente(limpiar_mascotas):
    limpiar_mascotas.append({'nombre': 'Max',
                            'especie': 'perro',
                            'edad': '2',
                            'duenio': 'Luis'})
    resultado = any(m['nombre'].lower() == 'max' for m in limpiar_mascotas)
    assert resultado is True

def test_eliminacion(limpiar_mascotas):
    limpiar_mascotas.append({'nombre': 'Rocky',
                            'especie': 'loro',
                            'edad': '1',
                            'duenio': 'Pedro'})
    limpiar_mascotas[:] = [m for m in limpiar_mascotas if m['nombre'].lower() != 'rocky']
    assert len(limpiar_mascotas) == 0