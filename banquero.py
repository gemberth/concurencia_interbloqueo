
# cliente = hilos o procesos
# dinero = recursos instancias
# Banquero = SO con sus recursos 
# requeridos = maximos
# asigndos SO  = asignados
# Instancia o recursos disponibles por SO = disponibles
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
# maximos = [
#     [1,2,2,1,2],
#     [2,2,2,1,0],
#     [2,1,3,1,0],
#     [1,1,2,2,1]
#     ]
# asignados = [
#     [1,0,2,1,1],
#     [2,0,1,1,0],
#     [1,1,0,1,0],
#     [1,1,1,1,0]
#     ]
# disponibles = [0,0,2,1,1]
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

def comprueba_configuracion(asignados, maximos, disponibles):
    finalizados = []
    i = 0
    while(i < len(asignados)):
        if not i in finalizados and puede_progresar(asignados[i], disponibles, maximos[i]):
            print('Finaliza P%s\nDisponibles: %s' % (i,disponibles))
            libera_recursos(asignados[i], disponibles)
            finalizados.append(i)   # Marca el proceso Pi como finalizado
            i = 0
        else:
            i += 1

    if(len(asignados) == len(finalizados)):     # Si todos los procesos finalizan
        print('\nEstado seguro para la configuracion de procesos-recursos dada')
    else:
        print('\nSe produce un interbloqueo')

# Incrementamos la lista de disponibles con los que tenia asignados
def libera_recursos(asignados, disponibles):
    for i in range(len(disponibles)):
        disponibles[i] += asignados[i]

# Devuelve True si el nº de elementos asignados mas los disponibles son mayores o iguales a los requeridos para continuar
def puede_progresar(asignados, disponibles, maximos):
    resultado = True
    for i in range(len(maximos)):
        if(asignados[i] + disponibles[i] < maximos[i]):
            resultado = False
            break
    return resultado



comprueba_configuracion(asignados, maximos, disponibles)