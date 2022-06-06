import pymongo as pm



def get_user(cedula):
    cliente= pm.MongoClient('localhost', 27017)
    db=cliente.get_database("datos_usuarios")
    coleccion=db.get_collection("usuarios")
    usuario=coleccion.find_one({"cedula":cedula}) 
    # if len(usuario)==0:
    #     return 'No existe el usuario con cedula: '+cedula
    cliente.close()
    
    return usuario

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



