# Mensaje de bienvenida.
print("\033[1m"+f"\nBienvenid@ al programa."+"\033[0m")

# Variables que se usaran en el programa:

# Variable que permita ejecutar el primer bucle.
num_datos = -1

#Variables de contador   
positivos = 0
negativos = 0
nulos = 0

# Bucle para que el usuraio ingrese un numero valido
while num_datos <= 0:

    # Funcion que permita que el bulce continue si el usuario ingresa un dato invalido  
    try:
        # Solicitar al usuario cuántos números desea ingresar
        num_datos = int(input("\n¿Qué cantidad de datos desea ingresar? -> "))

        if num_datos > 0:
            break
        print("\033[1m"+f"\nNo es posible ingresar la cantidad de datos escrita, por favor vuelva a intentarlo."+"\033[0m")

    # Mensaje que le indique al usuario que ha ingresado un dato invaido
    except ValueError:
        print("\033[1m"+f"\nUsted ingresó un valor que no es un número entero. Por favor ingrese un valor valido."+"\033[0m")

if num_datos <= 0:
    num_datos = 0

# Bucle para que el usuario ingrese los datos.
for i in range(num_datos):

    while True:
        # Funcion que permita que el bulce continue si el usuario ingresa un dato invalido   
        try:

            #Solicitar los números al usuario.
            dat = int(input(f"\nIngrese el dato #{i+1} -> "))
            
            # Contador de números positivos
            if dat > 0:
                positivos += 1

            # Contador de números negativos
            elif dat < 0:
                negativos += 1

            # Contador de números nulos
            else:
                nulos +=1

            break
        
        # Mensaje que le indique al usuario que ha ingresado un dato invaido
        except ValueError:
            print("\033[1m"+f"\nEl último dato ingresado es invalido. Por favor ingrese un valor valido."+"\033[0m")
        
# Mensajes que muesten la cantidad de numeros positivos, negativos y nulos escritos.
print(f"\nLa cantidad de números positivos ingresados es: {positivos}.")
print(f"La cantidad de números negativos ingresados es: {negativos}.")
print(f"La cantidad de números nulos ingresados es: {nulos}.\n")   

# Mensaje que indica el final del programa.
print("\033[1m"+"Fin del programa.\n"+"\033[0m")