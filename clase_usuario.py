class Usuario:
    def __init__(self, nombre_usuario, contraseña):
        self.nombre_usuario = nombre_usuario
        self.contraseña = contraseña

# Crear un objeto de la clase Usuario
usuario1 = Usuario("Manolito", "Shhhhhhh")

# Visualizamos nombre usuario
print("Nombre de usuario:", usuario1.nombre_usuario)

# Visualizamos contraseña de usuario
print("Contraseña:", usuario1.contraseña)