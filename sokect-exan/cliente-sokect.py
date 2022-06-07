
import socket
import sys
import json
import ast
import base64
import re
from tkinter import END


HOST = '25.11.139.228'                 # Symbolic name meaning all available interfaces
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
         string = data.decode("utf-8") 
        # string = string.replace("\'", "")   
         string = re.sub("\!|\'|\?","",string)
        #string=re.sub(r"^\s+|\s+$", "", string)  
        
      
         if string == 'None' :
             print("\033[;31m"+'No se encontro el usuario')
         else:
            
               
            datosF = dict(toks.split(":") for toks in string.split(",") if toks)     
            # print(datosF)
            print("\033[;32m"+'\nNombres: {}{}\nEdad: {}\nSaldo{}\n'.format(datosF[" nombre"],datosF[" apellido"],datosF[" edad"],datosF[" Saldo"]))
            
          
            # print(datosF[" cedula"])
            
            # print("\033[;32m"+'Datos del usuario:')
            # print("\033[;32m"+'Nombre:',datosF['nombre'])
            # print("\033[;32m"+'Apellido:',datosF['apellido'])
            # print("\033[;32m"+'Edad:',datosF['edad'])
            # print("\033[;32m"+'Cedula:',datosF['cedula'])
            # print("\033[;32m"+'Saldo:',datosF['Saldo'])

            # data = data.replace("\'", "\"")
            # output_dict = json.loads(data) 
            # data=data.decode('utf-8')
            # data = data.replace("\'", "\"")
            # ascii_message = data.encode('ascii')
            # output_byte = base64.b64encode(ascii_message)

             # convert string dictionary to dict format
         #print('received {!r}'.format(data))
    
finally:
    print('closing socket')
    sock.close()

