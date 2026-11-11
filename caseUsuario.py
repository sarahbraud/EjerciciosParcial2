name= ""
lastName= ""
age= 0
birthday= ""
email= ""
password= ""
confirmPass= ""
opcion= 0

print("Bienvenido al sistema de registro de usuarios")
print("MENU PRINCIPAL")
print("1. Registrar usuario")
print("2. Ver informacion del usuario")
print("3. Borrar infromacon del usuario")
print("5. Salir")
print("------------")
opcion= int(input("Selecciona una opcion"))

match opcion #Aqui inicia el match, que es una validacion de caso

case 1:
name= input("Ingresa tu nombre:")
lastName= input("Ingresa tu apellido:")
age= int(input("Ingresa tu edad:"))
birthday= input("Ingresatu fecha de nacimiento:")
email= input ("Ingresa tu correo electronico:")
password= input ("Ingresa tu contrasena:")
confirmPass= input ("Confirma tu contrasena:")
case 2:
print("Nombre:", name, "Edad:", age, "Fecha de nacimiento:", birthday, "Correo electronico:", email, "Contrasena:", password)
case 3:
name= ""
lastName= ""
age= 0
birthday= ""
email= ""
password= ""
case 4:
name= input("Ingresa tu nombre:")
lastName= input("Ingresa tu apellido:")
age= int(input("Ingresa tu edad:"))
birthday= input("Ingresa tu fecha de nacimiento:")
email= input("Ingresa tu correo electronico:")
case 5:
print ("¡Hasta luego!")
case _:
print ("Opcion no valida")
