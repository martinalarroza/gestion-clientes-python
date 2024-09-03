
import csv



# FUNCION QUE ME PERMITE VALIDAR EL INGRESO DE PREFERENTE
def obtener_preferente():
    while True:
        respuesta = input("¿Es cliente preferente? (SI/NO): ").lower()
        if respuesta == "si" or respuesta == "no":
            break
        else:
            print("Respuesta inválida. Debes ingresar 'SI' o 'NO'.")
    
    return respuesta

             
# FUNCION QUE ME PERMITE VALIDAR EL INGRESO DE EDAD
def obtener_edad():
    while True:
        try:
            edad = int(input("Ingrese la edad del cliente: "))
            if edad < 0:
                print("La edad no puede ser un número negativo.")
            else:
                return edad
        except ValueError:
            print("Error: Debes ingresar un número entero para la edad.")

# FUNCION QUE ME PERMITE VALIDAR EL INGRESO DE DNI
def obtener_dni():
    while True:
        try:
            dni = input("Ingrese DNI del cliente: ")
            if len(dni) != 8 or not dni.isdigit():
                print("El DNI debe ser un número de 8 dígitos.")
            else:
                return dni
        except ValueError:
            print("Error: Debes ingresar un número válido para el DNI.")

# FUNCION QUE ME PERMITE VALIDAR EL INGRESO DE TELEFONO
def obtener_tel():
 while True:
  try:
    tel = int(input("Ingrese número de télefono del cliente: "))
    return tel
  except ValueError:
    print("Por favor, ingrese un número de teléfono válido.")


# FUNCION QUE ME PERMITE REPETIR UNA OPERACION Y LUEGO MOSTRAR EL MENU
def volver_a_preguntar():
      while True:
       opcion_continuar = input("¿Desea realizar la misma operación? (SI/NO): ").lower()

       if opcion_continuar == "si":
            return True
       elif opcion_continuar == "no":
            return False
       else:
            print("Respuesta inválida. Debe ingresar 'SI' o 'NO'.")
  

def mostrar_menu():
    print("Menu:")
    print("1. Añadir cliente")
    print("2. Eliminar cliente")
    print("3. Mostrar datos de un cliente")
    print("4. Listar todos los clientes con nombre y DNI")
    print("5. Listar clientes preferentes con nombre y DNI")
    print("6. Listar todas las personas que se llamen Pedro.")
    print("7. Calcular el promedio de edad de los clientes.")
    print("8. Salir  \n")


# OPCION N°1 
def opcion_1():
  while True:
    nombre = input("Ingrese el nombre del cliente: ")
    dni = obtener_dni()
    edad = obtener_edad()
    direccion = input("Ingrese dirección del cliente: ")
    telefono = obtener_tel()
    email = input("Ingrese mail del cliente: ")
    prefe = obtener_preferente()
     
    # ABRO EL ARCHIVO.CSV PARA escritura
    with open("datos_clientes.csv","a",newline='') as archivo:
    #   archivo.readline()

        archivo_writer = csv.writer(archivo, lineterminator="\n")

    # ESCRIBO LOS DATOS INGRESADOS EN EL ARCHIVO.CSV
        archivo_writer.writerow([dni,nombre, edad, direccion, telefono, email, prefe])

    if not volver_a_preguntar():
         break


# OPCION 2°
def opcion_2():

 while True:
          dni_eliminar = obtener_dni()
          eliminar_cliente(dni_eliminar)

          if not volver_a_preguntar():
           break

# FUNCION PARA ELIMINAR CLIENTE
def eliminar_cliente(dni_eliminar):

    clientes = []
    dni_encontrado = False

    # ABRE EL ARCHIVO.CSV PARA LECTURA
    with open('datos_clientes.csv', 'r') as archivo:
        reader = csv.reader(archivo)

    # COMPARA UNA FILA HASTA ENCONTRAR EL DNI DESEADO
        for fila in reader:
            if fila and fila[0] == dni_eliminar:
                print(f"Cliente con DNI {dni_eliminar} eliminado.")
                dni_encontrado = True
            else:
                clientes.append(fila)

        if not dni_encontrado:
         print(f"No se encontró ningún cliente con el DNI {dni_eliminar}")

    # ESCRIBE EL ARCHIVO CSV SIN LA FILA CORRESPONDIENTE AL CLIENTE ELIMINADO
    with open('datos_clientes.csv', 'w', newline='') as archivo_csv:
        escritor_csv = csv.writer(archivo_csv)
        for cliente in clientes:
            escritor_csv.writerow(cliente)


# OPCION 3 °
def opcion_3():
 while True:
          dni_ingresado = obtener_dni()
          mostrar_cliente_por_dni(dni_ingresado)

          if not volver_a_preguntar():
           break


def mostrar_cliente_por_dni(dni_ingresado):
    # ABRE MI ARCHIVO.CSV EN MODO LECTURA
    with open('datos_clientes.csv', 'r') as archivo:
        reader = csv.reader(archivo)
    # recorro la fila de dni hasta dar con el ingresado
        for fila in reader:
            if fila[0] == dni_ingresado:   #si el dni existe, muestro los datos relacionados a ese dni
                print('Cliente encontrado:')
                print('Nombre:', fila[1])  
                print('DNI:', fila[0])
                print('Edad:', fila[2])
                print('Direccion:', fila[3])
                print('Telefono:', fila[4])
                print('Email:', fila[5])

                return  
            # Termina la función después de encontrar el cliente

    print('Cliente no encontrado para el DNI', dni_ingresado)



# opcion 4°
def opcion_4():
    mostrar_clientes()

# funcion mostrar todos los clientes 
def mostrar_clientes():

# abre el archivo en modo lectura
# recorro el archivo y muestro todos los nombres y dni del archivo.csv
 with open("datos_clientes.csv", "r") as archivo:
     reader = csv.reader(archivo)
     for fila in reader:
       print("Nombre:", fila[0])
       print("DNI:", fila[1])


# opcion 5°
def opcion_5():
   preferentes = listar_preferentes()

def listar_preferentes():

    # abre el archivo en modo lectura
    # recorro el archivo y muestro todos los nombres y dni que esten asociados a preferentes positivos
    with open("datos_clientes.csv", "r") as archivo:
        reader = csv.reader(archivo)
        for fila in reader:
           if fila[6] == "si":
            print("Nombre:", fila[1])
            print("DNI:", fila[0])
            
# opcion6
def opcion_6():
   listar_pedros()


def listar_pedros():

    # abre el archivo en modo lectura
    # recorro el archivo y muestro todos los nombres y dni que esten asociados al nombre "Pedro"
    # utlizo funciones para str como .lower() y capitalize()
    with open("datos_clientes.csv", "r") as archivo:
     reader = csv.reader(archivo)
     for fila in reader:
        if "pedro" in fila[1].lower():
             print("Nombre:", fila[1].capitalize())
             print("DNI:", fila[0])
             
# OPCION 7°
def opcion_7():
    
    calcular_edad = promedio_edad()
  
    if calcular_edad is not None:
      print(f"\nEl promedio de edad de los clientes es: {calcular_edad:.1f} años \n")
    else:
      print("\nNo se encontraron edades para calcular el promedio.\n")


def promedio_edad():

   #abre el archivo en modo lectura
    with open('datos_clientes.csv', 'r') as archivo:
        reader = csv.reader(archivo)
        next(reader)  # Omite la primera fila (encabezados)
        
        total_edad = 0
        cantidad_clientes = 0
        
    # si la fila no está vacía, agrega la edad al total_edad y aumenta cantidad_clientes en 1
        for fila in reader:
            if fila:  
                total_edad += int(fila[2])
                cantidad_clientes += 1
        
    #verifica si cantidad_clientes es mayor que 0 para evitar la división por cero
        if cantidad_clientes > 0:
         promedio = total_edad / cantidad_clientes
         return promedio
        else:
         return None  # No existe clientes



while True:
    mostrar_menu()
    opcion = input("Selecciona una opción: ")

    if opcion == "1":
        opcion_1()
    elif opcion == "2":
        opcion_2()
    elif opcion == "3":
        opcion_3()
    elif opcion == "4":
        opcion_4()
    elif opcion == "5":
        opcion_5()
    elif opcion == "6":
        opcion_6()
    elif opcion == "7":
        opcion_7()
    elif opcion == "8":
        print("Saliendo...")
        
        break
    else:
        print("Opción inválida. Por favor, selecciona una opción válida.")




