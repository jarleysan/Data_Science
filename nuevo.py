#pruebas doble loop
for j in range (3):
    for k in range (2):
        print (f"{j},{k}")

print ("Bienevenido a la calculadora")
print ('Escriba "salir" para finalizar ejecución')
print ("Operaciones son sum, rest, div, mul")

resultado = "" 
while True:
    if not resultado:
        resultado = input ("Ingrese numero")
        if resultado.lower () == "salir":
            break
    op = input ("Ingrese operación: ")
    if op.lower() == "salir":
        break
    n2= input ("Ingrese numero ")
    if n2.lower() == "salir":
        break
    n2 = int (n2)

    if op.lower () == "sum":
        resultado += n2
    elif op.lower () == "rest":
        resultado -= n2
    elif op.lower () == "div":
        resultado /= n2
    elif op.lower () == "mul":
        resultado *= n2
    else:
        print ("Operacion no valida")
        break

    print (f"El resultado es{resultado}")

#----------------------------- Listas
rango = list(range (1,11))
primero, *otros, ultimo = rango
print (primero, ultimo, otros)