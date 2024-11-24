from db import conectar

def crear_usuario():
    nombre = input("Ingrese el nombre: ")
    telefono = input("Ingrese el teléfono: ")
    email = input("Ingrese el email: ")
    foto_perfil = input("Ingrese la ruta de la foto de perfil (opcional): ")
    estado = input("Ingrese el estado del usuario (opcional): ")

    conexion = conectar()
    cursor = conexion.cursor()
    query = "INSERT INTO Usuarios (nombre, telefono, email, foto_perfil, estado) VALUES (%s, %s, %s, %s, %s)"
    datos = (nombre, telefono, email, foto_perfil, estado)
    cursor.execute(query, datos)
    conexion.commit()
    print("Usuario creado con éxito.")
    conexion.close()

def listar_usuarios():
    conexion = conectar()
    cursor = conexion.cursor()
    cursor.execute("SELECT * FROM Usuarios")
    usuarios = cursor.fetchall()
    for usuario in usuarios:
        print(usuario)
    conexion.close()

def actualizar_usuario():
    try:
        # Ingresar el ID del usuario (número) y el nuevo nombre
        id_usuario = input("Ingrese el ID del usuario a actualizar: ")
        nuevo_nombre = input("Ingrese el nuevo nombre del usuario: ")

        # Verificar que el ID del usuario sea un número entero
        if not id_usuario.isdigit():
            print("El ID del usuario debe ser un número entero.")
            return

        # Establecer la conexión a la base de datos
        conexion = conectar()
        cursor = conexion.cursor()

        # Consulta SQL para actualizar el nombre del usuario
        query = "UPDATE Usuarios SET nombre = %s WHERE id_usuario = %s"

        # Ejecutar la consulta con los parámetros adecuados
        cursor.execute(query, (nuevo_nombre, int(id_usuario)))  # Convertir id_usuario a entero
        conexion.commit()

        # Verificar si la actualización fue exitosa
        if cursor.rowcount > 0:
            print(f"Usuario con ID {id_usuario} actualizado correctamente.")
        else:
            print(f"No se encontró un usuario con el ID {id_usuario}.")

    except Exception as e:
        print(f"Ocurrió un error: {e}")

    finally:
        # Cerrar la conexión a la base de datos
        cursor.close()
        conexion.close()


def eliminar_usuario():
    # Pedir al usuario que ingrese el nombre del usuario a eliminar
    nombre_usuario = input("Ingrese el nombre del usuario a eliminar: ")

    # Establecer la conexión a la base de datos
    conexion = conectar()
    cursor = conexion.cursor()

    # Consulta SQL para eliminar el usuario por nombre
    query = "DELETE FROM Usuarios WHERE nombre = %s"

    # Ejecutar la consulta SQL con el nombre del usuario
    cursor.execute(query, (nombre_usuario,))
    conexion.commit()  # Confirmar los cambios en la base de datos

    # Verificar si la eliminación fue exitosa
    if cursor.rowcount > 0:
        print(f"Usuario '{nombre_usuario}' eliminado con éxito.")
    else:
        print(f"No se encontró un usuario con el nombre '{nombre_usuario}'.")

    # Cerrar la conexión a la base de datos
    cursor.close()
    conexion.close()