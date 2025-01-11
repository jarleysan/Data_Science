#Funciones 
def prueba (nombre,edad):
    print (f"Bienvendido {nombre},tu edad es {edad}")

nombre = input ("Ingresa tu nombre: ")
edad = input ("Ingresa tu edad: ")

prueba (nombre, edad)

def suma(*numeros):
    resultado = 0
    for numero in numeros:
        resultado += numero
    print (resultado)

#------- Suma de ejemplo 
suma (1,5,4,8)
suma (18,5,1,98,54)


#-------- Key work arguments
def sumaotra (a, b):
    resultado = a + b
    return resultado

c = sumaotra (1, 5)
d = sumaotra (c, 10)
print (d)