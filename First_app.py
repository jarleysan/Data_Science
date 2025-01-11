
edad = input ("Ingresa edad:>> ")
print (type(edad))
num =  int (edad)
# print (num + 15)

#------------------------------ Condicionales básicas
if num <= 18:
    print ("Menor de edad")
elif num > 18 and num <= 25:
    print ("Adulto joven")
elif num > 25 and num <= 60:
    print ("Adulto laboral")
else:
    print ("Pensionado")

#-------------------------------------- Arrays
lenguajes = ["Python","Ruby", "Java Script", "Java", "PHP"]
print (lenguajes)
print (lenguajes[1:3]) #Indice de listas

#--------------------------------------- Insert en arrays
lenguajes.insert (3,"VBA")
print (lenguajes)

#-------------------------------------   Delete en arrays 
lenguajes.remove ("PHP")
print ("PHP" in lenguajes)

#-------------------------------------  Bucle While 
i = 0
while i < len(lenguajes):
    print (lenguajes[i])
    i = i + 1

for lenguaje in lenguajes:
    print (lenguaje + " Curso")



#-------------------------------   Escape en string
# / se usa para introducir un caracter especifico ejem /"Python"/
#n introduce un espacio 
