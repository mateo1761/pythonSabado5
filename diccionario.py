'''
diccionario = {
    'nombre': "Mateo",
    'edad': 20,
    'trabaja': True,
    'comidas':['fesa','chocolate','piza']
}

print(diccionario)
print(diccionario['comidas'])
print(diccionario['comidas'][0])
'''

##Imprimiendo por el usuario
diccionario = {

}

diccionario['comidas'] = input('Digite su nombre: ')

print(diccionario)
print(diccionario['comidas'])

#recorriendo datos

for llave,valor in diccionario.items():
    print(llave)
    print(valor)