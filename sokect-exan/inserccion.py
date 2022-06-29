import pymongo as pm
import time
from pymongo.errors import ConnectionFailure
try:

    cliente="mongodb://administrador:asd123@server-quito,server-manta,server-guayaquil/?replicaSet=rsfacci&authMechanism=DEFAULT"    
    connection = pm.MongoClient(cliente, 27017, serverSelectionTimeoutMS=30000, connectTimeoutMS=30000, socketTimeoutMS=30000)
    
    mydb = connection["escuela"]
    mycol = mydb["estudiantes"]
    x=int(input("Ingrese el numero de registros a registrar: "))
    for i in range(1,x+1):
        mydict = {
                'id': str(i),
                'nombre':'Stiven'+str(i),
                'apellido':'Portillo',
                'edad':'26',
                'cedula':'130888',
                'Grado':'8vo',
                    }
        
        
        dataInserted=mycol.insert_one(mydict)        
        print("ID:"+str(dataInserted.inserted_id))
        print(mydict)
        time.sleep(1)
        print('Registro '+str(i)+' de '+str(x))
        print('------')

    connection.close_cursor
    connection.close
except ConnectionFailure:
    print("Server no se encuentra disponible. Intente más tarde")