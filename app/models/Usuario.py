from dataclasses import dataclass
from enum import Enum


class TipoUsuario(Enum):
    CLIENTE: str = 'CLIENTE'
    ADMINISTRADOR: str = 'ADMINISTRADOR'


@dataclass
class Usuario:
    """
    Create a dataclass of an object Usuario.
    """
    dni: str

    nombre1: str = None
    nombre2: str = None

    apellido1: str = None
    apellido2: str = None

    contrasena: str = None

    rol: TipoUsuario = None

    telefono: str = None
    correo: str = None
    direccion: str = None
