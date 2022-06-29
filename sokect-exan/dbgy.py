import pymongo as pm
from pymongo.errors import ConnectionFailure
try:

    cliente="mongodb://facci:asd@192.168.0.130:27017/dbprueba"
    connection = pm.MongoClient(cliente)
    mydb = connection.get_database("dbprueba")
    mycol = mydb.get_collection("usuarios")
    mydict = {
             'id': '8',
             'nombre':'Stiven',
             'apellido':'Portillo',
             'edad':'26',
             'cedula':'130888',
             'Saldo':'5988$'
                }
    dataInserted = mycol.insert_one(mydict)
    print("ID:"+str(dataInserted.inserted_id))
    print ("Registro insertado")
    connection.close_cursor
    connection.close
except ConnectionFailure:
    print("Server no se encuentra disponible. Intente más tarde")