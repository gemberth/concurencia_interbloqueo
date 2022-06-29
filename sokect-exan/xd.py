import time
# ciclo for que resiva un rango por consola
x=int(input("Ingrese el numero de registros a registrar: "))


for i in range(1,x+1):
    mydict = {
             'id': str(i),
             'nombre':'Stiven'+str(i),
             'apellido':'Portillo',
             'edad':'26',
             'cedula':'130888',
             'Saldo':'5988$'
                }
    print(i)
    print(mydict)
    time.sleep(1)
    print('Registro '+str(i)+' de '+str(x))
    print('------')
