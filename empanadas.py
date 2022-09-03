print("***MENU***")
print("1. Agregar 1 empanada")
print("2. Mostrar Empanada")
print("3. Salir")
opcion = 100
#DATOS EMPANADA
#SABOR
#Ingredientes (x3)
#Precio de fabricación
#Precio de venta

empanadas = []
ingredientes = []

while(opcion != 3):
    empanada = {}
    menu = int(input('Ingrese un numero: '))
    if(menu == 1):
        empanada['Sabor'] = input('Digite el sabor de la empanada: ' )
        empanada['ingredientes']=[]

        for i in range(3):
            ingredientes.append(input(f'{i + 1}.Digita el ingrediente: '))

        empanada['PrecioFabricacion'] = int(input('Digite el valor: '))

        empanada['PrecioVenta'] = int(input('Digite el precio de venta: '))
        
        empanadas.append(empanada)
        print("Agregando empanada")
    elif(menu == 2):
        print(empanadas)
else:
    print('Digite una opcion valida')



