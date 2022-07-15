from pymongo import MongoClient # El cliente de MongoDB
from bson.objectid import ObjectId # Para crear ObjectId, porque _id como cadena no funciona
import time

class Cliente:
    def __init__(self, nombres, direccion, email, saldo,cedula):
        self.nombres = nombres
        self.direccion = direccion
        self.email = email
        self.saldo = saldo
        self.cedula = cedula
        
def obtener_bd():

    nameBD = "banco_uleam"
    #cliente = MongoClient("mongodb://{}:{}@{}:{}/?replicaSet=rsfacci".format(user, pwd, host, port))
    cliente = MongoClient("mongodb://administrador:asd123@server-jarod,server-natalia,server-karla,server-gember/?replicaSet=rsfacci&authMechanism=DEFAULT")
    return cliente[nameBD]

def insertar(cliente):
    BD = obtener_bd()
    clientes = BD.estudiante
    return clientes.insert_one({
        "nombres": cliente.nombres,
        "direccion": cliente.direccion,
        "email": cliente.email,
        "saldo": cliente.saldo,
        "cedula": cliente.cedula
    }).inserted_id

def actualizar(id, saldo, tipo):
    BD = obtener_bd()
    saldoObt = BD.estudiante.find_one({'_id': ObjectId(id)})
    if tipo == 1:
        resultado = BD.estudiante.update_one(
            {
             '_id': ObjectId(id)
            }, 
            {
                '$set': {
                    "saldo": round(saldoObt['saldo']+saldo, 2)
                }
            })
        return "¡Saldo actualizado correctamente!"
    else:
        if saldoObt['saldo'] >= saldo:
            resultado = BD.estudiante.update_one(
                {
                 '_id': ObjectId(id)
                }, 
                {
                    '$set': {
                        "saldo": round(saldoObt['saldo']-saldo, 2)
                    }
                })
            return "¡Saldo actualizado correctamente!"
        else:
            return "¡Sin saldo disponible intente nuevamente!"


def eliminar(id):
    DB = obtener_bd()
    resultado = DB.estudiante.delete_one(
        {
        '_id': ObjectId(id)
        })
    return resultado.deleted_count

def eliminarTodo():
    DB = obtener_bd()
    resultado = DB.estudiante.delete_many({})
    return resultado.deleted_count

def obtener():
    BD = obtener_bd()
    return BD.estudiante.find()

def obtenerCant():
    BD = obtener_bd()
    return BD.estudiante.estimated_document_count()

menu = """\n ¿QUÉ DESEAS HACER?.
1 - Ingresar estudiante
2 - Ver todos los estudiantes
3 - Eliminar estudiante
4 - Eliminar todos los estudiantes
5 - Depositar
6 - Retirar
7 - Salir"""

accion = None

while accion != 7:
    print(menu)
    accion = int(input("Acción: "))
    if accion == 1:
        ingresar =int(input("Ingrese el numero de registros a registrar: "))
        #cliente = Producto(nombres, direccion, email, saldo)
        x = 1
        while x <= ingresar:
            nombres = input("Ingrese nombres: ")
            direccion = input("Ingrese dirección: ")
            email = input("Ingrese email: ")
            saldo = float(input("Ingrese saldo: "))
            cedula = float(input("Ingrese cedula: "))
            cliente = Cliente(nombres, direccion, email, saldo,cedula)
            print("¡Estudiante "+str(x)+" ingresado exitosamente!","--> Id generado:", insertar(cliente), '\n')
            x=x+1
            time.sleep(1)

    elif accion == 2:
        print("============= LISTA DE ESTUDIANTES =======") 
        for cliente in obtener():
            print("----------------------------------")
            print("Id: ", cliente["_id"])
            print("Nombres: ", cliente["nombres"])
            print("Dirección: ", cliente["direccion"])
            print("Email: ", cliente["email"])
            print("Saldo: ", cliente["saldo"])
            print("cedula: ", cliente["cedula"])
        print("=======", obtenerCant(), "ESTUDIANTES OBTENIDOS ========")
        
    elif accion == 3:
        id = input("Ingrese ID: ")
        productos_eliminados = eliminar(id)
        print("¡Estudiante eliminado exitosamente!")
    elif accion == 4:
        estudiantes_eliminados = eliminarTodo()
        print(estudiantes_eliminados, "¡Estudiante(s) Eliminado(s) exitosamente!")

    elif accion == 5:
        id = input("Ingrese ID: ")
        saldo = float(input("Cantidad a depositar: "))
        saldo_actualizado = actualizar(id, saldo, 1)
        print(saldo_actualizado)

    elif accion == 6:
        id = input("Ingrese ID: ")
        saldo = float(input("Cantidad a retirar: "))
        saldo_actualizado = actualizar(id, saldo, 2)
        print(saldo_actualizado)
