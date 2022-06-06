# -*- coding: utf-8 -*-
"""
Created and adapted on Fri Nov 4 14:44:26 2021
@author: Willian
"""


import socket
import sys
import ast


HOST = 'localhost'                 # Symbolic name meaning all available interfaces
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
        data = data.decode("utf-8")
        amount_received += len(data)
        
        
        

        if len(data) ==None :
            print("\033[;31m"+'No se encontro el usuario')
            
        else:
            # dict_str = data.decode("UTF-8")
            # mydata = ast.literal_eval(dict_str)
            # print(repr(mydata))
            print(data)
            print (type(data))
            # data=data.decode('utf-8')
            # data=data.split(',')
            # print("\033[;32m"+'Datos del usuario:')
            # print("\033[;32m"+'Nombre:',data[2])
            # print("\033[;32m"+'Apellido:',data[3])
            # print("\033[;32m"+'Edad:',data[4])
            # print("\033[;32m"+'Saldo:',data[6])
                         
            #  print(data)
            #  print (type(data))
             
            # #  m=data
            # #  print("\033[;32m"+'Cedula:',m[2][2])
             
            # #  print("\033[;32m"+'Recibido {!r}'.format(data.decode()))
            # #  print("\033[;32m"+'Recibido {!r}'.format(m))
            # #  print("\033[;32m"+'Datos del usuario:')
             

            # #  mensag=mensag.split(',')
            # #     print("\033[;32m"+'Datos del usuario:')
            # #     print("\033[;32m"+'Cedula:',mensag[0])
            # #     print("\033[;32m"+'Nombre:',mensag[1])
            # #     print("\033[;32m"+'Apellido:',mensag[2])
            # #     print("\033[;32m"+'Edad:',mensag[3])
            # #     print("\033[;32m"+'Sexo:',mensag[4])
            #  print("\033[;32m"+'Nombre: {}, Cedula: {}, Telefono: {}'.format(data[1],data[2],data[3]))
            #   for user in data:
                
            # print("\033[;32m"+'Recibiendo dato: {}'.format(data['cedula']))
            # print("{organization} is {adjective}!".format(organization="freeCodeCamp", adjective="awesome"))
         #print('received {!r}'.format(data))
    
finally:
    print('closing socket')
    sock.close()

