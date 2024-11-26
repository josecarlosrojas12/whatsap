from db import conectar

def crear_mensaje():
    id_chat = input("Ingrese el ID del chat: ")
    id_usuario = input("Ingrese el ID del usuario: ")
    contenido = input("Ingrese el contenido del mensaje: ")
    tipo_mensaje = input("Ingrese el tipo de mensaje (texto, imagen, audio, etc.): ")

    conexion = conectar()
    cursor = conexion.cursor()
    query = "INSERT INTO Mensajes (id_chat, id_usuario, contenido, tipo_mensaje) VALUES (%s, %s, %s, %s)"
    datos = (id_chat, id_usuario, contenido, tipo_mensaje)
    cursor.execute(query, datos)
    conexion.commit()
    print("Mensaje creado con éxito.")
    conexion.close()

def listar_mensajes():
    id_chat = input("Ingrese el ID del chat para listar los mensajes: ")

    conexion = conectar()
    cursor = conexion.cursor()
    query = "SELECT * FROM Mensajes WHERE id_chat=%s"
    cursor.execute(query, (id_chat,))
    mensajes = cursor.fetchall()
    for mensaje in mensajes:
        print(mensaje)
    conexion.close()