
import socket
import json 
from tkinter import END
# import yaml

HOST = 'localhost'                 # Symbolic name meaning all available interfaces
# HOST = 'localhost'                 # Symbolic name meaning all available interfaces
PORT = 50007
mBuffer=1024


# Create a TCP/IP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# Connect the socket to the port where the server is listening


print('Conectando con el servidor up on {} port {}'.format(HOST, PORT))

sock.connect((HOST, PORT))

try:
    # print(chr(27)+"[1;33m"+"Texto en negrita de color amarillo")
  
    print("\033[;36m"+'Ingrese la cedula a buscar en el servidor')
    cedula=input("\033[;33m"+'Ingrese su cedula: ')
    # Send data
    message = cedula#' '.join(sys.argv[1:]) or 'Mensaje de prueba que se envia al servidor y retorna al cliente'
    # se envia
    print("\033[;32m"+'Enviando {!r}'.format(message))
    sock.sendall(str.encode(message))    
    # Look for the response
    amount_received = 0
    amount_expected = len(message)
    print("Longitud del mensaje:",amount_expected )
    while amount_received < amount_expected:
         data = sock.recv(mBuffer)
         amount_received += len(data)
         string = data.decode()        
         if string == 'None' or string == 'null':
             print("\033[;31m"+'No se encontro el usuario')
         else:   
            
            datosF=json.loads(string)    
            print(type(datosF))       
            print("\033[;36m"+'\nNombres: {} {}\nEdad: {}\nSaldo {}\n'.format(datosF["nombre"],datosF["apellido"],datosF["edad"],datosF["Saldo"]))
               
finally:
    print("\033[;32m"+'closing socket')
    sock.close()

