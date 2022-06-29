import pymongo as pm
import asyncio

async def get_user(cedula):
    cliente= pm.MongoClient('mongodb://facci:asd@192.168.0.125:27017/dbprueba')
    db=cliente.get_database("datos_usuarios")
    coleccion=db.get_collection("usuarios")
    usuario=coleccion.find_one({"cedula":cedula}) 
    # if len(usuario)==0:
    #     return 'No existe el usuario con cedula: '+cedula

    
    return usuario
    
# cliente= pm.MongoClient('mongodb+srv://aeiou2022:facci2022@cluster0.pj50i.mongodb.net/?retryWrites=true&w=majority')
# db=cliente.get_database("datos_usuarios")
# coleccion=db.get_collection("usuarios")
# usuario=coleccion.insert_one({
#             'id': '8',
#             'nombre':'Stiven',
#             'apellido':'Portillo',
#             'edad':'26',
#             'cedula':'130888',
#             'Saldo':'5988$'
#         },) 
# print(usuario)



# ced=get_user("1302222222")
# print(ced)
    



    

# for document in coleccion.find({
   
   
#     # 'edad':{'$gt':'21'}
# }):
#     print(document)
# doc=coleccion.find_one(
#     {
#         'cedula':'1303333333'
#     })


# print(doc)
# cliente.close()
# cliente= pm.MongoClient('localhost', 27017)
# db=cliente.get_database("datos_usuarios")
# coleccion=db.get_collection("usuarios")
# coleccion.update_one({
#     'id':'1'
# },{'$set':{
    
#     'Saldo':'9356$'

#      }})
# coleccion.insert_one({ 
#     'id': '4',
#             'nombre':'Esteban',
#             'apellido':'Moreira',
#             'edad':'21',
#            'cedula':'1304444444',
#           'Saldo':'8598$'


# })

cliente= pm.MongoClient('mongodb://administrador:asd123@server-quito,server-manta,server-guayaquil/?replicaSet=rsfacci&authMechanism=DEFAULT')
db=cliente.get_database("dbprueba")
coleccion=db.get_collection("usuarios")
# usuario=coleccion.find_one({"cedula":cedula})
usuarios1=coleccion.find( {})
print(usuarios1)
print('------')
for usuario in usuarios1:
    print(usuario)
# coleccion.insert_many(
#     [ 
#         {
#             'id': '1',
#             'nombre':'juan',
#             'apellido':'perez',
#             'edad':'20',
#             'cedula':'1301111111',
#             'Saldo':'1598$'
#         },
#         {
#             'id': '2',
#             'nombre':'Diago',
#             'apellido':'Mero',
#             'edad':'22',
#             'cedula':'1302222222',
#             'Saldo':'1598$'
#         },
#         {
#             'id': '3',
#             'nombre':'Diago',
#             'apellido':'Mero',
#             'edad':'22',
#             'cedula':'1303333333',
#             'Saldo':'1598$'
#         },
        
#     ]
# ) 



