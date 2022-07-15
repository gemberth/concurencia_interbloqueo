import pymongo as pm
import time 
from pymongo.errors import ConnectionFailure
try:

    cliente="mongodb://administrador:asd123@server-quito,server-manta,server-guayaquil/?replicaSet=rsfacci&authMechanism=DEFAULT"    
    connection = pm.MongoClient(cliente, 27017, serverSelectionTimeoutMS=30000, connectTimeoutMS=30000, socketTimeoutMS=30000)
    
    mydb = connection["colegio"]
    mycol = mydb["docentes"]
    x=int(input("Ingrese el numero de registros a registrar: "))
    for i in range(1,x+1):
        mydict = {
                'id': str(i),
                'nombre':'Roberto'+str(i),
                'apellido':'Zambrano',
                'edad':'36',
                'cedula':'1314589765',
                'Grado':'8vo',
                'Materia':'Fisica',
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