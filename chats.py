from db import conectar

def crear_chat():
    tipo_chat = input("Ingrese el tipo de chat (individual o grupal): ")
    nombre_chat = input("Ingrese el nombre del chat (opcional): ")
    foto_chat = input("Ingrese la ruta de la foto del chat (opcional): ")

    conexion = conectar()
    cursor = conexion.cursor()
    query = "INSERT INTO Chats (tipo_chat, nombre_chat, foto_chat) VALUES (%s, %s, %s)"
    datos = (tipo_chat, nombre_chat, foto_chat)
    cursor.execute(query, datos)
    conexion.commit()
    print("Chat creado con éxito.")
    conexion.close()

def listar_chats():
    conexion = conectar()
    cursor = conexion.cursor()
    cursor.execute("SELECT * FROM Chats")
    chats = cursor.fetchall()
    for chat in chats:
        print(chat)
    conexion.close()