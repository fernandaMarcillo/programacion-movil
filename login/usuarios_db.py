# Sistema de almacenamiento de usuarios en memoria
usuarios_db = {}
usuario_actual = None


def guardar_usuario(nombre, email, password):
    """Guarda un nuevo usuario en la base de datos en memoria"""
    nuevo_usuario = {
        'nombre': nombre,
        'email': email,
        'password': password
    }
    usuarios_db[email] = nuevo_usuario
    return nuevo_usuario


def obtener_usuario(email_o_nombre):
    """Busca un usuario por email o nombre"""
    for usuario in usuarios_db.values():
        if usuario['email'] == email_o_nombre or usuario['nombre'] == email_o_nombre:
            return usuario
    return None


def verificar_credenciales(email_o_nombre, password):
    """Verifica si las credenciales son correctas"""
    usuario = obtener_usuario(email_o_nombre)
    if usuario and usuario['password'] == password:
        return usuario
    return None


def email_existe(email):
    """Verifica si un email ya está registrado"""
    return email in usuarios_db


def limpiar_sesion():
    """Limpia la sesión del usuario actual"""
    global usuario_actual
    usuario_actual = None


def establecer_usuario_actual(usuario):
    """Establece el usuario actual de la sesión"""
    global usuario_actual
    usuario_actual = usuario


def obtener_usuario_actual():
    """Obtiene el usuario actual de la sesión"""
    return usuario_actual
