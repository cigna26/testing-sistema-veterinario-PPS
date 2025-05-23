# test_logica_sistema_veterinario.py

import pytest
from logica_sistema_veterinario import mascotas, registrar_mascota

@pytest.fixture
def limpiar_mascotas():
    mascotas.clear()
    return mascotas

def test_registro(limpiar_mascotas):
    registrar_mascota('Luna', 'gato', '3', 'Ana')
    assert len(limpiar_mascotas) == 1
    assert limpiar_mascotas[0]['nombre'] == 'Luna'
