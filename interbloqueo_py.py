#---------------------------------------------------------------------------------------#
print("\n#-------------------Algoritmo del banquero-------------------#\n")

def comprobar(asignados, maximos, disponibles):
    finalizados = []
    i = 0
    while(i < len(asignados)):
        if not i in finalizados and puede_ejecutar(asignados[i], disponibles, maximos[i]):
            print('Finaliza P%s\nDisponibles: %s' % (i,disponibles))
            liberar_recursos(asignados[i], disponibles)
            finalizados.append(i) # Marca el proceso Pi como finalizado.
            i = 0
        else:
            i += 1
    if(len(asignados) == len(finalizados)): # Si todos los procesos finalizan.
        print('\n--> Estado seguro <--')
    else:
        print('\n--> Se produjo un interbloqueo <--')

def liberar_recursos(asignados, disponibles):
    for i in range(len(disponibles)):
        disponibles[i] += asignados[i] # Sumo los disponibles con los que tenia asignados.
    print('Recursos liberados --> Disponibles:',disponibles)

def puede_ejecutar(asignados, disponibles, maximos):
    print('Asignados:',asignados, 'Diponibles:',disponibles, 'Maximos:',maximos)
    resultado = True
    for i in range(len(maximos)):
        if(asignados[i] + disponibles[i] < maximos[i]):
            resultado = False # No puede sastifacer con esa Disponibilidad ninguna Necesidad.
            break # El proceso queda bloqueado esperando.
    print('Resultado: ',resultado)
    return resultado
# Devuelve True si la cantidad de elementos asignados mas los disponibles son 
# mayores o iguales a los requeridos para ejecutar. Existencia = Disponibles + Asignados.

#---------------------------------------------------------------------------------------#
maximos = [
    [3,2,2],
    [6,1,3],
    [3,1,4],
    [4,2,2]
    ]
asignados = [
    [1,0,0],
    [6,1,2],
    [2,1,1],
    [0,0,2]
    ]
disponibles = [0,1,1]
# EJEMPLO 1 - Estado seguro
# asignados = [
#     [1,0,0],
#     [1,1,0],
#     [0,1,0]
#     ]

# maximos = [
#     [1,1,0],
#     [1,1,0],
#     [1,1,0]
#     ]

# disponibles = [0,0,1]

# EJEMPLO 2 - Interbloqueo
# asignados = [
#     [1,0,0],
#     [0,1,0],
#     [0,0,0],
#     [0,0,1]
#     ]

# maximos = [
#     [1,1,0],
#     [1,1,0],
#     [0,1,1],
#     [0,0,1]
#     ]
# disponibles = [0,0,0]

comprobar(asignados, maximos, disponibles)