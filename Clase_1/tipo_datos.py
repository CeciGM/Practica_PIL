a = "Esto es una cadena"
b = "Esto es otra cadena"

print(a, type(a))
print(b, type(b))

#c = str(120,56)
#print(c, type(c))

print(len(a))
print(a[5])
print(a[:3])
print(a[-1])

# Metodos
print(a.lower())
print(a.upper())
print(a.split())

# List
lista_1=["Hola", 4, 2.5, True, [8,"ana"]]
print(lista_1, type(lista_1))
print(len(lista_1))
print(lista_1[2])

var_1 = lista_1[4]
print(var_1)

# Metodo---------------------
lista_1.append("lista")
print(lista_1)

print(lista_1.index([8,"ana"]))

lista_1.insert(3,"sol")
print(lista_1)

# Diccionario --------------------
usuario = {
    "nombre" : "Octavio",
    "apellido": "Gomez",
    "edad" : 38,
    "hobbies" : ['futbol','musica'],
    'Mascotas': False
}
print(usuario)
#Busco con las KEYS
print(usuario["edad"])

print(len(usuario))
print(len(usuario["hobbies"]))

#Metodos de Dicc
print(usuario.get("hobbies"))
print(usuario.get("direccion", "no encontrado"))

keys_usuario = usuario.keys()
print(type(keys_usuario))

#print(usuario.get(keys_usuario[0]))

keys_usuario = list(usuario.keys()) #si no hago esto me da error al hacer get sobre el dicc
print(usuario.get(keys_usuario[0]))

print(usuario.values())