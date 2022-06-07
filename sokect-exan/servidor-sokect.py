import socket
from db import  get_user

# Bind the socket to the port
HOST = '25.11.139.228'                 # Symbolic name meaning all available interfaces
PORT = 50007  
mBuffer=1024

# Create TCP Socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

print('Iniciando el servidor up on {} port {}'.format(HOST, PORT))
sock.bind((HOST, PORT))
# Listen for incoming connections
sock.listen(1)


while True:
    # espera la conn.
    print('Esperando conectar con un cliente')
    connection, client_address = sock.accept()
    try:
        print('Conectado desde', client_address)

        # Receive the data in small chunks and retransmit it
        while True:
            print('-------------------------------')
            data = connection.recv(mBuffer)#16
            decodificado = data.decode("utf-8")
            dataConsulta = get_user(decodificado)
            usuario = str(dataConsulta)
            # print('Recibiendo dato: {!r}'.format(data))
            
            if data:
                print('Enviando respuesta al cliente')
                datoUsuario = usuario.encode()
                connection.sendall(datoUsuario)
            else:#No existe datos, client_address
                break
    except KeyboardInterrupt:
        break
    finally:
        # Clean up the connection
        connection.close()

  