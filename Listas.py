mascotas = ["Pepe", "Pulga", "Tommy", "Chancho", "Luna", "Max"]

# Modificaciones de listas 
mascotas.insert (1,"Melvin") # --- Inserta en una posición específica
mascotas.append ("Nuevo chancho") # --- Inserta al final 
mascotas.remove ("Pepe") # --- Borra por el dato, no por el index
mascotas.pop ()# --- Elimina el último
del mascotas [2] # --- Elimina por index

mascotas.sort() # --- Ordena el arreglo 
nuevalista = sorted (mascotas) # ---Ordena el arreglo pero lo vuelve una nueva variable


usuarios = [["Juan Carlos", 1],["Jarley Santos", 2], ["Richard Briceno", 3], ["Gerardo", 5]]
nombres = [usuario [0] for usuario in usuarios]
print (nombres)

# Cuando inicia con [] son  listas y se puede modificar, si la variable inicia con () son tuplas y no se pueden modificar
# Set o data set {} quita los elementos duplicados
#tuple () convierte una lista en una tupla || set() convierte de una lista o tupla en un set 

# union de set, o tuplas: variable = (set | set2)
# intereseccion (Cuando hay datos iguales en dos set) variable = (set & set2)
# diferencia izq que no coincide en la derecha  variable  = (set - set2)
# diferencia simetrica (es decir los que no coincida en ambos) = variable = (set ˄ set2)

diccionario = {"x":25,"y": 50}
# La llave que recibe son string siempre 
print (diccionario.get ("x"))
# No existen index dentro de un diccionario 
del diccionario["x"] # borra la llave de un diccionario 

for valor in diccionario:
    print (valor, diccionario[valor])
    
for llave, valor in diccionario.items ():
    print (llave, valor)
    
    


