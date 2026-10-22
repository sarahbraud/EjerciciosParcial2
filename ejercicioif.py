nombre = " "
edad = 0
nacionalidad = " "

nombre = input("Ingrese su nombre: ")
edad = int(input("Ingrese su edad: "))
nacionalidad = input("Ingrese su nacionalidad: ")

if edad >= 18:# el if va seguido de una condicion, si la condicion es verdadera se ejecuta el bloque de codigo que esta indentado
    print("Usted es mayor de edad") 
else  # el else se ejecuta si la condicion del if es falsa
    print("Usted es menor de edad") 

if nacionalidad == "N": # el if va seguido de una condicion, si la condicion es verdadera se ejecuta el bloque de codigo que esta indentado
    print("Eres de nacionalidad mexicana")  
else # el else se ejecuta si la condicion del if es falsa
    print("No eres de nacionalidad mexicana")  