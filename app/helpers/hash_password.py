from app.models.Usuario import Usuario

from werkzeug.security import generate_password_hash
from werkzeug.security import check_password_hash


def hash_password(usuario: Usuario):
    """Create and modify the current user password into a hashed password.

    Args:
        usuario (Usuario): user instance with a password diferrent of None.
    """
    usuario.contrasena = generate_password_hash(usuario.contrasena)


def check_hashed_password(usuario: Usuario, password: str) -> bool:
    """check if a given password is equal to the actual user password.

    Args:
        usuario (Usuario): the user with a hashed password
        password (str): the password to be compared with.

    Returns:
        bool: True, if the passwords are equals, otherwhise False.
    """
    return check_password_hash(usuario.contrasena, password)
