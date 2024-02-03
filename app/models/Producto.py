from dataclasses import dataclass


@dataclass
class Producto:
    id_: int = None
    cod_barra: int = None

    id_almacen: int = None

    nombre: str = None
    descripcion: str = None
    imagen: str = None

    precio: int = None
    stock: int = None
