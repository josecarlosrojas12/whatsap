import mysql.connector

def conectar():
    # Crear y devolver la conexión
    conexion = mysql.connector.connect(
        host="localhost",
        user="root",
        password="12345",
        database="WhatsAppClone"
    )
    return conexion

# Establecer la conexión
conexion = conectar()

try:
    # Crear un cursor para ejecutar consultas
    cursor = conexion.cursor()

    # Consulta para obtener todos los registros de la tabla Usuarios
    cursor.execute("SELECT * FROM Usuarios")
    usuarios = cursor.fetchall()

    # Mostrar los datos de la tabla Usuarios
    print("Usuarios:")
    for usuario in usuarios:
        print(usuario)

    # Consulta para obtener todos los registros de la tabla Chats
    cursor.execute("SELECT * FROM Chats")
    chats = cursor.fetchall()

    # Mostrar los datos de la tabla Chats
    print("\nChats:")
    for chat in chats:
        print(chat)

    # Consulta para obtener todos los registros de la tabla Mensajes
    cursor.execute("SELECT * FROM Mensajes")
    mensajes = cursor.fetchall()

    # Mostrar los datos de la tabla Mensajes
    print("\nMensajes:")
    for mensaje in mensajes:
        print(mensaje)

    # Consulta para obtener todos los registros de la tabla Contactos
    cursor.execute("SELECT * FROM Contactos")
    contactos = cursor.fetchall()

    # Mostrar los datos de la tabla Contactos
    print("\nContactos:")
    for contacto in contactos:
        print(contacto)

finally:
    # Cerrar el cursor y la conexión
    cursor.close()
    conexion.close()
